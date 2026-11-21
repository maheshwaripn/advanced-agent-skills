---
name: studio-showrunner
description: Coordinate studio stages from premise to delivery.
disable-model-invocation: true
---

# Studio Showrunner

Inventory available inputs and approvals. Track bible, screenplay, shot list, budget, render, audio, continuity and final QC by revision and owner. Advance only stages with satisfied dependencies. Report the next executable stage and blocker.

## Stage order and continuity gates

Stage order: story bible, screenplay, shot list, budget, pre-render continuity check, bulk render, post-render continuity pass, audio, assembly and QC. A stage starts only when its dependencies are satisfied.

- Pre-render continuity check: runs on the approved shot list before any paid render. Paid rendering needs both an approved budget and a passed pre-render check.
- Post-render continuity pass: runs on the rendered shots before audio sign-off and assembly. A failure sends only the affected shots back for a targeted re-render.
- Audio planning may start once the shot list is approved. Audio mixing waits for the post-render pass. Assembly and QC wait for both audio and the post-render pass.

Illustrative walkthrough: the budget is approved with a 20-credit cap and the shot list S01 to S03 is approved. The pre-render check passes, so bulk render runs. The post-render pass finds a radio colour mismatch in S03 only. S03 is re-rendered within the cap, the pass succeeds, and then audio mixing and assembly run.

## Illustrative request

The shot list is approved but the render quote is missing.

## Expected result

Continue audio planning while marking paid rendering blocked by the unknown cost.
