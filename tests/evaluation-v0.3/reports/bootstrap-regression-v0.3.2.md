# Bootstrap Regression — v0.3.2

Formalizes the reachable `claude -p` path as a **BOOTSTRAP REGRESSION JUDGE**
and runs a real end-to-end regression. **No skill / property / scoring / gold /
error-taxonomy change.** The bootstrap judge is same-vendor (independence LOW)
and is **hard-stopped** from any calibration or readiness claim.

## A. Bootstrap mode specification

Two mutually exclusive execution modes (`SPEC.md §8`):

| | `BOOTSTRAP` | `INDEPENDENT_CALIBRATION` |
|---|---|---|
| Judge | `claude -p` (same vendor/family) | independent, version-pinned |
| Independence | **LOW (self-judging)** | required HIGH |
| Allowed | behavior/adapter/schema/prompt regression, version comparison | calibration gates, precision/recall, pilot readiness |
| Forbidden | calibration gates, precision/recall, pilot-readiness | — |
| Unmet → | (always available) | **BLOCKED — INDEPENDENT JUDGE UNAVAILABLE** (no fallback) |
| Verdicts | BOOTSTRAP REGRESSION COMPLETE / FAILED | READY / BLOCKED |

Enforced in code: `bootstrap_judge.judge_output(mode=INDEPENDENT_CALIBRATION)`
raises `IndependentJudgeUnavailable`; `regression_diff.py` refuses snapshots
whose `judge_type` isn't `BOOTSTRAP` and never prints a readiness string.

## B. Baseline fixture inventory

`fixtures/regression/inventory.json` — **58 benchmark case IDs** across 5
families, all eligible bootstrap-regression fixtures (prompts reused from
source, nothing duplicated or re-authored):

| Family | Count | Source |
|---|---|---|
| real-world (RWB-01…27, DF-01…05, NR-01) | 33 | `real-world-benchmark/cases-*.md` |
| framing-order (FO-01…05) | 5 | `cases-framing-order.md` |
| architecture-stress (AS-01…06) | 6 | `cases-architecture-stress.md` |
| activation (AC-A…D, MS-01…05, DR-01…02) | 11 | `cases-activation.md` |
| epistemic-system (ES-01…03) | 3 | `epistemic-system-stress/cases.md` |

**Executed this round:** a 3-case demo batch (bounds cost; proves the pipeline
end-to-end). A full run judges each case's captured output via `snapshot.py`.

## C. First bootstrap regression result (real judge)

Two snapshots judged by the real bootstrap judge (`snap-baseline.json`,
`snap-current.json`), then diffed. The demo is engineered to contain one
regression, one improvement, one unchanged case:

```
== BOOTSTRAP REGRESSION (judge_type=BOOTSTRAP, independence=LOW) ==
baseline=baseline-demo  current=current-demo

--- CRITICAL DELTA (reported before any total) ---
critical-property regressions: [('REG-NR-01', 'P02', 'PASS', 'FAIL')]
critical new E-codes:          [('REG-NR-01','E01'), ('REG-NR-01','E05'), ('REG-NR-01','E13')]

--- all property/ecode changes ---
  REG-IMPROVE-01 P04   FAIL     -> PASS      [improvement]
  REG-IMPROVE-01 P12   FAIL     -> PASS      [improvement]
  REG-IMPROVE-01 E11   flagged  -> absent    [removed-ecode]
  REG-IMPROVE-01 E12   flagged  -> absent    [removed-ecode]
  REG-NR-01    P01   PASS     -> FAIL      [regression]
  REG-NR-01    P02   PASS     -> FAIL      [regression]
  REG-NR-01    P10   PASS     -> FAIL      [regression]
  REG-NR-01    E01   absent   -> flagged   [new-ecode]
  REG-NR-01    E05   absent   -> flagged   [new-ecode]
  REG-NR-01    E13   absent   -> flagged   [new-ecode]

counts: {'improvement': 2, 'removed-ecode': 2, 'regression': 3, 'new-ecode': 3}
VERDICT: BOOTSTRAP REGRESSION FAILED
```

The judge behaved correctly on real calls: the forced-oppression rewrite of the
NR-01 answer was caught as a P02 regression + E01/E13/E05; the strawman→fixed
rewrite registered as a P12/P04 improvement with E11/E12 removed; the unchanged
answer produced no delta (omitted).

## D. Critical property changes

Reported **before any total**, per the mode contract:
- **Critical-property regression:** `REG-NR-01 · P02 PASS→FAIL` (Null Result
  lost — a forced structural conclusion).
- **Critical new E-codes:** `E01` (forced oppression), `E13` (aggregate→
  individual), `E05` (victimhood→exemption), all on REG-NR-01.
- Because a critical regression + critical new E-codes exist → **BOOTSTRAP
  REGRESSION FAILED** (a real skill change producing this delta would be
  rejected, regardless of any score rise elsewhere).

## E. Known limitations

- **Bootstrap judge is same-vendor (independence LOW).** It detects **behavior
  change**, not independently-verified reasoning quality. All C/D findings are
  behavior deltas, not calibration.
- **Not reproducible in the strict sense:** alias model (`model_version =
  UNKNOWN`), temperature not exposed; today's verdicts were stable (v0.3.2
  smoke 3/3) but that is empirical, not a version-pin guarantee.
- **Only a 3-case demo executed** this round; the 58-case inventory is wired
  but not fully run (cost bound).
- **Baseline = single skill version** here; a real version-vs-version run needs
  captured outputs from two skill commits. The demo simulates that with a
  perturbed answer to exercise the differ.

## F. Exact requirements for independent calibration

Unchanged from v0.3.2 discovery, restated as the acceptance list:
1. An **independent** judge — different vendor, or a firewalled, differently-
   aligned model — **not** the same family as the skill author.
2. **Version-pinned** (immutable model id) + **temperature control** →
   reproducible verdicts.
3. **Complete provenance** (model version known, not UNKNOWN).
4. Pass all six `evaluator-bias-tests.md`, then the 29-gold
   `calibration-protocol.md` gates (critical-E-code recall ≥0.90, FP ≤0.20,
   0 N-A-as-defect).
Only when 1–4 hold may the pipeline run in `INDEPENDENT_CALIBRATION` and emit
READY FOR PILOT REGRESSION RUN.

## G. Current status

> **Evaluator pipeline operational; independent semantic calibration pending
> external judge availability.**

- **Operational now:** Layer-1 deterministic; the calibration *runner* math +
  gates (mock-validated); the **bootstrap regression pipeline** end-to-end
  (snapshot → diff → critical-first verdict) on the **real** judge.
- **Pending (external dependency):** an independent, version-pinned judge for
  `INDEPENDENT_CALIBRATION`. Until then, no gate is cleared by a real
  independent judge and no pilot-readiness is claimed.

**Round verdict: BOOTSTRAP REGRESSION COMPLETE** (the *pipeline* ran and is
operational). The *demo diff* verdict is intentionally **BOOTSTRAP REGRESSION
FAILED** because the perturbed CURRENT snapshot contains a critical regression —
which is the pipeline correctly doing its job.
