# Upstream review

Reviewed mattpocock/skills at [5863806](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa). The original MIT notice is in LICENSE. This downstream edition retains Git ancestry, the 27 promoted workflows, their supporting files and their invocation names. Historical documentation and experimental skills reflect their original authors and are outside the promoted catalog.

| Observation in that revision | Decision in this edition |
| --- | --- |
| ask-matt maps discovery, specs, tickets and implementation. tdd and diagnosing-bugs already specify feedback loops. | Reuse these workflows. Add an effort and evidence decision before selecting a workflow. |
| code-review checks standards and spec coverage. pr records blast radius. Neither establishes that a release candidate has a runnable recovery path. | Add a release evidence review with explicit hold conditions and an owner for outstanding checks. |
| scripts/link-skills.sh removes an existing same-name directory and includes beta skills. | Replace it with a promoted-only, preflighted installer that preserves conflicts. |
| Distribution metadata and release automation target the original maintainer. | Give the derivative its own plugin identity and a read-only CI job. |
| The plugin catalog is enumerated by hand. | Check promoted paths, names, human docs and invocation flags together. |

For an upstream refresh, fetch the upstream main branch, compare the skill files and reference documents with the pinned revision, port selected changes, run the checks and record the new baseline here. Any model quality or token saving claim needs a measured trial on the same tasks and model settings.
