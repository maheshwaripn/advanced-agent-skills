---
name: site-publish
description: Prepare or execute a scoped static-site release.
disable-model-invocation: true
---

# Site Publish

Identify the site, known build entry point, current release and restore point from the project's runbook. Build in staging, validate links and assets and compare release contents. Publish only within authorized scope. Verify the served revision and a representative route. Record privileged steps separately if needed.

## Verification table and owner handoff

| Check | Pass condition |
| --- | --- |
| Staging build | Build completes with no errors in a staging folder |
| Links and assets | No broken internal link or missing asset |
| Served revision | The live route reports the expected revision |
| Representative route | One page per template returns its expected content |
| Restore point | The previous release is identified before publishing |

Steps that need privileges (first publish, web-server or system configuration) are written as a numbered script for the site owner. They are never run by the assistant.

## Illustrative request

Preview a course page where the build succeeds but its quiz link returns 404.

## Expected result

Hold the release and identify the broken link and previous restore point.
