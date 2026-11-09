---
name: detect-drift
description: Compare approved specifications with implemented code and verified behavior.
---
# Detect Drift

**Use when:** a feature has shipped, implementation changed after design approval, or a periodic reconciliation is requested.

1. Locate current approved specifications, ADRs, documented invariants, relevant implementation and tests.
2. Map each material assertion to code paths, tests or observed behavior; identify missing evidence.
3. Categorize differences: VERIFIED DRIFT, POSSIBLE DRIFT, APPROVED CHANGE, UNVERIFIED.
4. Note severity, user impact, ownership and suggested remediation without automatically rewriting specs to match buggy code.
5. The owner selects a code fix, a documentation change or deferral.

**Output:** traceable drift report, evidence, unknowns and a clear remediation recommendation.
**Next:** `doc-sync`, `diagnose-bug` or `architecture-decision`.
