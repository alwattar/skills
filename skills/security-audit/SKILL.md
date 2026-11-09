---
name: security-audit
description: Evidence-based security audit and prevention in software projects.
---

# Security Audit

Use on security reviews or security-related tickets. Determine scope, assets, trust boundaries, threat actors and approved testing permissions. Inspect authentication/authorization, BOLA/IDOR, tenancy isolation, input/output handling, XSS/CSRF/SSRF, upload and deserialization risks, session lifecycle, cryptography, secrets, logging and CI/CD surfaces. Prioritize exploitable evidence; separate confirmed findings from hypothetical risks. Never attack third-party systems or production without explicit authorization. For each finding give impact, prerequisite, exact code path, safe reproduction, fix, tests and remaining risk. Invoke threat-model for material architecture changes, secrets-safety for secret handling, privacy-review for personal data, dependency-audit for dependency risk.

## Review output
List evidence, severity, affected boundary, verification and explicit open decisions. Obey project authorization and registered workflows.
