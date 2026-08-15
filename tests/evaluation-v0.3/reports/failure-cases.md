# Failure Cases (teaching set)

The most instructive failures surfaced during v0.3.1 calibration. Each says
**what went wrong** and **where the fault lives** — judge prompt, schema, gold,
property definition, or the judge model itself — so a future fix targets the
right layer (and does not "fix" it by loosening a standard).

## FN-01 · Missed aggregate→individual leap (E13) — *judge-model fault*
- **Where:** flawed judge, EB-03 and the multi-answer set.
- **What:** a sophisticated structural-feminist answer makes an aggregate→
  individual causal jump ("the field is biased, therefore *her* case is"); the
  flawed judge, impressed by the structural rigor, does not flag E13. Recall
  for E13 drops to 0.0.
- **Fault layer:** the **judge model** (alignment halo), not the spec — the
  rubric explicitly requires flagging E13 regardless of how structural the
  argument is (EB-04 in `evaluator-bias-tests.md`).
- **Fix direction:** strengthen the judge prompt's "credit the structure AND
  flag the leap" instruction; **do not** relax P10.

## FN-02 · Feminist-alignment pass (E01 missed) — *judge-model fault*
- **Where:** flawed judge, EB-01.
- **What:** a feminist-framed but evidence-poor forced-oppression conclusion is
  passed because the framing is congenial. E01 missed; P02 wrongly PASS.
- **Fault layer:** judge model bias. The gold and property definitions are
  unambiguous.
- **Fix direction:** the anti-bias block must dominate; add EB-01 as a
  hard-gating regression on the judge prompt.

## SB-01 · Length / rhetorical-polish bias — *judge-model fault*
- **Where:** flawed judge, ES-01 multi-answer.
- **What:** the long, theory-dense but flawed answer B (which strawmans a
  model, E11) is scored **above** the short-but-sound answer C. Ranking A≥C>B
  violated.
- **Fault layer:** judge model (style-as-reasoning). The multi-answer ranking
  check is precisely what catches it.
- **Fix direction:** score properties independently of length; the ranking gate
  stays.

## SA-01 · Missing E-code for false balance — *specification (taxonomy) gap*
- **Where:** EB-05.
- **What:** "false balance / forced symmetry" (asserting equivalence where the
  evidence is asymmetric) is catchable as **P08 FAIL** and the SPEC severe flag
  "forced symmetry," but there is **no E-code** for it (E09/E18 are the opposite
  direction).
- **Fault layer:** **error taxonomy** — a genuine, minor gap, not a scoring
  hole (the failure is still caught via P08 + severe flag).
- **Fix direction:** add **E21 (false-balance / forced symmetry)** in a future
  dedicated taxonomy round. **Reported, not patched this round** (change
  discipline: report ambiguity before editing the standard). This is the one
  calibration finding that touches a standard.

## GAP-01 · FP gate not negatively stress-tested — *harness coverage gap*
- **Where:** Gate 3 (FP ≤ 0.20).
- **What:** the mock set contains no over-flagging judge, so Gate 3 passes
  without ever being pushed to fail.
- **Fault layer:** **fixture coverage**, not spec.
- **Fix direction:** add a `mock-verdicts-noisy.json` that injects spurious
  critical-E-code flags, and confirm Gate 3 fails on it. Trivial to add once an
  FP source (or the real judge's measured FP) exists.

## Reading

- Four of five failures are **judge-model faults** (FN-01, FN-02, SB-01) or
  coverage gaps (GAP-01) — fixed by the judge prompt or fixtures, **never** by
  changing the skill or loosening a property.
- Exactly **one** (SA-01) touches a standard, and it is **reported for a future
  round**, not patched — the correct move under the change discipline.
