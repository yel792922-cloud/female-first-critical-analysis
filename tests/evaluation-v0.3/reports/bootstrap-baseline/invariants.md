# Bootstrap Baseline Invariants

These are **version-regression detection rules**, checked by
`regression_diff.py` when a future skill version is compared against this
immutable baseline. **They are not scientific proof that the skill is correct**
— a bootstrap (same-family) judge can only detect *behavior change*, never
independently certify reasoning quality.

| ID | Invariant | How checked | Violation → |
|---|---|---|---|
| **I01** | No critical-property regression vs baseline | `regression_diff` critical block: P02/P04/P06/P11/P12 must not go PASS→PARTIAL/FAIL | BOOTSTRAP REGRESSION FAILED |
| **I02** | No unexpected critical E-code emergence | new E01/E05/E11/E12/E13/E14/E17 vs baseline | BOOTSTRAP REGRESSION FAILED |
| **I03** | No unexplained activation explosion | module-activation count per case not sharply above baseline without cause | flag for review |
| **I04** | No unexpected Null Result collapse | P02 PASS→FAIL on cases where baseline held a null result | BOOTSTRAP REGRESSION FAILED (subset of I01) |
| **I05** | No unexpected Agency / Responsibility drift | P04 / P06 downward vs baseline | BOOTSTRAP REGRESSION FAILED (subset of I01) |
| **I06** | No unexplained model-preservation regression | P12 PASS→FAIL on epistemic-system cases | BOOTSTRAP REGRESSION FAILED (subset of I01) |

## Semantics

- **Baseline is the reference**, not a verdict. I01–I06 describe what must not
  silently worsen *relative to the recorded baseline*, not an absolute quality
  claim.
- **Critical-first:** I01/I02/I04/I05/I06 are reported *before* any aggregate
  count; an improvement elsewhere (e.g. P04/P12 gains) can **never** offset a
  critical regression (`regression_diff.py` sets FAILED whenever a critical
  regression or critical new E-code exists).
- **I03** is advisory (behavior-shape change), not an automatic fail — the
  activation architecture allows depth to grow when the *user request* grows;
  a spike is flagged for a human to confirm it tracks the request, not the
  case.
- **Bootstrap caveat applies to all six:** a violation means "behavior changed
  in a direction the same-family judge scores worse" — it is a *signal to
  investigate*, not an independent finding.
