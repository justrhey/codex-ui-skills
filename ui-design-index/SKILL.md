---
name: ui-design-index
description: Use when the user wants UI/UX design inspiration, motion, component references, or patterns distilled from design galleries and React UI libraries, and you need to pick the right category — mobile app, landing page, design system/dashboard, or e-commerce/portfolio. The front door / router for the ui-* design-knowledge skill set.
---

# UI Design Index (Router)

## Overview

A hand-curated set of design-knowledge references distilled from top work on **Dribbble**, **Pinterest**, and **Awwwards**. Each category lives in its own skill so you load only what the task needs. This skill is the router: identify the surface being designed, then open the matching skill.

These are **reference skills**, not live scrapers — the sites rate-limit, gate behind auth, and block bots. The distilled patterns below are reliable, offline, and load instantly. For fresh examples, pair with WebSearch on `site:dribbble.com`, `site:awwwards.com`, or `pinterest.com` for the specific pattern.

## React component and motion references

Use these as implementation references after choosing a surface. Prefer the smallest primitive that matches the interaction; do not copy a gallery demo wholesale or add a dependency just for decoration.

| Need | Reference | Best for | Guardrails |
|---|---|---|---|
| Declarative React animation, gestures, layout, presence | [Motion](https://motion.dev/docs/react) | Production page transitions, dialogs, draggable/reorderable UI, scroll-linked state | Respect reduced motion; keep layout animation off large lists; import only the APIs used |
| Copy-paste animated React primitives | [Motion Primitives](https://motion-primitives.com/) | Focus rings, text reveals, modal transitions, animated lists, cursor/hover treatments | Treat examples as source material; audit keyboard behavior and bundle cost before adoption |
| Artistic animated components and effects | [React Bits](https://www.reactbits.dev/get-started/index) | Hero accents, text effects, backgrounds, cursor/hover experiments | Use sparingly in product workflows; avoid WebGL/canvas effects when a CSS transform works |
| React component registry and blocks | [Watermelon UI](https://ui.watermelon.sh/) | Dashboard blocks, forms, marketing sections, composed layouts | Check license and underlying dependencies; extract structure/tokens instead of importing a whole page |
| Accessible unstyled interaction primitives | [Radix UI](https://www.radix-ui.com/primitives), [React Aria](https://react-spectrum.adobe.com/react-aria/) | Dialogs, popovers, menus, tabs, comboboxes, focus management | Preserve semantic labels, focus return, escape behavior, and announcements |
| Headless layout primitives | [Headless UI](https://headlessui.com/), [Ark UI](https://ark-ui.com/) | Framework-neutral menus, disclosures, selects, dialogs | Verify the project’s React/version compatibility before adding a package |
| Composable design-system starter | [shadcn/ui](https://ui.shadcn.com/) | Local-owned components built on Radix/Tailwind, forms, data display | Copy only needed components; keep tokens in the project’s design system |
| High-polish ready-made blocks | [Aceternity UI](https://ui.aceternity.com/), [Magic UI](https://magicui.design/), [Origin UI](https://originui.com/) | Landing-page sections, animated cards, navigation patterns | These are inspiration/starting points, not proof of accessibility or performance |
| Production design systems | [MUI](https://mui.com/), [Base Web](https://baseweb.design/), [Chakra UI](https://chakra-ui.com/) | Dense application screens, tables, theming, responsive states | Do not mix competing system resets/tokens without an explicit boundary |

### Motion selection rules

1. Start with CSS transitions for opacity, color, transform, and simple hover/focus states.
2. Use Motion when state, presence, gesture, layout, or scroll orchestration is the actual problem.
3. Use Motion Primitives or React Bits only after identifying the exact primitive to extract; remove unrelated demo code.
4. Keep motion subordinate to hierarchy and feedback. Never animate a required action, error, or security warning in a way that delays comprehension.
5. Every animated interaction needs a reduced-motion path, keyboard path, focus visibility, and a no-JavaScript failure state where practical.
6. Check bundle impact and avoid shipping an entire registry or animation runtime for one effect.

## Route to the Right Skill

| The user is designing... | Open skill | Triggers |
|---|---|---|
| A phone/tablet app screen, native flow, gesture UI | **ui-mobile-patterns** | iOS, Android, app, onboarding, tab bar, bottom sheet |
| A marketing/hero page, product launch, scroll story | **ui-landing-patterns** | landing, hero, above-the-fold, conversion, CTA, awwwards |
| A component system, admin panel, SaaS dashboard, data table | **ui-design-systems** | dashboard, admin, tokens, components, tables, charts |
| A shop, checkout, product page, portfolio, editorial | **ui-commerce-portfolio** | store, cart, PDP, checkout, portfolio, agency, case study |

Ambiguous request → ask which surface, or open the two closest and merge.

## Relationship to `ui-ux-pro-max`

`ui-ux-pro-max` is the deep implementation library (50+ styles, 161 palettes, 57 font pairings, stack-specific code). Use **these ui-* skills** for *what good work in a category looks like and why* (inspiration, patterns, references); use **ui-ux-pro-max** for *how to build it in a given stack* (concrete tokens, components, code). They complement — pull direction here, then implement there.

## How to Use a Category Skill

1. Open the matching skill and read its pattern tables.
2. Pick 2–3 patterns that fit the brief; note *why* they work (the skills explain the reasoning, not just the look).
3. For live inspiration, WebSearch the pattern name + platform.
4. Hand direction to `ui-ux-pro-max` or `frontend-design` for implementation.

## Common Mistakes

- **Copying a shot literally** — Dribbble shots are often non-functional concept art. Steal the *idea* (hierarchy, motion, spacing), not the exact pixels.
- **Loading everything** — open only the one category skill you need.
- **Skipping the "why"** — each pattern includes rationale; ignoring it produces templated slop.
