---
name: grill
description: Clarify a request using a design-tree interview.
---

# Grilling
Build a design tree and ask only the current frontier.
Challenge ambiguity, permissions, edge cases, failure modes, lifecycle and reversibility.
Exit when material requirements are explicit.

## Interactive decision protocol

Whenever this skill needs an owner decision, follow `.agents/workflow/rules/interactive-decisions.md`.

- Prefer structured single-select/multi-select only if the host exposes such an interaction.
- Otherwise render equivalent A/B/C text options.
- Provide realistic domain-specific choices.
- Include a recommendation when justified.
- Always provide `Other / Custom` unless the option set is logically exhaustive.
- Do not ask the user to type information that can be selected safely.
- Do not force bounded options onto a genuinely open-ended question.

## Question shape

Each owner-decision question should normally contain:
1. a short title;
2. the decision being made;
3. realistic options;
4. single-select or multi-select semantics;
5. `Other / Custom` when applicable;
6. a recommendation and concise rationale;
7. only the follow-up context needed to choose.

Do not mix multiple dependent decisions into one selection.
