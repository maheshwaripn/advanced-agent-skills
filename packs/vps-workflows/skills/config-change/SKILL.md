---
name: config-change
description: Change one scoped agent configuration setting.
disable-model-invocation: true
---

# Config Change

Identify the active host, supported schema and precedence. Inspect only the relevant non-secret setting. Prepare a minimal reversible edit, validate syntax and verify the effective value in the correct scope. Never echo environment secrets.

## Illustrative request

Enable a formatting hook for one project.

## Expected result

A scoped diff and one sample run demonstrate the hook fires once.
