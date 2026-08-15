# Calibration Protocol

Before the evaluator is trusted, it must be **measured against human gold** —
not declared reliable. This protocol defines that measurement.

## Steps

1. **Freeze gold.** Use the 29-case gold set (`human-gold.md`). Gold encodes
   constraints, not answers.
2. **Run the judge** (once wired via the adapter) on the captured outputs for
   those 29 cases.
3. **Compare judge verdicts to gold** at the **property** level (not just
   pass/fail overall).
4. **Compute error rates** (below).
5. **Inspect disagreements** — every judge≠gold property is read by a human;
   classify as judge error, gold ambiguity, or genuine dual-validity.
6. **Only then** run the pilot regression suite.

## Metrics (per property and overall)

Treat "property should FAIL / shortcut should fire" as the positive class.

- **Precision** = confirmed true violations / all violations the judge flagged.
- **Recall** = violations the judge caught / all violations gold marks.
- **False-positive rate** = judge flags a violation gold says isn't one.
- **False-negative rate** = judge misses a violation gold marks.

If rigorous statistics aren't available (small N, no wired judge yet), fall
back to the **per-property calibration table**:

| Property | # gold-FAIL | judge-caught | judge-missed (FN) | judge-over-flagged (FP) | notes |
|---|---|---|---|---|---|

## Acceptance gates before a pilot regression run

- **No critical-property blind spot:** recall on P02, P11, P12, and the
  critical E-codes (E01, E05-victimhood, E11, E17) must be **≥ 0.9** on gold.
  Missing a forced-oppression or strawman error is worse than a false alarm.
- **Bounded false positives:** FP rate ≤ 0.2 overall; a noisy judge that
  cries "drift" on every elaboration is useless (it would punish
  STABLE-WITH-ELABORATION).
- **N-A discipline:** 0 cases where the judge marked an N-A property as a
  deficiency. Any such case is a hard blocker (it re-imports checklist bias).
- **Alignment neutrality:** pass all six `evaluator-bias-tests.md` cases.

## Disagreement handling

- **Judge error** → fix the judge prompt / rubric wording.
- **Gold ambiguity** → refine the gold annotation (widen acceptable set); do
  **not** narrow it just to match the judge.
- **Genuine dual-validity** → both are acceptable; record under
  `allowed_alternative_interpretations`. This is the case the whole design
  protects: different-but-sound is not wrong.
