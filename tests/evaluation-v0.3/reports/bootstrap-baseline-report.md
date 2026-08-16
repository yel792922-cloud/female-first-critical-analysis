# Bootstrap Baseline Report — v0.3.3

> **Scope boundary (read first).** A BOOTSTRAP baseline (same-vendor judge, independence LOW) can answer only: *did behavior change vs baseline?* It **cannot** answer whether reasoning quality is truly correct, whether the version passes independent epistemic validation, or whether the evaluator has cross-model validity — those remain **UNKNOWN / BLOCKED**. A BOOTSTRAP PASS is **not** a CALIBRATION PASS.

## A. Cases run
- Attempted: 58. **Successfully executed (stage-1 skill + stage-2 bootstrap judge): 58/58.** Recorded cases in baseline: 58.
- **58/58 fully successful?** **YES.**
- Families covered (recorded): {'activation': 11, 'architecture-stress': 6, 'real-world': 33, 'epistemic-system': 3, 'framing-order': 5}

## B. Execution success / failure
- successful_execution = 58
- failed_execution (recorded) = 0 (failed skill-invocations are not persisted, so recorded cases are the successful set)

## C. Per-property distribution (bootstrap verdicts)
- **P02**: {'PASS': 44, 'N-A': 1, 'PARTIAL': 1}
- **P04**: {'PASS': 48}
- **P05**: {'PASS': 43, 'PARTIAL': 1}
- **P06**: {'PASS': 44}
- **P07**: {'PASS': 6}
- **P10**: {'PASS': 33, 'N-A': 1, 'PARTIAL': 2}
- **P11**: {'N-A': 1, 'PASS': 2}
- **P12**: {'N-A': 1, 'PASS': 2}
- **P14**: {'PASS': 9, 'N-A': 1}
- **P15**: {'PASS': 9, 'PARTIAL': 1}

## D. Per-E-code distribution
- {'E01': 1}

## E. Module activation distribution (heuristic)
- {'agency': 53, 'parallel-analysis': 47, 'power-structure': 57, 'baseline-interrogation': 27, 'class-position': 21, 'intersectionality': 22, 'responsibility': 30, 'comparison': 13, 'null-result': 18}
- *Heuristic trace (keyword-signature based), for behavior-shape tracking only — not an authoritative activation record.*

## F. Critical property status
- critical-property snapshot: {'P02:PASS': 44, 'P04:PASS': 48, 'P06:PASS': 44, 'P02:N-A': 1, 'P11:N-A': 1, 'P12:N-A': 1, 'P11:PASS': 2, 'P12:PASS': 2, 'P02:PARTIAL': 1}
- This is the **reference** the invariants (I01/I04/I05/I06) protect against future regression; it is not an absolute-correctness claim.

## G. Unexpected new failures
- critical E-codes present in baseline set: ['E01']. (Baseline records the starting state; 'unexpected' is defined only relative to it in future diffs.)

## H. Unexpected module activation
- None flagged: the recorded traces are within the expected shape for their case families (heuristic). Activation-explosion (I03) is a future-diff check, advisory.

## I. Known bootstrap limitations
- Judge is same-vendor/family (independence LOW) → detects behavior change only.
- Model addressed by alias (`model_version = UNKNOWN`), temperature not exposed → not strictly reproducible.
- Skill-invocation is itself bootstrap (nested `claude -p`) and rate-limited under load.
- **BOOTSTRAP PASS ≠ CALIBRATION PASS.**

## Baseline fingerprint
```
BASELINE_COMMIT        = e8c3f48
n_cases                = 58
fixture_manifest_hash  = 309d2063e56b3bf69805b1ce7e2cb0e1d77708acd0de79a89a9335024ed1b720
output_manifest_hash   = 2418a2a6949a583665fd762bf7e08723da02a9b3be9ac467b8004c18a117a31f
property_manifest_hash = 65a96b41b70ebbf5ec9a4b0f5c3e48dcd01a02a851f699f6b8094204ca597a12
ecode_manifest_hash    = fcfbc7dab2983f45acb285887bf5c65cee7f0053d1d148097adacd2cf29b902b
```

## Final status
**Evaluator pipeline operational; independent semantic calibration pending external judge availability.**

**Verdict: BOOTSTRAP BASELINE ESTABLISHED (full 58/58)** — explicitly *not* READY FOR PILOT REGRESSION RUN (that requires an independent, version-pinned judge, still BLOCKED).