# SECURITY_CHANGE

**Workflow:** `security-change` · **Risk profile:** `high`

This guide explains the registered sequence; executable routing is owned only by [registry/registry.yaml](../registry/registry.yaml). The canonical route notes are in [workflows/security-change.md](./security-change.md).

## When to use

Select this route only when it is the smallest authorized match. `high` risk routes require explicit decisions for material changes. Optional skills run only when their named registry conditions apply.

## Steps

1. [`grill`](../skills/grill/README.en.md) — required
2. [`architecture-decision`](../skills/architecture-decision/README.en.md) — optional if `architecture-decision` conditions apply
3. [`threat-model`](../skills/threat-model/README.en.md) — required
4. [`privacy-review`](../skills/privacy-review/README.en.md) — optional if `privacy-review` conditions apply
5. [`secrets-safety`](../skills/secrets-safety/README.en.md) — optional if `secrets-safety` conditions apply
6. [`review-design`](../skills/review-design/README.en.md) — optional if `review-design` conditions apply
7. [`resolve-findings`](../skills/resolve-findings/README.en.md) — optional if `resolve-findings` conditions apply
8. [`doc-impact`](../skills/doc-impact/README.en.md) — required
9. [`to-spec`](../skills/to-spec/README.en.md) — required
10. [`implement`](../skills/implement/README.en.md) — required
11. [`security-audit`](../skills/security-audit/README.en.md) — required
12. [`verify`](../skills/verify/README.en.md) — required
13. [`code-review`](../skills/code-review/README.en.md) — required
14. [`decision-capture`](../skills/decision-capture/README.en.md) — optional if `decision-capture` conditions apply
15. [`doc-sync`](../skills/doc-sync/README.en.md) — required
16. [`handoff`](../skills/handoff/README.en.md) — required

## Completion

Report verified artifacts, tests or observations, unresolved blockers, owner approvals and recommended follow-up. No external publishing, spending or deployment without authorization.
