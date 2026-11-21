---
name: quant-research-protocol
description: Evaluate a pre-registered trading hypothesis.
disable-model-invocation: true
---

# Quant Research Protocol

Freeze universe, timing, costs, splits, sizing assumptions and rejection criteria. Check point-in-time inputs and leakage, then run walk-forward and cost stress on development data. Keep the sealed period closed until explicit in-session owner authorization. Record disappointing results as well as passes. Passing gates permits a paper-trial proposal only.

## Gates and cost sensitivity

- Pre-register the gates before reading results: net edge, drawdown, trade count and stability. State the rejection rule with them.
- Stress the simulated result at 1x, 2x and 3x the assumed costs. The edge must still pass at 2x. Report 3x as a sensitivity figure, not a pass condition.
- The sealed period stays closed unless the owner authorises it in the current session. One authorisation covers one strategy and one opening.
- Passing every gate permits a paper-trial proposal only. It never permits an order.

## Illustrative request

A simulated signal loses its advantage after doubled costs.

## Expected result

Report the failed gate and retain the sealed sample.
