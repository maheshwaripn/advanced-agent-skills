---
name: review-ui-journey
description: Evaluate a real user journey across interface states, keyboard navigation and responsive layouts.
disable-model-invocation: true
---

# Review UI Journey

Pick a named user, starting state, goal and observable success condition. Identify the design system and existing components. Trace one complete journey first. Sample the relevant states: initial, loading, empty, populated, error, retry and completion. Record which states were reachable.

Exercise the primary path at desktop and narrow widths. Use keyboard-only input for navigation, submit and recovery. Observe focus visibility, focus return after dialogs, labels, feedback and whether an error preserves the user's work. Compare the same task across widths; a screenshot alone cannot demonstrate keyboard behavior. If runtime access is unavailable, mark findings as static observations and list the missing interaction tests.

Report defects in task order with reproduction, impact, evidence, smallest remediation and a repeatable acceptance check. Choose component tests for local interaction and a browser journey for integration. Make clear which checks actually ran. Keep visual preferences separate from failures that block users.

**Acceptance example.** A form works on desktop but a sticky footer covers Retry on mobile. Record viewport, failed state and keyboard reachability. Verify successful recovery with the original field values after the fix.
