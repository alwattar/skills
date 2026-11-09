---
name: architecture-decision
description: Compare architecture alternatives and capture an owner decision.
---

# Architecture Decision
Compare realistic alternatives across complexity, operations, security, reversibility, migration, testing and maintainability.
Recommend; owner decides. Approval gate required.

## Documentation language

Before creating or updating any repository engineering artifact, follow `policies/documentation-language.md`.

Follow the consuming project's approved documentation language (English by default). Preserve externally pasted ticket source text verbatim.

Do not apply this rule to localization files or explicitly requested translation artifacts.

## Interactive decision protocol

Whenever this skill needs an owner decision, follow `policies/interactive-decisions.md`.

- Prefer structured single-select/multi-select only if the host exposes such an interaction.
- Otherwise render equivalent A/B/C text options.
- Provide realistic domain-specific choices.
- Include a recommendation when justified.
- Always provide `Other / Custom` unless the option set is logically exhaustive.
- Do not ask the user to type information that can be selected safely.
- Do not force bounded options onto a genuinely open-ended question.

## Architecture choice interaction

Present architecture alternatives as selectable choices after comparing their consequences.

The comparison may be detailed, but the final owner action should be simple:
- choose one option;
- choose multiple only when combinations are genuinely valid;
- or select Other/Custom and describe a different architecture.

The recommendation is advisory, never an automatic decision.
