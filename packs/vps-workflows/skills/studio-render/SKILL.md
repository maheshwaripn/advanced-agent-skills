---
name: studio-render
description: Prepare and track a reproducible render batch.
disable-model-invocation: true
---

# Studio Render

Read approved shot IDs, reference assets, output specs, provider availability and budget. Build a per-shot manifest recording prompts, settings and seeds when supported. Check an inexpensive sample before a batch. Reuse accepted shots and record failed attempts against the cap.

## Retake log

- Record each retake with shot ID, reason, attempt number and cost.
- Keep accepted outputs. A retake adds a new output; it never overwrites an accepted one.

## Illustrative request

S02 passed but S03 has a mismatched prop.

## Expected result

Queue only S03 for a permitted retry and keep the accepted S02 asset.
