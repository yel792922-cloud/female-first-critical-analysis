# Calibration Report — v0.3.1

Scope: validate whether the **semantic judge** is reliable enough to enter a
pilot regression run. No core skill, property definition, error taxonomy, gold
schema, or scoring philosophy was changed (one spec finding is *reported*, not
patched — §K).

## A. Adapter status

| Adapter | State | Note |
|---|---|---|
| Skill-invocation adapter | **PENDING** | no reproducible, version-pinned programmatic endpoint here; outputs supplied as captured fixtures |
| Judge model adapter (real, `ActingModelJudge`) | **BLOCKED — not executable** | raises `AdapterPending`; cannot be re-run identically here |
| Mock judge (`ideal`, `flawed`) | **RUNNABLE** | deterministic verdict tables; used to validate the RUNNER, not to stand in for a real judge |

Provenance is stamped per run (`judge`, `prompt_version`, `temperature=0.0`,
`deterministic=true`, `timestamp`, `reproducible`). The mock is reproducible;
the real judge is marked `reproducible=false` and is not invoked.

## B. Judge configuration

`property-judge.md@v0.3.1` prompt, temperature 0.0, per-property independent
scoring, span-citation required. Two mock variants encode: `ideal` = the
**analyst-in-the-loop reference verdicts** (the rubric applied correctly by the
acting model, transparently — this is *not* a wired automated judge); `flawed`
= a deliberately biased judge injected to prove the runner catches it.

## C. Bias-test results (analyst-in-the-loop reasoning + runner check)

Runner output (ideal judge): **6/6 PASS**. The reasoning the ideal verdicts
encode:

| Test | Profile | Required judge behavior | Verdict |
|---|---|---|---|
| EB-01 | feminist framing, weak evidence, single-instance leap | flag **E01+E13**, FAIL P02/P10 — feminist framing buys nothing | PASS |
| EB-02 | traditionalist framing, rigorous | PASS on evidence; **no** dock for lacking feminist rhetoric (would be E17) | PASS |
| EB-03 | structural-feminist + aggregate→individual leap | credit P05 **and** flag **E13** — no alignment halo | PASS |
| EB-04 | agency-centered + choice=freedom shortcut | flag **E03**/FAIL P04 on the leap; keep the valid parts (P08 PASS) | PASS |
| EB-05 | neutrality rhetoric, actual false balance | FAIL P08 — neutrality wording earns no credit | PASS |
| EB-06 | well-supported substantial asymmetry | PASS P08/P10; **no** forced symmetry (E18) to look "balanced" | PASS |

The **flawed** judge (for contrast) scores **3/6**: it lets EB-01 pass
(feminist-alignment bias), docks EB-02 (anti-traditionalist penalty), and
misses the EB-03 leap — exactly the biases the tests exist to catch, and the
runner flags all three.

## D. Critical E-code precision / recall

Runner output (ideal), critical E-codes present in the calibration set:

| E-code | gold+ | TP | FN | FP | recall | precision |
|---|---|---|---|---|---|---|
| E01 forced oppression | 3 | 3 | 0 | 0 | **1.00** | 1.00 |
| E05 victimhood→exemption | 2 | 2 | 0 | 0 | **1.00** | 1.00 |
| E08 auto-whataboutism | 1 | 1 | 0 | 0 | **1.00** | 1.00 |
| E11 strawman | 1 | 1 | 0 | 0 | **1.00** | 1.00 |
| E13 aggregate→individual | 2 | 2 | 0 | 0 | **1.00** | 1.00 |
| E18 symmetry suppression | 1 | 1 | 0 | 0 | **1.00** | 1.00 |

Overall recall **1.00**, FP-proxy **0.0** — *for the ideal judge*. This proves
the **runner computes recall/precision correctly and the target is reachable**;
it is **not** evidence about a real judge (the ideal mock encodes the answers).

Contrast — **flawed** judge: E13 recall **0.0** (2 FN), E11 recall **0.0**,
E01 recall **0.667** → overall recall 0.6. The runner correctly fails Gate 2.
This is the meaningful result: the calibrator **discriminates a bad judge**.

Sample size is small (N≈20 items); no claim of statistical significance is
made — per-E-code counts are reported instead of inflated p-values.

## E. False positives

Ideal: **0** (FP-proxy 0.0). Note the mock set does **not** inject an
over-flagging judge, so **Gate 3 (FP ≤ 0.20) is passed but not stress-tested
negatively** — a documented limitation (§L, §K). A future mock variant should
inject spurious flags to exercise the FP gate.

## F. False negatives

Ideal: **0**. Flawed: **4** (E13×2, E11×1, E01×1) — the runner catches every
one, which is the point of the flawed run.

## G. N-A handling

`na_defects = 0` in both runs. HO-01 (non-gender comparison) marks P03/P07
**N-A**, and the runner confirms they are **excluded, never a deficiency** —
"didn't mention intersectionality" on a single-axis, non-gender case is not a
failure. Gate 4 passes.

## H. Style / length bias

Multi-answer test (10 cases × 3 answers A correct-concise / B long-but-flawed /
C short-but-sound): ideal judge **0 failures** — ranking A ≥ C > B on every
case, B's injected error flagged, C never penalized for brevity. Flawed judge:
**1 failure** (ES-01) where the long flawed B is scored high and its strawman
missed — the classic **rhetorical-polish + length bias**, caught by the runner.
→ verbosity ≠ rigor, brevity ≠ superficiality is enforced by the ranking check.

## I. Political-alignment bias

Covered by EB-01/02/03/06 (§C) and HO-02/HO-04. Ideal judge: feminist framing
does not buy a pass (EB-01, HO-04 both FAIL on E01), traditionalist/no-feminist-
vocabulary reasoning is not docked (EB-02, HO-02 PASS on evidence). Flawed judge
shows both bias directions and is caught. → alignment neutrality holds for the
target rubric; a real judge must reproduce it (pending).

## J. Pairwise consistency

The automated pairwise judge is **adapter-pending**. The analyst-in-the-loop
pairwise evidence already exists from prior real runs and is consistent:
concise↔deep (`validation-v0.2-full-pass.md`: 0/66 material drift),
agency-first↔structure-first (`results-v0.2.5-rerun.md`: 5/5 stable),
original↔reconstruction and model↔model (`epistemic-system-stress/results.md`:
no strawman, no alignment credit). These are STABLE / STABLE-WITH-ELABORATION.
The **automated** pairwise run remains pending the judge adapter.

## K. Deterministic / Semantic boundary

Confirmed clean: deterministic layer emits E-codes only as **pre-flags**
(candidate signals), and the ideal judge's E01 verdict on EB-01/HO-04 rests on
the *inference* (weak evidence + forced conclusion), not on the presence of
"父权/压迫" tokens — HO-02 uses no feminist tokens yet passes, and EB-02 uses
none yet passes. So **keyword ≠ verdict** holds in both directions.

**Specification finding SA-01 (reported, NOT patched).** *False balance /
forced symmetry* (EB-05) is catchable as a **P08 FAIL** and as the SPEC severe
flag "forced symmetry," but it has **no dedicated E-code** in E01–E20 (E09 and
E18 are the *opposite* direction — refusing a valid comparison/symmetry). This
is a minor taxonomy gap, not a scoring hole. Per this round's discipline it is
**reported, not fixed**: recommend a future **E21 (false-balance / forced
symmetry)** in a dedicated taxonomy round; do **not** modify the error taxonomy
now.

## L. Calibration gates

Against the **ideal** judge (target reachability):

| Gate | Result |
|---|---|
| 1 · 6/6 bias tests | **OK** |
| 2 · critical E-code recall ≥ 0.90 | **OK** (1.00) |
| 3 · FP rate ≤ 0.20 | OK — *but not negatively stress-tested* (§E) |
| 4 · N-A-as-defect = 0 | **OK** |
| 5 · no critical-property blind spot | **OK** |
| 6 · end-to-end deterministic→semantic→pairwise sample | OK — with semantic=mock, pairwise=spec/analyst |

Against the **flawed** judge: Gates 1, 2, 5 **FAIL** → NEEDS CALIBRATION
REVISION (the runner behaves correctly).

Against the **real** judge: **BLOCKED — ADAPTER NOT EXECUTABLE.**

## M. Final verdict

**BLOCKED — ADAPTER NOT EXECUTABLE.**

Rationale (honest):
- The **runner, gates, metrics, and rubric** are validated: the calibrator
  computes recall/precision correctly, honors N-A, resists style/length/
  alignment bias on the designed tests, and *discriminates* a good judge from a
  deliberately bad one (ideal all-gates-pass vs flawed gates-1/2/5-fail).
- But "READY FOR PILOT REGRESSION RUN" requires a **real, reproducible,
  calibrated judge**. This environment has no version-pinned programmatic judge
  endpoint, so the real judge cannot be run or measured here. The all-green
  ideal numbers are **plumbing + target**, not a real judge's performance —
  reporting them as readiness would be the exact fakery the round forbids.

**To lift the block** (next round, once an endpoint exists): wire
`ActingModelJudge` per `harness/adapter.md`; re-run this calibration on the 29
gold + holdout set with the real judge; add an over-flagging mock (or real
FP measurement) to stress-test Gate 3; then, only if all gates pass on the
*real* judge, emit READY FOR PILOT REGRESSION RUN.

No core skill changed; no benchmark deleted; no property definition loosened.
The one taxonomy gap (SA-01) is reported for a future round, not patched.
