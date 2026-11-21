---
name: bounded-loop
description: Repeat an observable check within an active session.
disable-model-invocation: true
---

# Bounded Loop

Define the condition, interval, deadline, maximum attempts, cancellation and stop state. Make repeated reads idempotent and back off on transient failures. Verify completion using the observed target revision or value.

## Illustrative request

Check a build every minute for at most ten attempts.

## Expected result

Stop on a terminal result and report attempt count and last observed state.
