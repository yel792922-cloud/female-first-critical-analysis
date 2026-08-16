# Reproducibility Report (v0.4)

**Question:** under identical fixture + prompt + skill version + mode, are the
skill's *reasoning* outputs stable, distinguishing textual variance (allowed)
from reasoning variance (recorded)?

## Evidence (bootstrap, LOW independence)
- **v0.3.2 smoke, 3×3:** 3 fixtures (null-result, strawman/E11, aggregate→
  individual/E13), each judged 3×. **Core property verdicts and E-code flags
  were 100% stable** across repeats; evidence *wording* varied (allowed). See
  `../../tests/evaluation-v0.3/reports/adapter-smoke-runs.json`.

| Dimension | Result |
|---|---|
| structural consistency (schema/parse) | stable (9/9 parsed) |
| property consistency (core verdicts) | 3/3 stable per fixture |
| output variation (wording) | present, allowed |
| epistemic variation (commitment) | none observed on these cases |

## Provenance / limits
- model_version = **UNKNOWN** (alias, not pinned); temperature = **UNKNOWN**.
- So observed stability is **empirical over few runs**, NOT a version-pin
  guarantee — an alias backend can change. Strict reproducibility remains
  **pending** an independent, version-pinned endpoint.
- Sample is small and same-family (BOOTSTRAP). Not an independent finding.

## Status
Textual variance ≠ reasoning variance is operationalized and observed to hold
on the tested cases. Durable (version-pinned) reproducibility: **pending
external judge/model pinning**.
