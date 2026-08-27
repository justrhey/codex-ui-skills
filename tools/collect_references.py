#!/usr/bin/env python3
"""Collect small, robots-aware UI reference records from public URLs.

This intentionally avoids stealth behavior, browser fingerprint spoofing,
CAPTCHA/login bypasses, and broad discovery. Pass exact URLs or a newline-
delimited file of URLs that you are allowed to fetch.
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


USER_AGENT = "codex-ui-reference-collector/1.0 (+contact-the-site-owner)"


class PageSummary(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title: list[str] = []
        self.description = ""
        self.headings: list[str] = []
        self._in_title = False
        self._in_heading = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag in {"h1", "h2", "h3"}:
            self._in_heading = True
        elif tag == "meta" and attrs_dict.get("name", "").lower() == "description":
            self.description = (attrs_dict.get("content") or "").strip()

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag in {"h1", "h2", "h3"}:
            self._in_heading = False

    def handle_data(self, data: str) -> None:
        value = " ".join(data.split())
        if not value:
            return
        if self._in_title:
            self.title.append(value)
        elif self._in_heading and len(self.headings) < 12:
            self.headings.append(value)


def robots_allows(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    robots_url = urllib.parse.urlunparse((parsed.scheme, parsed.netloc, "/robots.txt", "", "", ""))
    parser = urllib.robotparser.RobotFileParser(robots_url)
    try:
        parser.read()
    except (OSError, urllib.error.URLError):
        # A missing/unreachable robots file is not permission to crawl broadly;
        # the caller still supplies the exact URL and the collector stays bounded.
        return True
    return parser.can_fetch(USER_AGENT, url)


def fetch(url: str, timeout: float) -> tuple[str, str]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get_content_type()
        if content_type != "text/html":
            raise ValueError(f"expected text/html, got {content_type}")
        return response.read(1_500_000).decode(response.headers.get_content_charset() or "utf-8", "replace"), response.geturl()


def collect(url: str, delay: float, timeout: float) -> dict[str, object]:
    captured_at = datetime.now(timezone.utc).isoformat()
    record: dict[str, object] = {
        "url": url,
        "source": urllib.parse.urlparse(url).netloc,
        "captured_at": captured_at,
        "surface": "unknown",
        "pattern": "unknown",
        "evidence": [],
        "layout": "",
        "type_scale": "",
        "color_roles": "",
        "spacing": "",
        "interaction": "",
        "accessibility": "",
        "license_or_usage_note": "Inspect source terms before reuse.",
        "confidence": "low",
    }
    if not robots_allows(url):
        record["evidence"] = ["robots.txt disallows this URL"]
        record["confidence"] = "blocked"
        return record
    try:
        html, final_url = fetch(url, timeout)
        summary = PageSummary()
        summary.feed(html)
        record["url"] = final_url
        record["evidence"] = [
            f"title: {' '.join(summary.title)[:180]}",
            *[f"heading: {heading[:180]}" for heading in summary.headings],
        ]
        if summary.description:
            record["evidence"].append(f"description: {summary.description[:240]}")
        record["confidence"] = "medium" if record["evidence"] else "low"
    except (OSError, ValueError, urllib.error.URLError) as error:
        record["evidence"] = [f"fetch failed: {error.__class__.__name__}"]
        record["confidence"] = "error"
    finally:
        time.sleep(delay)
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("urls", nargs="*", help="Exact public URLs to inspect")
    parser.add_argument("--file", type=Path, help="Newline-delimited URL file")
    parser.add_argument("--output", type=Path, default=Path("references.json"))
    parser.add_argument("--delay", type=float, default=2.0, help="Seconds between requests")
    parser.add_argument("--timeout", type=float, default=15.0)
    args = parser.parse_args()

    urls = list(args.urls)
    if args.file:
        urls.extend(line.strip() for line in args.file.read_text().splitlines() if line.strip() and not line.startswith("#"))
    if not urls:
        parser.error("provide exact URLs or --file")
    if args.delay < 0 or args.timeout <= 0:
        parser.error("--delay must be non-negative and --timeout must be positive")

    records = [collect(url, args.delay, args.timeout) for url in urls]
    args.output.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {len(records)} reference records to {args.output}")


if __name__ == "__main__":
    main()
