# Advanced Agent Skills

Advanced Agent Skills is Prashant Maheshwari’s public collection of 85 skill definitions: 33 core workflows, 40 optional VPS workflows, 8 experimental skills and 4 reference tools. Start with `/askadvisor` to find a skill, or run `/setup-agent-skills` to configure a project’s issue tracker, triage labels, and documentation. [Maintainer’s website](https://pusaram.com/)

## Optional VPS workflow pack

The [illustrated VPS catalog](packs/vps-workflows/README.md) maps 42 inventory entries to 40 companion skills and two existing core skills. It includes operations, research, film production, scheduling, documents and host-specific workflows. Install the companion separately when needed.

## Use from this checkout

On Linux, link the promoted skills into your chosen agent directory. Existing same-name entries are preserved and reported. Keep this checkout in place while using the links.

```bash
python3 scripts/check.py
bash scripts/link-skills.sh ~/.agents/skills
# For Claude Code use ~/.claude/skills as the destination instead.
```

For a local Claude marketplace install, run `claude plugin marketplace add .` from this checkout, followed by `claude plugin install advanced-agent-skills@maheshwaripn`. Choose one installation method per host.

Try: “Use plan-effort to route a change that adds a field to our invoice export. A consumer still reads the old format.” Then, on the candidate revision, ask: “Use release-evidence to check that old and new consumers can both read the export.”

See [the upstream review](REVIEW.md) for the baseline, changes and attribution. [Run the scenarios](EVALUATION.md) to evaluate a specific model.

## Reference

User-invoked skills start when you request them. Model-invoked skills can also be selected by the agent when a task fits.

### Engineering

Engineering workflows.

**User-invoked**

- [draft-release-notes](./skills/engineering/draft-release-notes/SKILL.md) — Write audience-facing release notes from a verified comparison between two revisions.
- [evaluate-skill](./skills/engineering/evaluate-skill/SKILL.md) — Compare two skill or prompt revisions on paired cases and report regressions, reliability and cost.
- [review-ui-journey](./skills/engineering/review-ui-journey/SKILL.md) — Evaluate a real user journey across interface states, keyboard navigation and responsive layouts.
- [trace-architecture](./skills/engineering/trace-architecture/SKILL.md) — Trace one behavior across a codebase with revision-specific evidence and an explicit map of unknowns.
- [plan-effort](./skills/engineering/plan-effort/SKILL.md) selects an effort level and verification path.
- [release-evidence](./skills/engineering/release-evidence/SKILL.md) checks a release candidate and its recovery evidence.

- **[askadvisor](./skills/engineering/askadvisor/SKILL.md)**: Ask which skill or flow fits your situation. A router over the user-invoked skills in this repo.
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)**: Grilling session that also builds your project's domain model, sharpening terminology and updating `GLOSSARY.md` and ADRs inline.
- **[triage](./skills/engineering/triage/SKILL.md)**: Move issues through a state machine of triage roles.
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)**: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- **[setup-agent-skills](./skills/engineering/setup-agent-skills/SKILL.md)**: Configure this repo for the engineering skills (issue tracker, triage labels, domain doc layout). Run once per repo before using the other engineering skills.
- **[to-spec](./skills/engineering/to-spec/SKILL.md)**: Turn the current conversation into a spec and publish it to the issue tracker. No interview, just synthesizes what you've already discussed.
- **[to-tickets](./skills/engineering/to-tickets/SKILL.md)**: Break any plan, spec, or conversation into a set of tracer-bullet tickets, each declaring its blocking edges, written as text in a local file, or as native blocking links on a real tracker.
- **[implement](./skills/engineering/implement/SKILL.md)**: Build the work described by a spec or set of tickets, driving `/tdd` at pre-agreed seams and closing out with `/code-review` before committing.
- **[implement-spec](./skills/engineering/implement-spec/SKILL.md)**: Implement a whole spec on one integration branch. Works the tickets as a task graph, running implementer subagents across the ready frontier for maximum concurrency, then closes out with `/code-review`.
- **[wayfinder](./skills/engineering/wayfinder/SKILL.md)**: Plan a huge chunk of work, more than one agent session can hold, as a shared map of decision tickets on the issue tracker, and resolve them one at a time until the way to the destination is clear.
- **[retro](./skills/engineering/retro/SKILL.md)**: Suggest improvements to the coding agent's environment (navigation, automated checks, coding standards, steering files, tooling) after a session, most severe first.

**Model-invoked**

- **[prototype](./skills/engineering/prototype/SKILL.md)**: Build a throwaway prototype to answer a design question, either a single shareable HTML file for state/logic questions, or several radically different UI variations toggleable from one route.
- **[diagnosing-bugs](./skills/engineering/diagnosing-bugs/SKILL.md)**: Disciplined diagnosis loop for hard bugs and performance regressions: build a feedback loop that goes red on this bug → minimise → hypothesise → instrument → fix → regression-test.
- **[research](./skills/engineering/research/SKILL.md)**: Investigate a question against high-trust primary sources and capture the findings as a cited Markdown file in the repo, run as a background agent.
- **[tdd](./skills/engineering/tdd/SKILL.md)**: Test-driven development with a red-green-refactor loop. Builds features or fixes bugs one vertical slice at a time.
- **[domain-modeling](./skills/engineering/domain-modeling/SKILL.md)**: Actively build and sharpen a project's domain model: challenge terms against the glossary, stress-test with edge-case scenarios, and update `GLOSSARY.md` and ADRs inline.
- **[codebase-design](./skills/engineering/codebase-design/SKILL.md)**: Shared discipline and vocabulary for designing deep modules: a lot of behaviour behind a small interface, placed at a clean seam, testable through that interface.
- **[code-review](./skills/engineering/code-review/SKILL.md)**: Two-axis review of the diff since a fixed point: **Standards** (does it follow the repo's coding standards, plus a Fowler smell baseline?) and **Spec** (does it faithfully implement the originating issue/spec?), run as parallel sub-agents so neither pollutes the other.
- **[pr](./skills/engineering/pr/SKILL.md)**: The shape a pull request body should take: a summary as the smallest visual that makes the change clear, before/after evidence that it works, and a merge-danger call (one-way or two-way door, plus blast radius).
- **[wizard](./skills/engineering/wizard/SKILL.md)**: Generate an interactive bash wizard that walks a human through steps only they can perform: provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or running a one-off migration or cutover.

### Productivity

General workflow tools, not code-specific.

**User-invoked**

- **[grill-me](./skills/productivity/grill-me/SKILL.md)**: Get relentlessly interviewed about a plan or design until every branch of the design tree is resolved.
- **[handoff](./skills/productivity/handoff/SKILL.md)**: Compact the current conversation into a handoff document so another agent can continue the work.
- **[teach](./skills/productivity/teach/SKILL.md)**: Teach the user a new skill or concept over multiple sessions, using the current directory as a stateful teaching workspace.
- **[to-questionnaire](./skills/productivity/to-questionnaire/SKILL.md)**: Turn a decision you can't answer alone into a Markdown questionnaire for the one person who can, filled in async, or together over a meeting. It grills you about the send (who it's for, what you need back), not the subject.
- **[wait-what](./skills/productivity/wait-what/SKILL.md)**: Fire this the moment a message doesn't land. The agent re-pitches it with the context you're missing, in plain English, using your `GLOSSARY.md` vocabulary.

**Model-invoked**

- **[grilling](./skills/productivity/grilling/SKILL.md)**: Interview the user relentlessly about a plan, decision, or idea until every branch of the design tree is resolved. The reusable interview primitive behind `grill-me`, `grill-with-docs`, `triage`, `wayfinder` and `improve-codebase-architecture`.
- **[writing-for-agents](./skills/productivity/writing-for-agents/SKILL.md)**: Writing documents for agents: skills, AGENTS.md/CLAUDE.md, and any doc an agent reaches by a pointer.

[External skill review and selection decisions](docs/catalog-review.md)

## Optional VPS skills

Install the companion with `claude plugin install vps-workflows@maheshwaripn` after registering the local marketplace. Examples are illustrative. Source status and host requirements are recorded in the [VPS reconciliation](packs/vps-workflows/RECONCILIATION.md).

| Area | Skill | When to use it | Example or acceptance check |
| --- | --- | --- | --- |
| Workspace | [workspace-edit](packs/vps-workflows/skills/workspace-edit/SKILL.md) | Change a native Google Workspace file through an authorized connector. | The same spreadsheet ID now contains the renamed tab and its original formulas. |
| Operations | [dhan-token-triage](packs/vps-workflows/skills/dhan-token-triage/SKILL.md) | Diagnose an authentication alert using redacted status evidence. | Show the missed run, distinguish suspected expiry from confirmed failure, and name the next read-only check. |
| Research | [quant-research-protocol](packs/vps-workflows/skills/quant-research-protocol/SKILL.md) | Evaluate a pre-registered trading hypothesis. | Report the failed gate and retain the sealed sample. |
| Operations | [site-publish](packs/vps-workflows/skills/site-publish/SKILL.md) | Prepare or execute a scoped static-site release. | Hold the release and identify the broken link and previous restore point. |
| Studio | [studio-story-bible](packs/vps-workflows/skills/studio-story-bible/SKILL.md) | Establish the narrative and visual canon for a production. | Create a character and prop sheet that fixes the radio color and marks its repair state per scene. |
| Studio | [studio-screenplay](packs/vps-workflows/skills/studio-screenplay/SKILL.md) | Turn an approved premise into filmable scenes. | A timed scene reaches the repair payoff without dialogue in the final beat. |
| Studio | [studio-shotlist](packs/vps-workflows/skills/studio-shotlist/SKILL.md) | Plan camera coverage before rendering. | Two or more numbered shots add to twelve seconds and preserve the hand holding the radio. |
| Studio | [studio-budget](packs/vps-workflows/skills/studio-budget/SKILL.md) | Estimate production spend and enforce an agreed cap. | Flag a 2-credit overrun and propose a smaller batch within the remaining 8. |
| Studio | [studio-render](packs/vps-workflows/skills/studio-render/SKILL.md) | Prepare and track a reproducible render batch. | Queue only S03 for a permitted retry and keep the accepted S02 asset. |
| Studio | [studio-audio](packs/vps-workflows/skills/studio-audio/SKILL.md) | Plan and verify a soundtrack against picture timing. | Move or attenuate the cue, then verify the line and peak level on the new mix. |
| Studio | [studio-consistency](packs/vps-workflows/skills/studio-consistency/SKILL.md) | Review continuity across adjacent shots. | Record both shot IDs and the conflicting frames, then request a targeted correction. |
| Studio | [studio-assemble-qc](packs/vps-workflows/skills/studio-assemble-qc/SKILL.md) | Assemble accepted media and check delivery quality. | Identify the affected time range and require playback of the corrected export. |
| Studio | [studio-showrunner](packs/vps-workflows/skills/studio-showrunner/SKILL.md) | Coordinate studio stages from premise to delivery. | Continue audio planning while marking paid rendering blocked by the unknown cost. |
| Workflow | [task-router](packs/vps-workflows/skills/task-router/SKILL.md) | Choose direct work, a model recommendation or bounded delegation. | Assign independent document checks, then give the parent the test and final decision. |
| Design | [dataviz](packs/vps-workflows/skills/dataviz/SKILL.md) | Design and verify a chart for a specific comparison. | A labeled rate chart includes denominators and a readable data table. |
| Claude host | [config-change](packs/vps-workflows/skills/config-change/SKILL.md) | Change one scoped agent configuration setting. | A scoped diff and one sample run demonstrate the hook fires once. |
| Claude host | [keyboard-shortcuts](packs/vps-workflows/skills/keyboard-shortcuts/SKILL.md) | Resolve or customize a keyboard shortcut. | Show the conflict and confirm both actions in their intended contexts. |
| Engineering | [simplify-change](packs/vps-workflows/skills/simplify-change/SKILL.md) | Simplify a changed code path while preserving its behavior. | Unify only after tests capture both empty and nonempty cases. |
| Claude host | [review-read-permissions](packs/vps-workflows/skills/review-read-permissions/SKILL.md) | Review recurring prompts for narrowly scoped read-only operations. | Recommend only the verified read form and show why a write still requires approval. |
| Scheduling | [bounded-loop](packs/vps-workflows/skills/bounded-loop/SKILL.md) | Repeat an observable check within an active session. | Stop on a terminal result and report attempt count and last observed state. |
| Scheduling | [scheduled-routine](packs/vps-workflows/skills/scheduled-routine/SKILL.md) | Set up a persistent future task when the host supports it. | One stored schedule has the correct time zone, next run and cancellation identifier. |
| Engineering | [api-integration](packs/vps-workflows/skills/api-integration/SKILL.md) | Plan or update a Claude API integration. | A minimal example uses the verified SDK interface and handles an unavailable model. |
| Browser | [chrome-session](packs/vps-workflows/skills/chrome-session/SKILL.md) | Perform a bounded task in an authorized Chrome session. | Report the visible review state and stop before order submission. |
| Browser | [chrome-journey](packs/vps-workflows/skills/chrome-journey/SKILL.md) | Inspect a journey using a Chrome browser adapter. | Confirm whether the opened menu exposes the target item and keyboard focus. |
| Browser | [embedded-browser](packs/vps-workflows/skills/embedded-browser/SKILL.md) | Use an embedded browser for a scoped site task. | Report the opened lesson heading or the reason the preview could not load. |
| Browser | [desktop-journey](packs/vps-workflows/skills/desktop-journey/SKILL.md) | Verify a native desktop workflow through its UI. | Record the page count shown by the app or mark preview unavailable. |
| Planning | [ai-workflow-design](packs/vps-workflows/skills/ai-workflow-design/SKILL.md) | Design an AI-assisted workflow with evidence of success. | Deliver a routing design and a labeled pilot set with an escalation condition. |
| Research | [quant-study-design](packs/vps-workflows/skills/quant-study-design/SKILL.md) | Design a reproducible quantitative study. | Record all trials and require independent confirmation before crediting the apparent advantage. |
| Documents | [document-drafting](packs/vps-workflows/skills/document-drafting/SKILL.md) | Draft a structured document for a defined audience. | Include options, decision owner, rationale and unresolved evidence. |
| Documents | [word-document](packs/vps-workflows/skills/word-document/SKILL.md) | Create or edit a Word document with layout checks. | The DOCX reopens, headings are structured and the table fits the page. |
| Knowledge | [context-import](packs/vps-workflows/skills/context-import/SKILL.md) | Import selected context with provenance. | Keep both dated claims until the authoritative revision is identified. |
| Workflow | [morning-brief](packs/vps-workflows/skills/morning-brief/SKILL.md) | Prepare a dated morning brief from authorized sources. | List verified work items and identify the calendar coverage gap. |
| Documents | [pdf-document](packs/vps-workflows/skills/pdf-document/SKILL.md) | Produce or inspect a PDF against delivery requirements. | Report the affected page and distinguish clipping observed in rendering from a suspected issue. |
| Documents | [slide-deck](packs/vps-workflows/skills/slide-deck/SKILL.md) | Build a presentation around an audience decision. | A short deck shows the decision, trend and supporting evidence with readable labels. |
| Engineering | [author-skill](packs/vps-workflows/skills/author-skill/SKILL.md) | Author a portable agent skill with an acceptance example. | A mismatch is reported and a file with no comparable totals yields insufficient evidence. |
| Documents | [spreadsheet-workbook](packs/vps-workflows/skills/spreadsheet-workbook/SKILL.md) | Build or audit a spreadsheet with reproducible calculations. | Changing an input updates totals and missing capacity never produces a misleading percentage. |
| Documents | [docs-connector-edit](packs/vps-workflows/skills/docs-connector-edit/SKILL.md) | Edit an existing Google Doc using its connector. | The intended section changes while the other occurrence is preserved. |
| Claude host | [project-instructions](packs/vps-workflows/skills/project-instructions/SKILL.md) | Initialize project guidance from observed repository conventions. | Instructions reference the actual entry point and test command and preserve existing local guidance. |
| Engineering | [defensive-review](packs/vps-workflows/skills/defensive-review/SKILL.md) | Review a pending change for defensive security issues. | Point to the missing guard and require a test confirming unauthorized requests are rejected. |
| Engineering | [plugin-authoring](packs/vps-workflows/skills/plugin-authoring/SKILL.md) | Package skills into a host-compatible plugin. | Validation identifies the path and a corrected install discovers both commands. |

## Experimental skills

Available for evaluation as individual skills. Their interfaces may change.

- [chief-of-staff](skills/in-progress/chief-of-staff/SKILL.md) — Pursue a long-running goal in a single session by co-ordinating subagents.
- [claude-handoff](skills/in-progress/claude-handoff/SKILL.md) — Hand the current conversation off to a fresh background agent that picks up the work immediately.
- [loop-me](skills/in-progress/loop-me/SKILL.md) — Grill me about specs for the workflows I want to build, within this workspace.
- [setup-ts-deep-modules](skills/in-progress/setup-ts-deep-modules/SKILL.md) — Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through its entry-point files. User-invoked.
- [software-factory](skills/in-progress/software-factory/SKILL.md) — Shared language for designing a software factory: the tasks it runs and the services it plugs into.
- [writing-beats](skills/in-progress/writing-beats/SKILL.md) — Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it.
- [writing-fragments](skills/in-progress/writing-fragments/SKILL.md) — Writing, explore: mine raw fragments, no structure yet.
- [writing-shape](skills/in-progress/writing-shape/SKILL.md) — Writing, exploit: shape raw material into an article, paragraph by paragraph.

## Reference tools

Special-purpose workflows available in the source tree.

- [git-guardrails-claude-code](skills/misc/git-guardrails-claude-code/SKILL.md) — Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code.
- [migrate-to-shoehorn](skills/misc/migrate-to-shoehorn/SKILL.md) — Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data.
- [scaffold-exercises](skills/misc/scaffold-exercises/SKILL.md) — Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise stubs, or set up a new course section.
- [setup-pre-commit](skills/misc/setup-pre-commit/SKILL.md) — Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/typechecking/testing.
