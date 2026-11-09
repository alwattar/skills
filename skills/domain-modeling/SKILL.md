---
name: domain-modeling
description: Clarify vocabulary, entities, lifecycle and invariants.
---

# Domain Modeling
Route vocabulary → CONTEXT, behavior → PRODUCT, entities/lifecycle/invariants → DATA-MODEL, rationale-backed decisions → DECISIONS.

## Interactive decision protocol

Whenever this skill needs an owner decision, follow `.agents/workflow/rules/interactive-decisions.md`.

- Prefer structured single-select/multi-select only if the host exposes such an interaction.
- Otherwise render equivalent A/B/C text options.
- Provide realistic domain-specific choices.
- Include a recommendation when justified.
- Always provide `Other / Custom` unless the option set is logically exhaustive.
- Do not ask the user to type information that can be selected safely.
- Do not force bounded options onto a genuinely open-ended question.
