---
name: to-tickets
description: Split a spec into the minimum useful number of tickets.
---

# To Tickets

**Default: ONE ticket.**

Before creation announce:
- Size
- Proposed ticket count
- Proposed wave count
- Reason

Policy:
- Small: 1
- Medium: prefer 1, max 2 without owner approval
- Large: 2–4
- Initiative: 3–6
- >6: owner approval

Waves:
- disabled by default
- never for small/medium
- >2 requires owner approval
- explicit "no waves" always wins

Split by outcome, not DB/API/UI/tests/docs layers.
Prefer vertical slices.

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

## Owner override interaction

If ticket count or wave count requires owner approval, present the smallest viable decompositions as selectable choices.

Example:

```text
Choose one:
A. 1 ticket, 0 waves — recommended
B. 2 vertical-slice tickets, 0 waves
C. 2 tickets, 1 wave
D. Other — specify ticket/wave limits
```

Do not create the higher-count plan until the owner chooses it.
