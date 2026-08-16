# Ablation Report (v0.4)

**Design complete and deterministically verified. Live sweep execution-pending
under nested-CLI rate limits — NO ablation deltas are fabricated.**

## Infrastructure (verified, no model calls)
`../../tests/research-protocol/harness/ablate.py` generates single-module-
removed variants A1–A7. Verified: each variant drops **exactly one** `## `
section (21→20), all other modules byte-identical, and **SKILL.md is never
modified**. Variants: A1 Null Result · A2 Baseline · A3 Responsibility ·
A4 Intersectionality · A5 Comparison · A6 Parallel Analysis · A7 Class/Position.

## Live evidence captured this round
| Condition | Case | Result |
|---|---|---|
| **baseline (full skill)** | NR-01 | captured (1397 chars): keeps null result, separates pattern≠instance, **no forced oppression** — the A1 reference behavior |
| **ablate-A1 (Null Result removed)** | NR-01 | **NOT captured** — rate-limited (0/≥3 attempts). Delta **pending**, not fabricated. |
| A2–A7 sweeps | — | execution-pending (rate limit) |

The captured baseline confirms the *full* skill fires Null Result correctly on
an evidence-thin case; the ablated counterfactual (does removal → forced
oppression?) is exactly the measurement that is pending.

## Predicted causal contributions (HYPOTHESES, not results)
Grounded in the architecture; to be tested when the sweep runs. **Not measured.**
| Ablation | Predicted primary effect | Test cases |
|---|---|---|
| A1 Null Result | forced-oppression (E01) on evidence-thin cases | NR-01, RWB-23 |
| A2 Baseline | accepts "向下的自由" uninterrogated (E10) | DF-01…05 |
| A3 Responsibility | victimhood/structure→exemption (E05) | RWB-14/24/26 |
| A4 Intersectionality | homogenized "women" (E06) | RWB-13/16, AS-01 |
| A5 Comparison | auto-whataboutism / false balance (E08/E18) | RWB-20/22/27 |
| A6 Parallel Analysis | framing lock; choice→freedom or structure→no-agency | FO-01…05 |
| A7 Class/Position | single-axis power collapse (E29→E19) | AS-01/03/06 |

**Module interaction** (e.g. does removing A6 also degrade A3's responsibility
reading?) is measurable with the same harness once runs complete — not asserted
here.

## Status
Ablation **infrastructure READY**; ablation **results execution-pending**
(rate-limited). No causal-contribution or redundancy claim is made from data
this round — only the reference baseline datapoint and testable hypotheses.
