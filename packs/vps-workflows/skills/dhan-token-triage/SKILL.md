---
name: dhan-token-triage
description: Diagnose an authentication alert using redacted status evidence.
disable-model-invocation: true
---

# Dhan Token Triage

Collect timestamps, redacted response classifications, renewal job exit status and clock information. Separate expiration, missed renewal, connectivity and inconclusive evidence. Never print tokens or environment values. Present a recovery check using the project’s existing read-only health procedure.

## Illustrative request

A synthetic WARN follows a missed overnight job.

## Expected result

Show the missed run, distinguish suspected expiry from confirmed failure, and name the next read-only check.
