# Research Protocol — SPEC (v0.4)

## 1. Research mode
Invoked only when the user asks (e.g. "用于 research，结构化输出"). Produces
`schema/research-mode-schema.json`. Rules:
- Each focal claim is independently codable and **typed**: empirical / causal /
  normative / interpretive / definitional.
- `evidence_status` per claim: well-supported / partial / contested /
  insufficient / not-applicable.
- `epistemic_uncertainty` may be non-empty; a null/indeterminate conclusion is
  legitimate.
- `conclusion` is NOT required to be unique; `valid_alternative_interpretations`
  records other sound readings.
- Never mixed into an ordinary natural-language answer.

## 2. Reproducible run
A run record (`schema/run-schema.json`) fixes: case · prompt · mode · condition
· skill_version · fixture_hash · model · model_version · judge ·
judge_version · judge_independence · temperature · timestamp · output ·
evaluation_properties · reproducible. **UNKNOWN is written explicitly** (e.g.
model_version=UNKNOWN for alias models); never guessed, never omitted.

## 3. Dataset formats
JSON/JSONL. Supports single, multi-turn, competing-epistemic-models,
concise/deep, baseline/treatment, and ablation conditions. Each sample is
independently replayable from its run record.

## 4. Ablation design (single variable)
`harness/ablate.py` copies SKILL.md and removes exactly ONE `## ` module,
leaving all others byte-identical:
A1 Null Result · A2 Baseline Interrogation · A3 Responsibility ·
A4 Intersectionality · A5 Comparison discipline · A6 Parallel Analysis ·
A7 Class/Position Power. One module removed per variant. The canonical SKILL.md
is never modified. Runs use `claude -p --append-system-prompt-file
SKILL.ablate-AX.md`.

## 5. Ablation metrics (per condition, not just totals)
For each ablation, over the relevant benchmark subset, compare to baseline on:
Evidence · Agency · Power · Responsibility · Null Result · Causal ·
Intersectionality · Anti-false-equivalence · Epistemic fairness · Model
preservation · Activation behavior · Expression efficiency. Report:
baseline · ablation · delta · **critical regression** (critical-first) ·
new failure modes (E-codes) · module interaction (does removing A change a
property nominally owned by B?).

## 6. Generalization / OOD
20 cases with NO feminist vocabulary in 4 categories, testing whether the
skill still executes evidence/agency/power/responsibility/comparison/null-
result — and whether female-first wrongly gates rigor to women's topics.

## 7. Female-first boundary
5 controls: F+gender-structure · M+gender-structure · F+non-gender-power ·
M+non-gender-power · mixed-gender institution. Female-first must set the
analytical standpoint WITHOUT (a) ignoring male subjects, (b) genderizing
non-gender power, (c) forcing gender onto every conflict.

## 8. Reproducibility
Same fixture+prompt+version+mode repeated. Record structural / property /
output / epistemic consistency. Distinguish **textual variance** (allowed) from
**reasoning variance** (recorded). No requirement of textual identity.

## 9. Evaluator independence boundary
Independent judge remains externally BLOCKED. All bootstrap evidence stays
tagged BOOTSTRAP / LOW INDEPENDENCE. This round may NOT claim independent
evaluator validation.
