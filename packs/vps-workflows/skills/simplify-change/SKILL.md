---
name: simplify-change
description: Simplify a changed code path while preserving its behavior.
disable-model-invocation: true
---

# Simplify Change

Inspect the changed scope and tests. Identify duplication or unnecessary branching. Pick the smallest useful simplification. Check inputs, old formats and errors before and after. Leave unrelated edits intact.

## Illustrative request

Two branches normalize the same input differently on empty strings.

## Expected result

Unify only after tests capture both empty and nonempty cases.
