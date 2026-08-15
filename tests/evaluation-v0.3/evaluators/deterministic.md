# Layer 1 — Deterministic Evaluator

Rule/structure only. **No LLM.** Implemented in `../harness/run_eval.py`.
Everything here is mechanically verifiable; nothing here decides a reasoning
property on its own.

## Checks

1. **Output schema valid** — output JSON conforms to `output-schema.json`.
2. **Case-ID match** — `output.case_id == case.case_id`.
3. **Required fields present** — `answer_text` non-empty; `skill_version` set.
4. **Module trace present** — `module_trace` exists (may be empty on a trivial
   case, but the field must be there for P13/P14 mechanics).
5. **No dangling references** — every entry in `references_cited` exists under
   the repo `references/` directory. A cited-but-missing reference is a FAIL.
6. **Self-audit block** — present iff the case `mode` requires it
   (`argument-reconstruction` requires it; `standard` does not).
7. **Necessary-module presence (mechanical part of P14)** — for each module the
   gold annotation lists under `expected_modules.necessary`, that module must
   appear in `module_trace`. A missing *necessary* module is a FAIL and a
   candidate **E16/E20** depending on direction.
8. **Inactive-module respect (mechanical part of P13)** — for each module the
   gold lists under `expected_modules.inactive`, that module must **not** be in
   `module_trace`. Its presence is a candidate **E16** (over-activation) —
   flagged, then confirmed by the judge.
9. **Depth-length bucket (mechanical part of P15)** — `output_length_chars`
   bucketed (short <600 / medium / long >1800) must be consistent with
   `case.requested_depth`. A `concise` request with a `long` output, or a
   `deep` request with a `short` output, is a candidate **E15/E20** — flagged.
10. **Execution-error scan** — truncation markers, empty answer, obvious
    template leakage.

## Shortcut pre-flags (candidate signals ONLY)

The deterministic layer may emit **pre-flags** — heuristic string/pattern hits
that *might* indicate an E-code — but these are **routed to Layer 2**, never
turned into a verdict. **Keyword presence ≠ property satisfaction or
violation.** Examples of conservative pre-flag patterns (zh):

| Pattern (illustrative) | Candidate E-code | Why only a pre-flag |
|---|---|---|
| "显然是父权" / "就是父权制导致" near a single-instance claim | E01 | may be justified if evidence was actually presented |
| "她自己选的，所以…自由/没问题" | E03 | may be a quoted view the answer then refutes |
| "被父权洗脑" / "她其实不想" | E04 | may be flagged *by the answer* as a trap |
| "都是女性" used to equate two women's power | E06 | may be the position the answer criticizes |
| "男的也…所以" as a topic-closer | E08 | may be correctly labeled derailment by the answer |
| absence of any hedge on an underdetermined claim | E01/E14 | needs semantic read of what's underdetermined |

A pre-flag carries the matched span and is attached to the judge prompt as
"inspect this"; the judge confirms or clears it. A pre-flag that the judge does
not confirm is discarded (contributes to false-positive analysis, §calibration).

## Output

A `deterministic` object per `evaluation-schema.json`: `passed` (all hard
checks green), the `checks` array, and `shortcut_preflags`.
