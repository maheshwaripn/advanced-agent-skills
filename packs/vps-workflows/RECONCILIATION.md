# VPS evidence reconciliation

Claude Code supplied a read-only inventory follow-up on 21 November 2026. These are operator-reported observations. Repository paths and catalog coverage were checked against Git. Runtime equivalence has not been tested.

| Group | Reported evidence | How to interpret the public skills |
| --- | --- | --- |
| Owner workflows | 13 installed: broker-token diagnostics, quantitative research protocol, site publishing, nine studio stages, and task routing. The VPS report gives an installed SKILL.md blob prefix for all 13. Each differs from its public blob at d179066 (see the pinned table below). | Treat these as portable editions. A different blob establishes a file difference only. The source comparison and direction of changes remain open. |
| Studio and routing | Nine studio skills are installed and listed. An earlier count of eight was wrong. The installed router also has SETUP.md, EVALUATION.md and a claude-code directory. | Studio formats, costs and QC tolerances, plus router worker contracts, await sanitized evidence. |
| Vendor and plugin entries | Fifteen distinct names in the sync manifest. Its dates are update dates. Only google-workspace appeared in the latest harness listing. A listing or manifest entry is not evidence of successful invocation. Availability of the two plugin-backed skills was unchecked. | Public entries are independent workflows. Manifest dates are not version numbers or compatibility guarantees. |
| Documents | docs (anthropic-skills:docs) is the editable shared-document skill and docx is the Word-file skill. The Docs connector tool family (mcp__claude_ai_Claude_Docs__*) is separate from the docs skill, per the V2 listing. The separately invocable Docs skill ID remains unconfirmed. | Keep document-drafting, word-document and docs-connector-edit distinct as public tasks. Do not infer an installed implementation for the unconfirmed ID. |
| Browser and desktop | The claude-in-chrome skill and the mcp__claude-in-chrome__* tools are separate, per V2. The built-in browser and Chrome adapter use separate namespaces. Computer use addresses a desktop. The VPS has no display or browser, so no invocation was observed. | Test interactions on a suitable host. Listing a skill does not show that it works. |
| Charts | dataviz is listed in the harness and was not found as an owner-installed file (V2 and V3). The harness-bundled copy is the source of any ninth-series rule. | The public workflow is available. The pack ships no palette validator and no series-count threshold. A project-supplied chart validator is optional. Without one, check contrast manually: labels, a table alternative and text values can be verified by hand. |
| Other host commands | Earlier inventory listings are the evidence for host commands not reconciled to owner files or vendor manifest entries. | Check host discovery and permissions before attempting these workflows. |

No private sources, vendor prompt text, credentials or production configuration were supplied. Pinned blob pairs are recorded below. The pack's input/output examples and failure checks are illustrative and not exercised, except where a section says otherwise. No live broker calls, deployments, renders or sealed research data are required.

## Pinned blob evidence

Public blob prefixes were read from commit `d179066189aeeb2b4961e071cdbb9c267f34aad4`. Installed prefixes are operator-reported values from the VPS inventory, not checked against this repository. Every pair differs, so each difference is a file difference only.

| Owner workflow | Public SKILL.md blob (d179066) | Operator-reported installed blob |
| --- | --- | --- |
| dhan-token-triage | eac90cc33c7b | 99ce2d057305 |
| quant-research-protocol | b1a21afc6be4 | 199bbca1ad11 |
| site-publish | a2697a9cc980 | a59e7ce0e3a6 |
| studio-assemble-qc | b27f5c1cec82 | 19830d07ee21 |
| studio-audio | e934908e30cb | 96b09ab73041 |
| studio-budget | ac235356b20a | 8c01b06d76b9 |
| studio-consistency | 5f81773a0351 | cd16c9b4c31b |
| studio-render | 33bb509e5713 | a51da56b907d |
| studio-screenplay | 7b3b6aaa4395 | 76227aa209a5 |
| studio-shotlist | 3d3a2dbcaef5 | 02ee62266a01 |
| studio-showrunner | 873d1fe3194c | 7d0aa20a84a3 |
| studio-story-bible | 683b2507fa6c | 06a74ed006f6 |
| task-router | deb6a8faae44 | 93507726162d |

## Scope of the comparison

The reconciliation compared frontmatter descriptions, invocation flags and file lengths. It did not compare full bodies. The public patch adds behaviour descriptions in original wording, and its examples are illustrative unless marked as exercised.

