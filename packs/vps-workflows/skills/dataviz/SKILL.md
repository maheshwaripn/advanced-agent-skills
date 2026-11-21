---
name: dataviz
description: Design and verify a chart for a specific comparison.
disable-model-invocation: true
---

# Dataviz

Identify data grain, units, denominator, missing values and intended question. Choose marks and scales that answer it. Specify accessible labels, non-color cues and a table alternative. Check palette contrast with the project's validator if available. Keep essential values accessible without hover.

## Validator and scope

Use the project's own palette validator when one exists. This pack ships no validator and no series-count threshold. Any series limit belongs to the project's own style rules.

Illustrative example: group A has 10 events out of 40 (25%) and group B has 120 out of 400 (30%). The plotted rates must read 25% and 30%, the table must show 10/40 and 120/400, and the text alternative must state both rates and denominators.

## Illustrative request

Compare error rates for groups of very different sizes.

## Expected result

A labeled rate chart includes denominators and a readable data table.
