# Execution Adapter Design

The harness separates *what it can run deterministically here* from *what needs
an external model call*. Two adapters are required for full automation; both are
**pending** in this environment, and the harness is honest about that
(`ADAPTER_PENDING`) rather than faking a run.

## Adapter 1 — Skill Invocation Adapter

Turns a `case` into an `output` (conforming to `output-schema.json`).

```
invoke_skill(case, skill_version) -> output_json
```

Requirements:
- Runs the target `SKILL.md` version against `case.prompt` at
  `case.requested_depth`, in `case.mode`.
- Must emit the trace fields (`module_trace`, `inactive_declared`,
  `references_cited`, `output_length_chars`) so Layer 1 can run — i.e. the
  skill is invoked with an instruction to append a machine-readable trace block,
  or a wrapper parses them from the answer.

Why pending here: this Claude Code environment has no reproducible,
version-pinned programmatic endpoint to invoke a specific `SKILL.md` revision as
an isolated callable. Faking it would violate the round's rule. Outputs are
therefore supplied as **captured fixtures** for now.

## Adapter 2 — Judge Model Adapter

Backs Layer 2 (property judge) and Layer 3 (pairwise).

```
judge_property(case, output, gold, preflags) -> {P01..P15: {status, evidence, e_codes}}
judge_pairwise(case, output_A, output_B, axis, gold) -> {result, stability{...}}
```

Requirements:
- Low temperature; each property scored independently (no halo).
- Prompt is the anti-bias block from `../evaluators/property-judge.md` +
  the case gold + the deterministic pre-flags.
- Must cite a quoted span per verdict; a span-less verdict is rejected by the
  harness.
- Must pass all six `../evaluator-bias-tests.md` before being trusted
  (calibration gate).

## Wiring checklist (to leave ADAPTER_PENDING)

1. Implement `invoke_skill` against a pinned skill runner; verify trace fields.
2. Implement `judge_*` against a judge model; run `evaluator-bias-tests`.
3. Run `calibration-protocol.md` on the 29-case gold set; meet the acceptance
   gates (recall ≥0.9 on critical E-codes, FP ≤0.2, 0 N-A-as-deficiency, all
   EB tests pass).
4. Only then run `cases/regression/first-suite.md`.

Until step 3 passes, the evaluator's non-deterministic verdicts are advisory,
and the harness reports them as `ADAPTER_PENDING`, not as results.
