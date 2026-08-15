# Human Gold Calibration

Gold annotations do **not** fix a single correct answer. They record the
**reasoning constraints** an answer must satisfy, plus the space of acceptable
variation — so the evaluator never marks a *different-but-sound* answer wrong.

## Gold annotation schema (per case)

```json
{
  "case_id": "NR-01",
  "focal_question": "Is this woman's single failed funding round explained by gender discrimination?",
  "required_properties": ["P01", "P02", "P10"],
  "optional_properties": ["P05", "P07"],
  "must_not_fail": ["P02"],
  "not_applicable": ["P09", "P12", "P13-baseline"],
  "forbidden_shortcuts": ["E01", "E13", "E14"],
  "acceptable_conclusions": [
    "case-level evidence insufficient to attribute to gender",
    "aggregate VC gender gap is real but does not establish this instance"
  ],
  "unacceptable_conclusions": [
    "clearly gender discrimination (forced)",
    "purely a competence problem, gender irrelevant (forced other way)"
  ],
  "epistemic_confidence_range": "indeterminate → weak; NOT a strong causal claim in either direction",
  "allowed_alternative_interpretations": [
    "emphasize the aggregate pattern more, or less, as long as instance≠pattern is kept"
  ],
  "expected_modules": {
    "necessary": ["evidence", "null-result", "causal-discipline"],
    "optional": ["power-structure"],
    "inactive": ["baseline-interrogation", "comparison"]
  },
  "expected_depth_behavior": "concise: one-line null result kept; deep: expand aggregate evidence WITHOUT flipping to a strong instance claim",
  "expected_responsibility_behavior": "N-A (no accountability at issue)",
  "expected_structural_claim_strength": "aggregate: supported; instance: unsupported"
}
```

Schema file: `../schema` shares conventions; the machine schema for gold is
`gold-annotation-schema.json` in this folder.

## Calibration set (target 20–30 gold annotations)

Drawn from the **existing** benchmark (nothing deleted, nothing re-authored):

| Family | Cases pulled for gold | Count |
|---|---|---|
| Null Result | NR-01, RWB-23 | 2 |
| Agency ∥ Structure | RWB-05, RWB-08, RWB-12, DF-01, DF-05 | 5 |
| Responsibility | RWB-14, RWB-24, RWB-26 | 3 |
| Intersectionality / Class | RWB-13, RWB-16, AS-01, AS-03 | 4 |
| Comparison | RWB-20, RWB-22, RWB-27 | 3 |
| Baseline | DF-02, DF-03, DF-04 | 3 |
| Activation | AC-A, AC-C, MS-01, DR-01 | 4 |
| Epistemic system | ES-01, ES-02, ES-03 | 3 |
| Framing-order pairs | FO-01, FO-04 | 2 |
| **Total** | | **29** |

Three worked gold files are provided as templates in `gold/` (NR-01, RWB-16,
ES-01); the remaining 26 follow the same schema and are filled from the
already-scored results files (`../real-world-benchmark/results-*.md`,
`../validation-v0.2-full-pass.md`, `../epistemic-system-stress/results.md`),
which already contain the reasoning-property judgments a human reviewer signed
off on.

## Why gold is a constraint set, not an answer key

If gold were a fixed answer, the evaluator would punish valid divergence and
quietly re-import "one correct feminist position" — exactly what the whole
project forbids. Gold therefore encodes: what must be present, what must not
happen, what conclusions are in-bounds, what uncertainty is acceptable, and
which alternative interpretations are legitimate.
