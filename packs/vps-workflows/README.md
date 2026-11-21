# Claude Code VPS workflow inventory

This companion to Advanced Agent Skills covers the 21 November 2026 inventory. Each example is synthetic. The public workflows were written from descriptions. They are independent implementations and do not include vendor prompts, VPS configuration, private paths, credentials or provider integrations. Claude's follow-up identified 13 locally installed owner skills with different file revisions and 15 distinct vendor or plugin entries in the sync manifest. Only Google Workspace appeared in the latest session listing. A manifest entry indicates presence on disk; it does not establish successful invocation. [Read the source reconciliation](RECONCILIATION.md).

## Installation

From a checkout of the repository, register the local marketplace with `claude plugin marketplace add .`, then install `vps-workflows@maheshwaripn` with `claude plugin install`. The two reused skills belong to the core `advanced-agent-skills@maheshwaripn` plugin. Use the command name shown by your host (including its plugin namespace when required). Each packaged workflow is explicitly user-invoked. A skill provides instructions; its host must supply the required tools and authorization.

## Illustrated catalog

| Area | VPS inventory name | Public workflow | Example request | Expected result |
| --- | --- | --- | --- | --- |
| Workspace | `anthropic-skills:google-workspace` | [workspace-edit](skills/workspace-edit/SKILL.md) | Rename the January tab in a sample budget to Q1 inputs. | The same spreadsheet ID now contains the renamed tab and its original formulas. |
| Operations | `dhan-token-triage` | [dhan-token-triage](skills/dhan-token-triage/SKILL.md) | A synthetic WARN follows a missed overnight job. | Show the missed run, distinguish suspected expiry from confirmed failure, and name the next read-only check. |
| Research | `quant-research-protocol` | [quant-research-protocol](skills/quant-research-protocol/SKILL.md) | A simulated signal loses its advantage after doubled costs. | Report the failed gate and retain the sealed sample. |
| Operations | `site-publish` | [site-publish](skills/site-publish/SKILL.md) | Preview a course page where the build succeeds but its quiz link returns 404. | Hold the release and identify the broken link and previous restore point. |
| Studio | `studio-story-bible` | [studio-story-bible](skills/studio-story-bible/SKILL.md) | A child repairs a blue radio across three scenes. | Create a character and prop sheet that fixes the radio color and marks its repair state per scene. |
| Studio | `studio-screenplay` | [studio-screenplay](skills/studio-screenplay/SKILL.md) | Write a 30-second radio repair scene with a silent ending. | A timed scene reaches the repair payoff without dialogue in the final beat. |
| Studio | `studio-shotlist` | [studio-shotlist](skills/studio-shotlist/SKILL.md) | Cover a radio repair and a reaction in twelve seconds. | Two or more numbered shots add to twelve seconds and preserve the hand holding the radio. |
| Studio | `studio-budget` | [studio-budget](skills/studio-budget/SKILL.md) | Cap 20 credits, 12 committed, next batch costs 10. | Flag a 2-credit overrun and propose a smaller batch within the remaining 8. |
| Studio | `studio-render` | [studio-render](skills/studio-render/SKILL.md) | S02 passed but S03 has a mismatched prop. | Queue only S03 for a permitted retry and keep the accepted S02 asset. |
| Studio | `studio-audio` | [studio-audio](skills/studio-audio/SKILL.md) | A chime masks a spoken line near second eight. | Move or attenuate the cue, then verify the line and peak level on the new mix. |
| Studio | `studio-consistency` | [studio-consistency](skills/studio-consistency/SKILL.md) | A repaired radio changes color at the cut. | Record both shot IDs and the conflicting frames, then request a targeted correction. |
| Studio | `studio-assemble-qc` | [studio-assemble-qc](skills/studio-assemble-qc/SKILL.md) | A 30-second cut loses its last caption on export. | Identify the affected time range and require playback of the corrected export. |
| Studio | `studio-showrunner` | [studio-showrunner](skills/studio-showrunner/SKILL.md) | The shot list is approved but the render quote is missing. | Continue audio planning while marking paid rendering blocked by the unknown cost. |
| Workflow | `task-router` | [task-router](skills/task-router/SKILL.md) | Two read-only workers can inspect docs but cannot run tests. | Assign independent document checks, then give the parent the test and final decision. |
| Design | `dataviz` | [dataviz](skills/dataviz/SKILL.md) | Compare error rates for groups of very different sizes. | A labeled rate chart includes denominators and a readable data table. |
| Claude host | `update-config` | [config-change](skills/config-change/SKILL.md) | Enable a formatting hook for one project. | A scoped diff and one sample run demonstrate the hook fires once. |
| Claude host | `keybindings-help` | [keyboard-shortcuts](skills/keyboard-shortcuts/SKILL.md) | An editor shortcut shadows a terminal action. | Show the conflict and confirm both actions in their intended contexts. |
| Engineering | `code-review` | [code-review (core)](../../skills/engineering/code-review/SKILL.md) | A patch updates the UI label but leaves the export unchanged. | A finding cites the missed public surface and a regression check. |
| Engineering | `simplify` | [simplify-change](skills/simplify-change/SKILL.md) | Two branches normalize the same input differently on empty strings. | Unify only after tests capture both empty and nonempty cases. |
| Claude host | `fewer-permission-prompts` | [review-read-permissions](skills/review-read-permissions/SKILL.md) | A status command prompts repeatedly. | Recommend only the verified read form and show why a write still requires approval. |
| Scheduling | `loop` | [bounded-loop](skills/bounded-loop/SKILL.md) | Check a build every minute for at most ten attempts. | Stop on a terminal result and report attempt count and last observed state. |
| Scheduling | `schedule` | [scheduled-routine](skills/scheduled-routine/SKILL.md) | Run a weekly report Mondays at 09:00 IST. | One stored schedule has the correct time zone, next run and cancellation identifier. |
| Engineering | `claude-api` | [api-integration](skills/api-integration/SKILL.md) | Migrate a sample text request to a supported model. | A minimal example uses the verified SDK interface and handles an unavailable model. |
| Browser | `claude-in-chrome` | [chrome-session](skills/chrome-session/SKILL.md) | Check that a sample checkout shows a review step. | Report the visible review state and stop before order submission. |
| Browser | `anthropic-skills:chrome-browser` | [chrome-journey](skills/chrome-journey/SKILL.md) | Inspect a sample menu at mobile width. | Confirm whether the opened menu exposes the target item and keyboard focus. |
| Browser | `anthropic-skills:built-in-browser` | [embedded-browser](skills/embedded-browser/SKILL.md) | Check a lesson link in an embedded preview. | Report the opened lesson heading or the reason the preview could not load. |
| Browser | `anthropic-skills:computer-use` | [desktop-journey](skills/desktop-journey/SKILL.md) | Check print preview in a sample desktop document. | Record the page count shown by the app or mark preview unavailable. |
| Planning | `anthropic-skills:ai-architect-mastery-system` | [ai-workflow-design](skills/ai-workflow-design/SKILL.md) | Route incoming support requests to two teams. | Deliver a routing design and a labeled pilot set with an escalation condition. |
| Research | `anthropic-skills:apex-quant` | [quant-study-design](skills/quant-study-design/SKILL.md) | An indicator was selected after trying twenty settings. | Record all trials and require independent confirmation before crediting the apparent advantage. |
| Research | `anthropic-skills:deep-research` | [research (core)](../../skills/engineering/research/SKILL.md) | Two versions of a specification disagree. | A cited finding identifies which version governs the example and lists uncertainty. |
| Documents | `anthropic-skills:docs` | [document-drafting](skills/document-drafting/SKILL.md) | Draft a one-page project decision brief. | Include options, decision owner, rationale and unresolved evidence. |
| Documents | `anthropic-skills:docx` | [word-document](skills/word-document/SKILL.md) | Create a two-page SOP with a revision table. | The DOCX reopens, headings are structured and the table fits the page. |
| Knowledge | `anthropic-skills:import-memory` | [context-import](skills/context-import/SKILL.md) | Two notes disagree about the current release. | Keep both dated claims until the authoritative revision is identified. |
| Workflow | `anthropic-skills:morning` | [morning-brief](skills/morning-brief/SKILL.md) | Prepare a brief when the calendar is unavailable. | List verified work items and identify the calendar coverage gap. |
| Documents | `anthropic-skills:pdf` | [pdf-document](skills/pdf-document/SKILL.md) | Check a report whose wide table approaches the page edge. | Report the affected page and distinguish clipping observed in rendering from a suspected issue. |
| Documents | `anthropic-skills:pptx` | [slide-deck](skills/slide-deck/SKILL.md) | Turn three status tables into an executive update. | A short deck shows the decision, trend and supporting evidence with readable labels. |
| Engineering | `anthropic-skills:skill-creator` | [author-skill](skills/author-skill/SKILL.md) | Create a skill for reconciling report totals. | A mismatch is reported and a file with no comparable totals yields insufficient evidence. |
| Documents | `anthropic-skills:xlsx` | [spreadsheet-workbook](skills/spreadsheet-workbook/SKILL.md) | Build a sample monthly utilization workbook. | Changing an input updates totals and missing capacity never produces a misleading percentage. |
| Documents | `docs connector skill (exact ID unconfirmed)` | [docs-connector-edit](skills/docs-connector-edit/SKILL.md) | Update one heading that appears twice in a sample document. | The intended section changes while the other occurrence is preserved. |
| Claude host | `init` | [project-instructions](skills/project-instructions/SKILL.md) | Initialize guidance for a Python CLI with an existing README. | Instructions reference the actual entry point and test command and preserve existing local guidance. |
| Engineering | `security-review` | [defensive-review](skills/defensive-review/SKILL.md) | A new export handler lacks the project’s access check. | Point to the missing guard and require a test confirming unauthorized requests are rejected. |
| Engineering | `plugin-authoring` | [plugin-authoring](skills/plugin-authoring/SKILL.md) | Package two sample skills where one manifest path is stale. | Validation identifies the path and a corrected install discovers both commands. |

## Tool availability

Shell and file access, monitoring, delegation, web retrieval, document connectors, charting, communications and broker tools were reported separately in the inventory. Tool access varies by host. Read-only workers cannot certify tests they could not run. A headless session can prepare browser checks but cannot claim to have observed desktop playback.
