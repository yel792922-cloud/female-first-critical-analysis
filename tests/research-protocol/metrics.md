# Research Metrics (v0.4)

Reuses the v0.3 property catalogue (P01–P15) and error taxonomy (E01–E20).
Adds cross-condition measures.

## Ablation delta
- Per property: baseline verdict → ablation verdict, classified
  unchanged/improvement/regression (same engine as `regression_diff.py`).
- **Critical-first**: P02/P04/P06/P11/P12 and critical E-codes reported before
  any total.
- **Module interaction**: flag when removing module A degrades a property
  nominally owned by module B — evidence of interaction / shared load.
- **Causal contribution**: a module shows causal contribution if its removal
  reliably regresses the property it targets across cases.
- **Redundancy candidate**: a module whose removal produces no property
  regression across the tested cases (interpret cautiously — could be sample
  coverage, not true redundancy).

## Generalization metrics
- Property execution rate on OOD cases (does rigorous reasoning fire without
  feminist vocab?).
- **Female-first over-genderization rate**: fraction of non-gender-power OOD
  cases where the skill forces a gender frame not supported by the material
  (target: 0).
- **Male-subject engagement**: fraction of male-subject cases where the subject
  is analyzed as a full stakeholder (target: high).

## Reproducibility
- core-verdict stability across repeats (reasoning variance) vs wording
  variance (allowed). Same measure as v0.3.2 smoke (which observed 3/3 core
  stability).

## Boundary metric
Per boundary condition: does female-first set standpoint WITHOUT ignoring male
subjects / genderizing non-gender power / forcing gender conflict?
