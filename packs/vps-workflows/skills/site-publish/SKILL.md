---
name: site-publish
description: Prepare or execute a scoped static-site release.
disable-model-invocation: true
---

# Site Publish

Identify the site, known build entry point, current release and restore point from the project's runbook. Build in staging, validate links and assets and compare release contents. Publish only within authorized scope. Verify the served revision and a representative route. Record privileged steps separately if needed.

## Illustrative request

Preview a course page where the build succeeds but its quiz link returns 404.

## Expected result

Hold the release and identify the broken link and previous restore point.
