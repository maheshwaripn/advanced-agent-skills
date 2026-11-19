---
name: evaluate-skill
description: Compare two skill or prompt revisions on paired cases and report regressions, reliability and cost.
disable-model-invocation: true
---

# Evaluate Skill

Record the decision the trial must support, baseline and candidate revisions, model, tool permissions, effort and run budget. Include routine, ambiguous and failure cases. Freeze case IDs, inputs, expected evidence, grading rules and unacceptable failures before running. Reserve unseen cases for confirmation.

Use a fresh session for each attempt. Present only the task and its inputs. Keep expected answers out of the task context. Pair each baseline run with a candidate run under the same settings. Alternate order when possible. Prefer executable checks for objective properties. For judgment calls, blind the reviewer to revision, record disagreements and resolve them using the rubric. Keep tool failures and timeouts visible.

Record case, repeat, revision, verdict, elapsed time and measured tokens if available. The bundled scripts/score.py summarizes paired binary outcomes from CSV. Inspect individual regressions even when the total improves. Report missing trials separately. Compare cost only for equivalent coverage and account for failed attempts.

Decide adopt, revise, or insufficient evidence against the predeclared threshold. A fixture passing the scorer only verifies arithmetic. Never turn simulated responses into model-performance claims.

**Acceptance example.** The candidate wins two routine tasks but leaks expected answers on a held-out case. Reject that comparison, repair isolation and rerun both arms.
