# Cases

v0.3 **reuses the existing benchmark** — no benchmark case is deleted or
re-authored. This folder is an **index + machine manifest**, not a second copy
of the cases. Each evaluation case is a small JSON conforming to
`../schema/case-schema.json` whose `source` points at the real benchmark file.

## Families (source of truth)

| Family (subdir intent) | Source of truth | Count |
|---|---|---|
| `core/` | `../../real-world-benchmark/cases-lifestyle-family.md`, `-sexwork-career.md`, `-intra-women.md` | RWB-01…18 |
| `adversarial/` | `../../real-world-benchmark/cases-rhetoric-traps.md`, `cases-downward-freedom.md`, `cases-null-result.md` | RWB-19…27, DF-01…05, NR-01 |
| `epistemic-system/` | `../../epistemic-system-stress/cases.md` | ES-01…03 |
| `activation/` | `../../real-world-benchmark/cases-activation.md` | AC-A…D, MS-01…05, DR-01…02 |
| `regression/` | `regression/first-suite.md` (this folder) | first pilot suite |

Also indexed: framing-order (`cases-framing-order.md`, FO-01…05) and
architecture-stress (`cases-architecture-stress.md`, AS-01…06).

## Manifest convention

A case manifest is minimal; the prose lives in the benchmark:

```json
{
  "case_id": "RWB-16",
  "source": "tests/real-world-benchmark/cases-intra-women.md",
  "family": "core",
  "prompt": "富裕的都市女性雇了一位来自农村、低薪无社保的住家保姆……",
  "language": "zh",
  "requested_depth": "default",
  "case_complexity": "complex",
  "gold_ref": "tests/evaluation-v0.3/calibration/gold/RWB-16.json"
}
```

No benchmark content is duplicated here beyond the `prompt` field needed to
feed the skill; edits to reasoning content happen in the benchmark, once.
