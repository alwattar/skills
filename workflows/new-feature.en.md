# NEW_FEATURE

**Workflow:** `new-feature` · **Risk profile:** `standard`

This guide explains the registered sequence; executable routing is owned only by [registry/registry.yaml](../registry/registry.yaml). The canonical route notes are in [workflows/new-feature.md](./new-feature.md).

## When to use

Select this route only when it is the smallest authorized match. `high` risk routes require explicit decisions for material changes. Optional skills run only when their named registry conditions apply.

## Steps

1. [`grill`](../skills/grill/README.en.md) — required
2. [`domain-modeling`](../skills/domain-modeling/README.en.md) — optional if `domain-modeling` conditions apply
3. [`feature-design`](../skills/feature-design/README.en.md) — required
4. [`architecture-decision`](../skills/architecture-decision/README.en.md) — optional if `architecture-decision` conditions apply
5. [`review-design`](../skills/review-design/README.en.md) — optional if `review-design` conditions apply
6. [`resolve-findings`](../skills/resolve-findings/README.en.md) — optional if `resolve-findings` conditions apply
7. [`doc-impact`](../skills/doc-impact/README.en.md) — required
8. [`to-spec`](../skills/to-spec/README.en.md) — required
9. [`to-tickets`](../skills/to-tickets/README.en.md) — optional if `to-tickets` conditions apply
10. [`implement`](../skills/implement/README.en.md) — required
11. [`security-audit`](../skills/security-audit/README.en.md) — optional if `security-audit` conditions apply
12. [`accessibility-audit`](../skills/accessibility-audit/README.en.md) — optional if `accessibility-audit` conditions apply
13. [`performance-audit`](../skills/performance-audit/README.en.md) — optional if `performance-audit` conditions apply
14. [`verify`](../skills/verify/README.en.md) — required
15. [`code-review`](../skills/code-review/README.en.md) — required
16. [`detect-drift`](../skills/detect-drift/README.en.md) — optional if `detect-drift` conditions apply
17. [`decision-capture`](../skills/decision-capture/README.en.md) — optional if `decision-capture` conditions apply
18. [`doc-sync`](../skills/doc-sync/README.en.md) — required
19. [`handoff`](../skills/handoff/README.en.md) — required

## Completion

Report verified artifacts, tests or observations, unresolved blockers, owner approvals and recommended follow-up. No external publishing, spending or deployment without authorization.
