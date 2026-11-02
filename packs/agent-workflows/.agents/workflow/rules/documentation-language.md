# Documentation Language Policy

## Precedence
Follow the consuming project's explicit approved documentation-language policy in AGENTS.md or workflow.config.yaml. If unspecified, write agent-authored canonical engineering documents in English. The conversation language does not silently change repository policy.

## Verbatim external material
Pasted Jira, Linear, GitHub or other original ticket text is an imported SOURCE, not an agent-authored document. Preserve its wording and language verbatim in tickets/KEY.md. Put agent analysis, status and implementation notes in separate sections using the project's documentation language.

## Coverage
Policy covers generated specs, ADRs, plans, handoffs, reviews and agent-authored ticket updates. Localization files, marketing content, examples and translations use their expressly required language.

## Existing repositories
Do not bulk-translate historical documents or erase conflicting text. Surface material conflicts to the owner. When the owner changes the project policy, record it and apply it prospectively, preserving original source material.

## Verification
Before writing: identify project language policy and whether the material is authored or imported verbatim.
