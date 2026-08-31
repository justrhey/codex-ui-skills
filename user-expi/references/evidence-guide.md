# Evidence guide

Use this as a search map, not as permission to apply every item. Re-check sources when the population, device, task, or claim differs.

## Widely used foundations

| Topic | Evidence and useful implication | Boundary or misuse to avoid |
|---|---|---|
| Target acquisition | Fitts-style models relate movement difficulty to distance and effective target size. Make important controls comfortably targetable and separated. ([Gillan et al., 1992](https://doi.org/10.1016/0953-5438(92)90019-C)) | The correct target width depends on direction, movement sequence, input method, and task. “Make every button huge” is not the law. |
| Choice reaction | Reaction time grows with the information conveyed by alternatives. Clarify categories, labels, and likely choices. ([Hyman, 1953](https://doi.org/10.1037/h0056940)) | It does not establish a universal maximum number of menu items or justify hiding necessary choices. Familiarity, probability, and stimulus-response compatibility matter. |
| Working memory | Capacity is limited and often closer to about four chunks under constrained conditions than the popular seven-item slogan. Externalize state and avoid recall-heavy flows. ([Cowan, 2001](https://doi.org/10.1017/S0140525X01003922)) | A chunk depends on knowledge and task. Do not convert the estimate into “show exactly four things.” Recognition and persistent context change the problem. |
| Cognitive load | Unnecessary means-end processing can consume capacity needed for learning. Sequence complex tasks, provide relevant context near the action, and reveal detail when needed. ([Sweller, 1988](https://doi.org/10.1207/s15516709cog1202_4)) | The original evidence concerns learning and problem solving; transfer to ordinary product UI must be justified and tested. “Minimal UI” is not automatically low load. |
| Accessible perception and operation | WCAG 2.2 defines testable requirements for contrast, resizing, reflow, text spacing resilience, focus, alternatives to dragging, and minimum target size. ([W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)) | WCAG values are conformance criteria, not a complete UX theory. AAA guidance and exceptions must not be presented as universal AA requirements. |

## Less-obvious findings and useful corrections

| Topic | Evidence and useful implication | Boundary or misuse to avoid |
|---|---|---|
| Change blindness | Users can miss even meaningful display changes when attention is elsewhere. Keep feedback near the action, preserve state long enough to inspect, and announce critical changes through more than transient animation. ([Tse, 2004](https://doi.org/10.1016/j.cogsci.2003.12.002)) | Salience alone does not guarantee notice. Validate the actual task and attentional demands. |
| Foreground bias | Foreground elements may receive attention while background changes go unnoticed. Treat layering, contrast, and occlusion as attention allocation, not decoration. ([Mazza, Turatto & Umiltà, 2005](https://doi.org/10.1007/s00426-004-0174-9)) | A single scene experiment does not define a universal z-index recipe. |
| Visual complexity and prototypicality | Website complexity and familiarity can shape aesthetic impressions extremely quickly. Preserve recognizable structure while concentrating novelty where it supports the product. ([Tuch et al., 2012](https://doi.org/10.1016/j.ijhcs.2012.06.003)) | First-impression aesthetics do not prove task usability, trustworthiness, conversion, or long-term preference. |
| Aesthetic-usability perception | Aesthetics can influence perceived usability. Visual coherence therefore matters to confidence and expectations. ([Tractinsky, Katz & Ikar, 2000](https://doi.org/10.1016/S0953-5438(00)00031-X)) | Perceived usability is not actual usability. Never use polish to mask friction, risk, or inaccessible behavior. |
| Menu breadth and depth | Multiple menu studies find costs from deep hierarchies and context-dependent benefits from broader, shallower structures. ([Kiger, 1984](https://doi.org/10.1016/S0020-7373(84)80018-8); [screen-reader replication, 2010](https://doi.org/10.1016/j.intcom.2010.02.003)) | “Eight or nine items” came from particular tasks. Information scent, ordering, expertise, screen size, language, and input method can change the result. |
| Choice overload | A large meta-analysis found a near-zero mean effect with substantial variation; later experiments point to choice complexity as a moderator. Improve comparability and decision support before blindly cutting options. ([Scheibehenne, Greifeneder & Todd, 2010](https://doi.org/10.1086/651235); [Greifeneder, Scheibehenne & Kleber, 2010](https://doi.org/10.1016/j.actpsy.2009.08.005)) | “More than N choices overwhelms users” is not supported as a universal rule. |

## Research quality check

For each proposed implication, ask:

- Is this a primary study, synthesis, standard, expert heuristic, or design analogy?
- Do the participants, culture, language, ability, device, environment, and task resemble the product context?
- Is the result replicated, contested, or dependent on moderators?
- Does the source measure task success, behavior, recall, perception, preference, or only self-report?
- What product observation would contradict the proposed implication?
- Can the design be tested without manipulating or harming users?

Prefer outcome language such as “is expected to reduce search time” over “will increase conversion.”
