# Documentation Language Policy

## Mandatory rule

All repository documentation and generated engineering artifacts MUST be written in English, regardless of the language used in conversation with the user.

The agent may communicate with the user in Arabic, German, Turkish, or any other language, but that MUST NOT change the language of repository documentation.

## Covered artifacts

This rule applies to, at minimum:

- `README.md`
- `CONTEXT.md`
- `PRODUCT.md`
- `ARCHITECTURE.md`
- `DATA-MODEL.md`
- `SECURITY.md`
- `DECISIONS.md`
- `AGENTS.md`
- specifications
- implementation plans
- tickets / issue bodies generated from specs
- ADRs
- handoff documents
- audit reports stored in the repository
- workflow documentation
- generated engineering notes intended to become repository artifacts

## Conversation language

Conversation language and artifact language are independent.

Example:

- User discusses the project in Arabic.
- Agent replies to the user in Arabic.
- Agent writes `PRODUCT.md`, specs, tickets, ADRs, and handoff documents in English.

Do not translate English repository documentation into the conversation language merely because the user is speaking another language.

## Exceptions

The following are exempt when their purpose explicitly requires another language:

- localization files such as `locales/ar.json`, `de.json`, etc.
- user-facing translated content
- multilingual fixtures/test data
- examples whose purpose is to demonstrate another language
- a separately requested translation artifact

These exceptions do not change the default language of engineering documentation.

## Existing non-English documentation

Do not mass-translate existing documentation automatically.

When touching an existing non-English engineering document:
1. preserve its content unless the current task requires editing it;
2. report the language-policy conflict;
3. propose migration to English when appropriate;
4. require owner approval for broad translation/migration work.

## Enforcement

Before writing or updating a repository artifact, determine whether this policy applies.

If it applies, produce the artifact in English even when:
- the prompt is Arabic,
- the conversation is Arabic,
- the user mixes multiple languages,
- another agent previously replied in a non-English language.

Explicit owner instruction may request a separate translated artifact, but the canonical engineering documentation remains English unless the owner explicitly changes the project-wide policy.
