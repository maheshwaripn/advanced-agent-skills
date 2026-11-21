---
name: task-router
description: Choose direct work, a model recommendation or bounded delegation.
disable-model-invocation: true
---

# Task Router

Assess ambiguity, dependencies, verification cost and reversibility. Keep small deterministic work local. Split only independent tasks with clear evidence contracts. Map roles to available capabilities; verify documentary claims against their sources and execution claims against actual run evidence. Record any fallback to sequential work.

## Routing criteria and worker evidence

Route on four inputs: ambiguity, verification need, tooling available and the evidence quality the answer needs. Give a worker only independent, read-only work with a stated output contract.

The parent checks each claim by its type before applying or reporting it:

- **Documentary facts** (a setting, a rule, a figure): verify against the cited source. A fact with a valid source is accepted without a test run.
- **Execution claims** (a test passed, a build succeeded): accept only with actual run evidence, such as the command and its output. A check that was not performed stays unverified.

An unperformed check is recorded as unverified and is never reported as passed.

Illustrative examples (exercised offline against a synthetic fixture):
- Accepted: a worker cites the line of a configuration file that sets a default timeout. The parent reads that line, confirms the value, and accepts the claim.
- Rejected: a worker reports that the test suite passes but gives no run output. The parent finds no run evidence, records the claim as unverified, and leaves the change unapplied.

## Illustrative request

Two read-only workers can inspect docs but cannot run tests.

## Expected result

Assign independent document checks, then give the parent the test and final decision.
