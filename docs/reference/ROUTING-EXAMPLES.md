# Routing Examples

| Request | Route |
|---|---|
| Bootstrap agent workflow only | NEW_PROJECT, stop at the authorized bootstrap boundary |
| Audit documentation against implementation | PROJECT_AUDIT |
| Add a capture viewer filter | NEW_FEATURE |
| Capture viewer fails on absent media | BUGFIX |
| Restructure parser with identical output | REFACTOR |
| Choose evidence storage transaction design | ARCHITECTURE_CHANGE |
| Change case authorization or snapshot sanitization | SECURITY_CHANGE |
| Correct glossary wording | DOCS_ONLY |
| Implement the already approved capture spec | IMPLEMENT_APPROVED_SPEC, after checking approval and security impact |
| Review this diff | REVIEW_ONLY |
| Plan the acquisition/fusion/analysis program | LARGE_INITIATIVE |
| Reverse-engineer an undocumented existing deployment | LEGACY_ONBOARDING |

Security impact overrides routine feature/fix/refactor classification. Explicit skill invocation narrows the requested action without bypassing gates.
An explicit ticket limit such as "maximum two tickets, no waves" overrides default sizing.
