---
name: defensive-review
description: Review a pending change for defensive security issues.
disable-model-invocation: true
---

# Defensive Review

Map changed trust boundaries, authorization decisions, input validation and secret handling. Review source and existing tests. Report evidence, affected surface and remediation; verify fixes through safe regression checks. Keep findings free of credentials.

## Illustrative request

A new export handler lacks the project’s access check.

## Expected result

Point to the missing guard and require a test confirming unauthorized requests are rejected.
