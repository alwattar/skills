---
name: project-discovery
description: Discover product purpose, users, scope and workflows.
---

# Project Discovery
Facts are investigated; decisions belong to the owner.
Cover problem, users, outcomes, capabilities, workflows, non-goals, terminology and constraints.
Exit when no major product assumption remains silently implicit.

## Documentation language

Before creating or updating any repository engineering artifact, follow `.agents/workflow/rules/documentation-language.md`.

Keep canonical documentation, specs, tickets, ADRs, plans, audits, and handoffs in English even when the conversation with the user is in another language.

Do not apply this rule to localization files or explicitly requested translation artifacts.

## Interactive decision protocol

Whenever this skill needs an owner decision, follow `.agents/workflow/rules/interactive-decisions.md`.

- Prefer structured single-select/multi-select only if the host exposes such an interaction.
- Otherwise render equivalent A/B/C text options.
- Provide realistic domain-specific choices.
- Include a recommendation when justified.
- Always provide `Other / Custom` unless the option set is logically exhaustive.
- Do not ask the user to type information that can be selected safely.
- Do not force bounded options onto a genuinely open-ended question.

## Discovery rounds

Prefer 2–5 frontier decisions per round.

For bounded product decisions such as target market, customer type, language strategy, deployment model, or user roles, use selectable options.

For open discovery such as "what hurts most today?", allow free-form input while providing examples that help the owner answer faster.
