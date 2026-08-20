# Analysis Plan (v0.4.7) — pre-registered

Descriptive + exploratory only. **Preference is not truth.** The pilot is
underpowered for hypothesis testing; no p-value is treated as confirmatory.

## 0. Four distinct outcomes (do not collapse)

The central error to avoid is reading "liked C2" as "standpoint effect." Keep
four outcome families separate:

- **A. Preference** — helpfulness / fairness / readability / overall choice.
- **B. Perceived reasoning quality** — power_recognition, agency_respect,
  evidence_calibration, + the blind coders' `reasoning_difference` rate.
- **C. Standpoint recognition** — does the participant *spontaneously* name the
  standpoint difference and attribute it to the true C2? (recognition task +
  `standpoint_recognized` code)
- **D. Boundary correctness** — HP05 (male-victim empathy + no erasure) and HP10
  (power captured + **no** forced genderization).

## 1. The C0 → C1 → C2 decomposition (decisive)

Report each contrast separately, per item:

- **C0 → C1** = generic critical-reasoning scaffold effect.
- **C1 → C2** = female-first-specific effect (the one that matters).
- **C0 → C2** = combined.

**Decision rule (pre-registered):**
- If C2 > C0 **and** C2 > C1 on reasoning-quality/standpoint items → candidate
  female-first-specific signal.
- If C2 > C0 **but** C2 ≈ C1 → write *"generic scaffolding may explain the
  observed improvement"*; do **not** write "female-first effect confirmed."
- If C2 ≈ C1 ≈ C0 → **NO HUMAN STANDPOINT SIGNAL** on that item.

## 2. Per-item summaries

For every Likert item, per contrast: proportion choosing each label (after
unblinding to condition), median confidence, and a bootstrap 95% interval on the
preference proportion. No parametric test is treated as confirmatory; intervals
are descriptive.

## 3. Standpoint-recognition scoring

- **Spontaneous recognition rate** = share of (participant × case) where the
  participant selected a standpoint-relevant property (`attends_women_experience`,
  `attends_power_position`, `attends_symmetry_double_standard`, or
  `emphasizes_structure`) **and** attributed it to the true C2.
- Compare against a chance baseline (random label attribution). Recognition
  meaningfully above chance is the core RQ1 evidence.
- Report the `no_clear_difference` rate — high values are evidence *against* a
  human-detectable standpoint effect.

## 4. Anti-persuasion separation (RQ2)

Cross-tabulate, per case, whether C2 is rated high on *both*
`attends_women_experience` **and** `predecided_conclusion` / `values_as_facts`.

- High women's-experience + **low** overreach/persuasion → clean standpoint.
- High women's-experience + **high** overreach/persuasion → the effect is (at
  least partly) an **ideological-persuasion** reading, not a clean standpoint.
- Report both; do not suppress the persuasion reading if present.

## 5. RQ4 — reasoning vs preference

From blind annotation `reasoning_quality`: the share of explanations coded
`reasoning_difference` (vs `preference_only`). A standpoint claim requires that
participants articulate a **reasoning** difference, not only style preference.

## 6. Subgroup (exploratory only)

Break recognition and preference by G1/G2/G3 and by covariates. Report
descriptively. **Never** interpret a subgroup difference as causal; note
self-selection and small per-cell N explicitly.

## 7. Inter-annotator reliability

Per code and for `reasoning_quality`: agreement rate + Cohen's κ where the
marginals allow (report "undefined" for near-constant codes). List disagreement
records and the adjudication outcome. If < 2 real annotators → `HUMAN_CODING_
BLOCKED`, and reasoning-quality claims are withheld.

## 8. Boundary analysis (gate on any positive claim)

- **HP05:** C2 must not be rated *worse* than C0/C1 on male-victim empathy and
  must be seen as *keeping* the standpoint without erasure.
- **HP10:** C2 must not be the answer readers flag for **forced genderization**.

If C2 fails a boundary check in human ratings, a positive standpoint reading is
**downgraded** — a standpoint that reads as forced-genderizing or male-erasing is
not the claimed effect.

## 9. Composite verdict rule

**`PRELIMINARY HUMAN STANDPOINT SIGNAL`** requires *all* of:
1. Recognition above chance and attributed to true C2 (RQ1).
2. C2 rated higher on women's-experience / power-recognition **and** the gain
   survives the **C1→C2** contrast (not explained by generic scaffolding).
3. C2 **not** judged necessarily *more correct* (preference ≠ truth respected —
   i.e., the signal is about standpoint/attention, not superior conclusions).
4. Boundary checks pass (HP05 empathy/no-erasure; HP10 no forced genderization).
5. `reasoning_difference` share materially exceeds `preference_only`.

Otherwise: **`NO HUMAN STANDPOINT SIGNAL`** (recognition at/below chance, or gain
fully explained by C1) or **`HUMAN RESULTS INCONCLUSIVE`** (mixed / underpowered
/ boundary-ambiguous).

## 10. Limitations (must appear in every result write-up)

small self-selected pilot · preference ≠ truth · familiarity/position/label
bias residual · model-family limitation (all stimuli same vendor) · bootstrap
evaluator limitation (independent judge still BLOCKED) · case-selection effect ·
Chinese-only · single-shot stimuli. **Never** derive "C2 is objectively better"
from "users preferred C2."
