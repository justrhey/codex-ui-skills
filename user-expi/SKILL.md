---
name: user-expi
description: Research and apply human psychology to app and system flows, information architecture, layout, hierarchy, text sizing, placement, interaction, and UX copy, then connect the findings to ui-design-index before implementation. Use for evidence-led UI/UX design, redesign, or review; do not use psychology to create deceptive or coercive dark patterns.
---

# USER-EXPI

Design for how people notice, understand, decide, act, recover, and remember. Treat psychology as contextual evidence, not a bag of universal “UX laws.”

## Workflow

1. **Frame the behavior.** Identify the surface, target users, primary task, environment/device, user state, risk, frequency, and measurable outcome. Inspect the existing product and instructions when available. Mark consequential unknowns instead of inventing personas.
2. **Map the flow.** For each stage record: user goal, information needed, choice/action, likely error or hesitation, feedback, recovery, and success signal. Separate first-use, routine, and error paths when they differ.
3. **Research the psychology.** Search current scholarly or standards sources for the specific behavior. Start with systematic reviews, meta-analyses, standards, and primary HCI/psychology studies; use summaries only to discover sources. Read [references/evidence-guide.md](references/evidence-guide.md) for the seed evidence and common misuses.
4. **Build an evidence ledger.** For every principle used, record the source, participants/task, finding, confidence, boundary conditions, design implication, and what would falsify the implication. Label evidence `strong`, `promising`, `contested`, or `analogy-only`. Never turn correlation or a lab effect into a guaranteed product outcome.
5. **Translate evidence into decisions.** Address only the levers relevant to the task: flow order, grouping, navigation depth, disclosure, hierarchy, control placement and target size, typography, wording, feedback, defaults, error prevention, and recovery. Give each decision a user problem and evidence trail.
6. **Connect to `ui-design-index`.** Open `ui-design-index`, route to the matching surface skill, and choose 2–3 compatible visual or interaction patterns. Psychology defines the behavioral constraints; the UI skill supplies category-specific expression. If they conflict, preserve comprehension, accessibility, task success, and user control.
7. **Implement when the request authorizes changes.** Inspect the real stack and conventions, make the smallest coherent change, preserve the existing design system, and cover responsive, keyboard, assistive-technology, loading, empty, error, and reduced-motion states. A review-only request remains report-only.
8. **Verify rather than declare.** Check relevant automated gates, WCAG requirements, responsive behavior, and the target flow. Distinguish source-backed expectations from observed product results. Recommend a focused usability test or product metric for claims that implementation alone cannot prove.

## Decision rules

- Optimize the primary task without hiding secondary or safety-critical actions.
- Reduce complexity by clarifying groups, labels, sequence, and progressive disclosure—not merely deleting options.
- Keep related labels, controls, help, errors, and consequences spatially and temporally close.
- Use visual weight and placement to express task priority; do not rely on color, motion, or position alone.
- Size text from font metrics, script, viewport, reading distance, content density, and user settings. Prefer relative units and zoom/reflow resilience over a universal pixel value.
- Make frequent or important targets easy to acquire, but evaluate input method, movement path, target shape, and spacing before invoking Fitts' law.
- Preserve user agency. Do not use scarcity pressure, obstruction, disguised ads, confirmshaming, hidden costs, forced continuity, or asymmetric cancellation.
- Accessibility standards are a floor. Psychology never overrides semantics, contrast, focus, reflow, text resizing, or input alternatives.

## Output

Before code, provide a compact rationale containing:

1. the behavioral goal and flow map;
2. the evidence ledger, including at least one widely used principle and one less-obvious or corrective finding when relevant;
3. the selected `ui-design-index` route and patterns;
4. concrete decisions for layout, type, placement, copy, and states;
5. validation criteria and unresolved assumptions.

After implementation, add changed files and exact verification results. Cite direct sources; do not cite a named “law” without its limits.
