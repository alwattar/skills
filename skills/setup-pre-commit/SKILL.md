---
name: setup-pre-commit
description: Configure safe pre-commit quality checks appropriate to the project ecosystem.
---

# Setup Pre-Commit

Inspect existing hooks, project package manager, scripts, contributor instructions and CI before proposing changes.

1. Identify the language and toolchain rather than assuming Node.js. For JS/TS projects consider Husky, lint-staged or existing tools; for Python consider pre-commit; for other ecosystems use their established hooks.
2. Preserve existing hook behavior and avoid reinitializing or replacing customized configuration.
3. Select only checks that are deterministic, fast enough for commits and already supported by the repository. Keep expensive integration or browser tests in CI unless explicitly requested.
4. Explain required new dependencies and seek approval before installing or changing lockfiles if that action has not been authorized.
5. Add or modify the minimal hook files, respecting cross-platform use, executable permissions and project formatting conventions.
6. Run the actual hook on a disposable/staged example where safe. Record commands, results and any skipped checks.

Never stage, commit or push changes automatically merely because this skill ran. Keep the owner in control of Git actions.

**Output:** documented hook configuration, changed files, observed verification and remaining caveats.
**Next:** `verify` and `handoff`.
