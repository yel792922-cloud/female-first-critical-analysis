# Sample Run (real, Layer 1)

Command:

```
python3 harness/run_eval.py --demo --markdown
```

This is an **actual** execution of the deterministic layer on `../fixtures/`
(NR-01, one good output and one strawman/forced-oppression output). Layers 2–3
are `ADAPTER_PENDING` (no judge model wired — see `../harness/adapter.md`). No
non-deterministic verdict is fabricated.

## Output (verbatim)

### NR-01 — bad output (`v0.0-strawman`)
- deterministic layer: **FAIL**
  - [PASS] case_id_match — NR-01 vs NR-01
  - [PASS] answer_text_nonempty
  - [PASS] skill_version_set
  - [PASS] module_trace_present
  - [FAIL] no_dangling_references — dangling: references/nonexistent-file.md
  - [N-A] self_audit_present — not required in standard mode
  - [FAIL] necessary_module:evidence — missing necessary module → candidate under-activation
  - [FAIL] necessary_module:null-result — missing necessary module → candidate under-activation
  - [PASS] inactive_module_absent:baseline-interrogation
  - [PASS] inactive_module_absent:comparison
  - [PASS] depth_length_consistent(default→short)
- shortcut pre-flags (routed to Layer 2, **not** verdicts):
  - `E01` «显然就是父权» — strong structural claim marker — verify evidence
- property judge: 5 ADAPTER_PENDING, 2 N-A → [P09, P12]
- **verdict: FAIL** (deterministic hard-check failure)

### NR-01 — good output (`v0.2.7`)
- deterministic layer: **PASS**
  - [PASS] case_id_match / answer_text / skill_version / module_trace
  - [PASS] no_dangling_references
  - [N-A] self_audit_present — not required in standard mode
  - [PASS] necessary_module:evidence
  - [PASS] necessary_module:null-result
  - [PASS] inactive_module_absent:baseline-interrogation
  - [PASS] inactive_module_absent:comparison
  - [PASS] depth_length_consistent(default→short)
- property judge: 5 ADAPTER_PENDING, 2 N-A → [P09, P12]
- pairwise: ADAPTER_PENDING
- **verdict: ADAPTER_PENDING** (deterministic passed; awaiting judge)

## What this demonstrates

- **Deterministic layer works and discriminates:** the strawman/forced-
  oppression output is caught *without any LLM* — it drops the `null-result`
  and `evidence` modules the gold marks **necessary**, cites a **dangling
  reference**, and trips the **E01** pre-flag on "显然就是父权". The good output
  passes every mechanical check.
- **Keyword ≠ verdict:** the `E01` hit is emitted as a **pre-flag routed to the
  judge**, not as a property verdict. The deterministic layer never claims the
  output "failed P02" — only that a mechanical check failed and a candidate
  signal exists.
- **N-A is honored:** P09 (baseline) and P12 (model-preservation) are N-A for
  NR-01 per its gold annotation, excluded from scoring — *absence of baseline
  interrogation on a no-ranking case is not a deficiency.*
- **Honesty about pending layers:** the good output ends at `ADAPTER_PENDING`,
  not `PASS` — the harness will not certify a semantic pass without the judge
  adapter and calibration gates.

## Not yet run (adapter-pending, by design)

Layer 2 property verdicts, Layer 3 pairwise stability, and the calibration
metrics (precision/recall/FP/FN vs the 29-case gold set) require the judge
adapter. Their specifications, prompts, gold format, and acceptance gates are
complete; the runs are **not** fabricated.
