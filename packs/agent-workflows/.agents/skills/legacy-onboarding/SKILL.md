---
name: legacy-onboarding
description: Reverse-engineer a legacy project before normal work.
---

# Legacy Project Onboarding
Survey implementation/docs/config/history. Classify VERIFIED/CONDITIONAL/UNCERTAIN/REFERENCED BUT NOT IMPLEMENTED/LEGACY.
Show source→doc mapping, gaps and conflicts, then stop for owner approval before rewriting docs.

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
