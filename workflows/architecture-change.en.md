# ARCHITECTURE_CHANGE

**Workflow:** `architecture-change` · **Risk profile:** `high`

This guide explains the registered sequence; executable routing is owned only by [registry/registry.yaml](../registry/registry.yaml). The canonical route notes are in [workflows/architecture-change.md](./architecture-change.md).

## When to use

Select this route only when it is the smallest authorized match. `high` risk routes require explicit decisions for material changes. Optional skills run only when their named registry conditions apply.

## Steps

1. [`grill`](../skills/grill/README.en.md) — required
2. [`architecture-decision`](../skills/architecture-decision/README.en.md) — required
3. [`threat-model`](../skills/threat-model/README.en.md) — optional if `threat-model` conditions apply
4. [`review-design`](../skills/review-design/README.en.md) — optional if `review-design` conditions apply
5. [`resolve-findings`](../skills/resolve-findings/README.en.md) — optional if `resolve-findings` conditions apply
6. [`doc-impact`](../skills/doc-impact/README.en.md) — required
7. [`to-spec`](../skills/to-spec/README.en.md) — required
8. [`to-tickets`](../skills/to-tickets/README.en.md) — optional if `to-tickets` conditions apply
9. [`implement`](../skills/implement/README.en.md) — required
10. [`security-audit`](../skills/security-audit/README.en.md) — optional if `security-audit` conditions apply
11. [`accessibility-audit`](../skills/accessibility-audit/README.en.md) — optional if `accessibility-audit` conditions apply
12. [`performance-audit`](../skills/performance-audit/README.en.md) — optional if `performance-audit` conditions apply
13. [`verify`](../skills/verify/README.en.md) — required
14. [`code-review`](../skills/code-review/README.en.md) — required
15. [`detect-drift`](../skills/detect-drift/README.en.md) — optional if `detect-drift` conditions apply
16. [`decision-capture`](../skills/decision-capture/README.en.md) — required
17. [`doc-sync`](../skills/doc-sync/README.en.md) — required
18. [`handoff`](../skills/handoff/README.en.md) — required

## Completion

Report verified artifacts, tests or observations, unresolved blockers, owner approvals and recommended follow-up. No external publishing, spending or deployment without authorization.
