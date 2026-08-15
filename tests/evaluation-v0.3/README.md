# Evaluation v0.3 — Automatic Reasoning-Property Evaluation

An offline harness that checks whether a skill output **satisfies reasoning
properties**, and whether a new skill version **regresses** against a previous
one. It is **not** a "did it give the correct feminist answer?" checker.

> **Epistemic consistency > textual sameness.**
> **Reasoning properties > political alignment.**
> **Property satisfaction > fixed conclusion.**

## Three independent evaluator layers

1. **Deterministic** (`evaluators/deterministic.md`, `harness/run_eval.py`) —
   rule/structure checks only; no LLM. Format, required fields, module trace,
   dangling references, schema validity, and *heuristic* shortcut pre-flags
   (candidate signals routed to Layer 2 — **never** a verdict on their own).
2. **Property judge** (`evaluators/property-judge.md`) — a semantic judge that
   rates each property **PASS / PARTIAL / FAIL / N-A** with minimal evidence.
   Runs behind an execution adapter (an LLM call). **Not faked here.**
3. **Pairwise / contrastive** (`evaluators/pairwise.md`) — compares two outputs
   (concise vs deep, agency-first vs structure-first, old vs new version,
   original vs reconstructed argument, two competing models) and returns
   STABLE / STABLE-WITH-ELABORATION / REASONING-REFINEMENT / POSSIBLE-DRIFT /
   MATERIAL-DRIFT.

The three layers are **kept separate on purpose**: what can be checked by rule
is never handed to a judge, and what needs judgment is never faked by keyword
matching.

## Layout

```
evaluation-v0.3/
├── README.md              ← this file
├── SPEC.md                ← properties P01–P15, weighting, critical-failure
├── error-taxonomy.md      ← E01–E20 ↔ SKILL.md failure-mode map
├── regression-protocol.md ← version-vs-version, critical-property tracking
├── evaluator-bias-tests.md← 6 anti-bias tests for the evaluator itself
├── schema/                ← case / output / evaluation JSON schemas
├── cases/                 ← core · adversarial · epistemic-system · activation · regression
├── evaluators/            ← deterministic · property-judge · pairwise specs
├── calibration/           ← human-gold schema + gold annotations + protocol
├── fixtures/              ← mock case+output JSON for the sample run
├── harness/               ← run_eval.py (runnable Layer 1) + adapter.md
└── reports/               ← report format + sample run
```

## Execution status (honest)

- **Layer 1 (deterministic)** is **actually runnable** here:
  `python3 harness/run_eval.py` operates on captured output JSON in
  `fixtures/` and produces a report. A real sample run is recorded in
  `reports/sample-run.md`.
- **Layer 2 (property judge)** and **Layer 3 (pairwise)** require an LLM-judge
  call behind an **execution adapter** (`harness/adapter.md`). This environment
  cannot deterministically/programmatically invoke the skill or a judge model
  in a verifiable, reproducible way, so those layers are marked
  **`ADAPTER_PENDING`** — their prompts, output schemas, and gold calibration
  are fully specified, but **no automated judge run is fabricated**.
- **Skill invocation** (turning a case into an output) is likewise adapter-
  pending: outputs are supplied as fixtures for now.

This is deliberate: the round's rule is *don't pretend automated execution
succeeded.* What runs, runs; what needs an adapter is specified, not faked.

## Cases

Cases **reuse the existing benchmark** (no benchmark deleted). `cases/` indexes
the real-world benchmark (33), framing-order (5), architecture-stress (6), and
epistemic-system (3) cases, plus the v0.3 first regression suite
(`cases/regression/first-suite.md`) covering the four highest-value property
families.
