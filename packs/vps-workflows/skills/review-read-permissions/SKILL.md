---
name: review-read-permissions
description: Review recurring prompts for narrowly scoped read-only operations.
disable-model-invocation: true
---

# Review Read Permissions

Use redacted examples to group repeated reads. Inspect the host's rule semantics, including arguments, redirection and command composition. Exclude writes, secret reads, broad shell and network access. Propose narrow rules for owner review and test a permitted read and a prohibited write.

## Illustrative request

A status command prompts repeatedly.

## Expected result

Recommend only the verified read form and show why a write still requires approval.
