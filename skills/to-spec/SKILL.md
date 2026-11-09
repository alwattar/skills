---
name: to-spec
description: Turn approved understanding into an implementation-ready spec.
---

# To Spec
Record approval evidence before implementation; the detailed owner request can serve as the approved spec when it settles scope and behavior. Unresolved material choices still require an owner decision.
Include goals, non-goals, actors, behavior, invariants, flows, data/integration impact, failures, migration, acceptance criteria, verification and doc impact.

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
