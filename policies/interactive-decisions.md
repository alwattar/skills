# Interactive Decision Questions

Use this rule whenever the agent needs an owner/user decision.

## Goal

Reduce unnecessary free-form typing while preserving the owner's ability to choose something not anticipated by the agent.

## Preferred interaction mode

When the host/client exposes a real structured choice interaction:

1. Use **single-select** for exactly one choice.
2. Use **multi-select** when several choices may apply.
3. Ensure **Other / Custom** is available when the option space is not exhaustive. If the host supplies it automatically, do not add a duplicate.
4. If the UI supports a free-text value attached to Other/Custom, enable it.
5. If the UI does not support free text inside the choice control, follow the selection with a short prompt asking the user to type the custom value.

Do not pretend a structured picker exists when the host does not expose one.

## Text fallback

When no structured selection UI is available, render the same options in text:

```text
Q1 — Initial acquisition scope (choose one)
A. Visible post and currently loaded content
B. Manual evidence import only
C. Other — describe your scope
Recommendation: A, based on the supplied first-slice brief.
```

For multiple selections, state that multiple answers are allowed and use the project roles or evidence categories. See `.agents/workflow/INTERACTION-EXAMPLES.md`.

## Quality of options

Options MUST be:
- realistic for the specific project/domain;
- meaningfully different from each other;
- mutually exclusive for single-select where practical;
- concise enough to scan quickly;
- based on repository evidence, domain knowledge, or clearly stated reasoning;
- free of fake precision.

Do not generate placeholder options merely to avoid an open-ended question.

Bad:
- A. Simple
- B. Advanced
- C. Other

Better:
- A. One organization on isolated infrastructure
- B. Several organizational tenants requiring isolation
- C. A local investigator workstation
- D. A centrally managed investigative deployment
- E. Other

## Recommendations

For owner decisions:
- provide a recommendation when there is enough context;
- explain the main reason in one or two sentences;
- clearly separate the recommendation from the selectable options;
- do not treat a host-preselected option as a submitted answer or approval.

## Open-ended questions

Use free-form questions when the answer space is genuinely open and forcing options would distort discovery.

Even then, reduce effort where possible with examples or suggested dimensions.

Example:

> What are the three biggest operational problems today?
> Common examples: incomplete captures, evidence traceability, review delays, access control.
> You can answer freely; you are not limited to these examples.

## Frontier discipline

Do not present downstream choices before their prerequisites are settled.

Prefer:
- 2–5 high-value decisions per round;
- one interaction per genuinely independent decision;
- follow-up rounds derived from previous answers.

Avoid dumping 10–20 decisions into one message.

## Other / Custom is mandatory

Whenever predefined options are shown and the set is not logically exhaustive, include:
- `Other`
- `Custom`
- or equivalent wording in the user's conversation language.

The user must always be able to provide an answer outside the proposed options.

## Conversation vs artifact language

Choice prompts should use the user's conversation language.

Repository artifacts produced from those choices remain subject to `.agents/workflow/rules/documentation-language.md`.
