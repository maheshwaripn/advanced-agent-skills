---
name: studio-budget
description: Estimate production spend and enforce an agreed cap.
disable-model-invocation: true
---

# Studio Budget

Collect quoted units, currency, quantities, retries and cap. Separate committed spend from forecasts. Calculate the remaining allowance before approving more work. Treat missing prices as unknown. Never purchase a render from an estimate alone.

## Spend approval and tracking

- Each paid batch needs a recorded approval that names the cap, the quoted units and the approver. Render does not start without it.
- Keep a running ledger of committed spend, charged failed attempts and remaining allowance. Recalculate after every batch.

## Illustrative request

Cap 20 credits, 12 committed, next batch costs 10.

## Expected result

Flag a 2-credit overrun and propose a smaller batch within the remaining 8.
