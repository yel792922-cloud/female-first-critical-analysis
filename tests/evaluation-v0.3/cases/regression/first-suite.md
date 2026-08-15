# First Regression Suite (v0.3 pilot)

The first automated regression batch covers the **four highest-value property
families** (per the round). Each maps to gold-annotated cases already scored by
human/LLM review, so the pilot measures the *evaluator*, not new content.

## 1. Null Result — `evidence insufficient ≠ forced oppression`
- **Cases:** NR-01, RWB-23.
- **Guards:** P02, P10; forbidden E01, E13, E14.
- **Pilot assertion:** deep mode must **not** flip the null result to a strong
  structural claim; aggregate pattern must stay distinct from the instance.

## 2. Agency ∥ Structure — `choice ≠ liberation`, `constraint ≠ no agency`
- **Cases:** RWB-05, RWB-12, DF-01, FO-01, FO-04.
- **Guards:** P04, P05, P06; forbidden E03, E04; framing-lock (#28) via
  pairwise `agency-structure`.
- **Pilot assertion:** agency-first and structure-first prompts converge on the
  same agency/structure/responsibility reading.

## 3. Comparison — `comparison ≠ equivalence`, `male experience ≠ automatic derailment`
- **Cases:** RWB-20, RWB-22, RWB-27.
- **Guards:** P08; forbidden E08 (auto-whataboutism), E09/E18 (predefined
  non-equivalence / symmetry suppression).
- **Pilot assertion:** legitimate comparison admitted (RWB-27), derailment
  correctly labeled (RWB-20), false balance refused (RWB-22).

## 4. Epistemic System — `standpoint ≠ verdict`, `alignment ≠ credit`, `preservation ≠ strawman`
- **Cases:** ES-01, ES-02, ES-03.
- **Guards:** P03, P11, P12; forbidden E11, E12, E17.
- **Pilot assertion:** each competing model judged on the same bar; no model
  gets an alignment bonus; no view rebuilt as a version it disclaims.

## Running the pilot

```
python3 ../../harness/run_eval.py --suite first-suite --version <N> [--baseline <N-1>]
```

Layer 1 runs now (deterministic). Layers 2–3 return `ADAPTER_PENDING` until a
judge model is wired via `../../harness/adapter.md`. The pilot is not "passed"
until the calibration gates in `../../calibration/calibration-protocol.md` are
met.
