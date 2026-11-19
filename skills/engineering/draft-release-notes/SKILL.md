---
name: draft-release-notes
description: Write audience-facing release notes from a verified comparison between two revisions.
disable-model-invocation: true
---

# Draft Release Notes

Ask for the audience and release endpoints only if they cannot be established from the request or release metadata. Resolve both refs to commits. For Git releases, check ancestry and inspect the endpoint diff and intervening history. If histories diverged, explain the comparison and confirm the intended baseline before attributing changes.

Group surviving user-visible behavior by feature or user action. Trace each statement to a changed entry point, test, or documented contract. A commit subject is a lead. Squashes, reverts, flags and partial rollouts can change what users actually receive. Separate availability by platform or flag when evidenced. Keep internal refactors out unless they change an observable outcome.

Deliver a draft with highlights, breaking changes, migration steps and known limitations where applicable. Attach evidence for the maintainer outside the reader-facing copy. Distinguish merged, released and deployed using the evidence available. Never publish merely because a draft was requested.

**Acceptance example.** A comparison adds CSV export and reverts it before the candidate, renames a CLI flag, and changes a private helper. Cover the flag with a verified replacement invocation. Omit CSV export and the private refactor.
