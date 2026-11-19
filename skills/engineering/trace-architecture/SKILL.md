---
name: trace-architecture
description: Trace one behavior across a codebase with revision-specific evidence and an explicit map of unknowns.
disable-model-invocation: true
---

# Trace Architecture

Start with one question, entry point, end condition and revision. For example, trace an export request until a worker writes the file. Search locally for registrations, callers, message names and storage operations. Follow one path before widening the map.

For each edge record source, destination, action, evidence path and symbol, and confidence. Distinguish declared wiring, observed execution and inference. An import proves availability, not invocation. For queues, verify the producer, routing key, consumer binding and handler separately. Mark missing bindings and runtime configuration as unknown.

If a local Graphify index or Archify map already exists, use it to find candidates. Verify its revision and confirm material edges against code or traces. A stale graph is a search aid. Neither tool is required. Inspect only the files needed for the requested path.

Deliver a compact Mermaid diagram or a table, plus an evidence ledger and the smallest next check for each unresolved edge. Mark inferred edges visibly in the diagram. Give the traced revision and distinguish current implementation from proposed design.

**Acceptance example.** A handler and producer share a payload type, but the subscription is configured elsewhere. Show the observed components and flag the missing subscription. Do not draw a confirmed delivery edge.
