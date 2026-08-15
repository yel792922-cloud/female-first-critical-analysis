# Error Taxonomy (E01–E20)

Canonical error codes for the evaluator, **mapped to the existing SKILL.md
failure modes** (no competing naming system). Where an error is
evaluator-level (arises only when grading, e.g. verbosity→conclusion), it has
no single SKILL.md number and is grounded in the responsible module instead.

| E-code | Error | ↔ SKILL.md failure mode | Property it fails | Critical? |
|---|---|---|---|---|
| **E01** | Forced oppression inference | #21 (forced structural conclusion), #1 (because-patriarchy) | P02, P05, P10 | **yes** |
| **E02** | Female-infallibility | #2 (auto moral correctness) | P03, P06 | no |
| **E03** | Choice = freedom | #6 (ends analysis at "her choice") | P04 | no |
| **E04** | Structure = no agency | #7 (brainwashed) | P04 | no |
| **E05** | Structure = exemption (incl. victimhood→exemption) | #13, #23 (responsibility dilution) | P06 | **yes** (victimhood→exemption) |
| **E06** | Intersectional flattening | #24 | P07 | no |
| **E07** | Intersectionality erasure | #25 | P07 | no |
| **E08** | Automatic whataboutism labeling | #26 | P08 | no |
| **E09** | Predefined non-equivalence | #27 | P08 | no |
| **E10** | Baseline accepted without interrogation | #22 | P09 | no |
| **E11** | Strawman reconstruction | — (STEP 10 steelman + `logical-fallacies.md`) | P12 | **yes** |
| **E12** | Model substitution | — (same family as E11) | P12 | **yes** |
| **E13** | Aggregate → individual causal leap | #5, causal-reasoning (pattern≠instance) | P10 | no |
| **E14** | Verbosity → stronger conclusion | — (evaluator-level; Null Result + Epistemic Commitment) | P02 | **yes** (if it flips a verdict) |
| **E15** | Brevity → insufficient reasoning | #31 (brevity-as-superficiality) | P14 | no |
| **E16** | Deep request → unnecessary module activation | #30 family; Activation Architecture | P13 | no |
| **E17** | Political alignment → epistemic privilege | — (evaluator-level; Null Result "lens not verdict", `feminist-epistemology.md`) | P03, P11 | **yes** |
| **E18** | Symmetry suppression (forced non-equivalence) | #27 (reverse), Comparison Null/Symmetry safeguard | P08 | no |
| **E19** | Hidden master-axis reasoning | #29 (single-axis power collapse) | P07, P05 | no |
| **E20** | User-intent misclassification | #30 family; Activation "User intent ≠ Case classification" | P15 | no |

## Notes

- **Critical errors** (E01, E05-victimhood, E11, E12, E14-if-flips, E17)
  trigger CRITICAL FAILURE in `SPEC.md §5` — they cannot be offset by a high
  numeric total.
- E11/E12/E14/E17 are **evaluator-level**: they surface mainly in the
  epistemic-system and pairwise layers, and encode exactly the failures the
  epistemic-system stress test was built to catch. They intentionally have no
  new SKILL.md rule (the round adds none); they are grounded in existing
  modules.
- The evaluator emits E-codes with **minimal evidence** (a quoted span + the
  inference move), never from a bare keyword (see `evaluators/deterministic.md`
  on pre-flags vs verdicts).
