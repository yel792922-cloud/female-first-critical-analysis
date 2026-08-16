# Baseline Report (v0.4)

The research baseline is the **immutable 58-case bootstrap baseline** from
v0.3.3 (`../../tests/evaluation-v0.3/reports/bootstrap-baseline/`,
BASELINE_COMMIT=e8c3f48), reused unchanged as the reference condition for
ablation and generalization comparison.

## Reference distribution (58 real outputs, BOOTSTRAP judge)
- P04 (agency) 48/48 PASS; P02 (null result) 44 PASS / 1 PARTIAL / 1 N-A;
  P06 (responsibility) 44 PASS; P10 (causal) 33 PASS / 2 PARTIAL / 1 N-A.
- Only 1 E-code (E01) across the whole set.
- Fingerprint: fixture/output/property/ecode manifest hashes recorded in
  `FINGERPRINT.json`.

## Role in v0.4
- **Ablation** compares each single-module-removed variant against this
  reference on the relevant subset.
- **Generalization** compares OOD behavior against the property expectations,
  not against a fixed answer.
- The baseline is **not modified** by v0.4 (immutability preserved).

## Provenance / limits
BOOTSTRAP judge (LOW independence), model_version UNKNOWN. This is a *behavior*
reference, not an independent-quality certification.
