---
name: doc-impact
description: Predict permanent doc impact before implementation.
---

# Documentation Impact
Classify README/CONTEXT/PRODUCT/ARCHITECTURE/DATA-MODEL/SECURITY/DECISIONS/AGENTS as update/no-change.
Prediction only: do not document planned behavior as shipped.

## Documentation language

Before creating or updating any repository engineering artifact, follow `.agents/workflow/rules/documentation-language.md`.

Keep canonical documentation, specs, tickets, ADRs, plans, audits, and handoffs in English even when the conversation with the user is in another language.

Do not apply this rule to localization files or explicitly requested translation artifacts.
