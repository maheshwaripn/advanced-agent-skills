---
name: scheduled-routine
description: Set up a persistent future task when the host supports it.
disable-model-invocation: true
---

# Scheduled Routine

Resolve time zone, recurrence, destination, overlap and duplicate policy. Inspect current schedules before creation. Use an authorized scheduler, read back the stored schedule and record cancellation and next run. Distinguish registration from actual execution.

## Illustrative request

Run a weekly report Mondays at 09:00 IST.

## Expected result

One stored schedule has the correct time zone, next run and cancellation identifier.
