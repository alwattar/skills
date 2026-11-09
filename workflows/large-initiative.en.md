# LARGE_INITIATIVE

**Workflow:** `large-initiative` · **Risk profile:** `high`

This guide explains the registered sequence; executable routing is owned only by [registry/registry.yaml](../registry/registry.yaml). The canonical route notes are in [workflows/large-initiative.md](./large-initiative.md).

## When to use

Select this route only when it is the smallest authorized match. `high` risk routes require explicit decisions for material changes. Optional skills run only when their named registry conditions apply.

## Steps

1. [`project-discovery`](../skills/project-discovery/README.en.md) — optional if `project-discovery` conditions apply
2. [`grill`](../skills/grill/README.en.md) — required
3. [`map-initiative`](../skills/map-initiative/README.en.md) — required
4. [`domain-modeling`](../skills/domain-modeling/README.en.md) — optional if `domain-modeling` conditions apply
5. [`feature-design`](../skills/feature-design/README.en.md) — required
6. [`architecture-decision`](../skills/architecture-decision/README.en.md) — optional if `architecture-decision` conditions apply
7. [`review-design`](../skills/review-design/README.en.md) — optional if `review-design` conditions apply
8. [`resolve-findings`](../skills/resolve-findings/README.en.md) — optional if `resolve-findings` conditions apply
9. [`doc-impact`](../skills/doc-impact/README.en.md) — required
10. [`to-spec`](../skills/to-spec/README.en.md) — required
11. [`to-tickets`](../skills/to-tickets/README.en.md) — required
12. [`implement`](../skills/implement/README.en.md) — required
13. [`security-audit`](../skills/security-audit/README.en.md) — optional if `security-audit` conditions apply
14. [`accessibility-audit`](../skills/accessibility-audit/README.en.md) — optional if `accessibility-audit` conditions apply
15. [`performance-audit`](../skills/performance-audit/README.en.md) — optional if `performance-audit` conditions apply
16. [`verify`](../skills/verify/README.en.md) — required
17. [`code-review`](../skills/code-review/README.en.md) — required
18. [`detect-drift`](../skills/detect-drift/README.en.md) — optional if `detect-drift` conditions apply
19. [`decision-capture`](../skills/decision-capture/README.en.md) — optional if `decision-capture` conditions apply
20. [`doc-sync`](../skills/doc-sync/README.en.md) — required
21. [`handoff`](../skills/handoff/README.en.md) — required

## Completion

Report verified artifacts, tests or observations, unresolved blockers, owner approvals and recommended follow-up. No external publishing, spending or deployment without authorization.
