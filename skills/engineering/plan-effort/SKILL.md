---
name: plan-effort
description: Choose a workflow and reasoning budget for a task using its uncertainty, impact and verification cost. Use when the user asks how to route or split work.
disable-model-invocation: true
---

# Plan effort

Read the request and the closest available evidence (a failing check, diff, spec or sample). State the outcome and one observable acceptance check. If a missing decision changes the expected result, ask for it. Otherwise record the assumption and proceed with planning.

Select the first applicable tier:

| Condition | Effort | First move |
| --- | --- | --- |
| Irreversible data change, broad operational impact or conflicting requirements | High | Identify failure modes, the decision owner and a recovery test. Resolve conflicting requirements before implementation. |
| Cause unknown, multiple components affected or verification requires integration | Medium | Start with one discriminating test. Use diagnosing-bugs for a regression or to-spec for an agreed multi-session change. |
| Local, reversible and directly verifiable | Light | Use one focused edit and one direct check. |

Separate independent work only when each part has its own input, output and acceptance check. Group edits to the same contract under one owner. List dependencies in order. Use the available model and tools. Model switching and delegation require host support and authorization. When either is absent, work sequentially. For deterministic transformations prefer a local script. Open only the selected skill and the evidence it needs.

Return a short table of work item, dependency, tier, chosen workflow and acceptance evidence. Give one escalation trigger and one stopping condition. Planning ends at the recommendation unless execution was requested.

Example: a quiz label is wrong on one lesson. If a single renderer owns the label, choose light and check the rendered lesson. If search and course totals each compute it separately, choose medium, trace the shared rule, and check all three surfaces.
