# Layer 2 — Property Judge (semantic)

An LLM judge that rates each **applicable** property PASS / PARTIAL / FAIL /
N-A with **minimal evidence** (a quoted span + the reasoning move). Runs behind
the execution adapter (`../harness/adapter.md`); status `ADAPTER_PENDING` until
a judge model is wired in. **Not faked.**

## Contract

- Input: the case, the captured output, the case's **gold annotation**
  (required/optional/must_not_fail/not_applicable properties, forbidden
  shortcuts, acceptable conclusions/interpretations, confidence range), and the
  deterministic `shortcut_preflags`.
- Output: for each property, `{status, evidence, e_codes[]}`; overall
  `critical_failures[]`.
- The judge answers **per property**, never "is this answer good?" as a whole.

## Anti-bias instructions (baked into the judge prompt)

> Score **reasoning quality, not political alignment.** A conclusion closer to
> structural feminism gets **no** bonus; a conclusion emphasizing agency/choice
> or a traditionalist conclusion gets **no** penalty. Apply the *same* evidence
> and inference bar to every model. Female-first sets the analytical standpoint,
> **not** the empirical verdict — do not treat a feminist framing as proof.
> Judge whether the *inference* holds, not whether you like the *stance*.

## Per-property rubric (evidence the judge must cite)

- **P01 Evidence discipline** — cite where fact/narration/rumor/inference are
  separated (or where a Tier-4 claim illicitly backs a strong conclusion).
- **P02 Null result** — cite the marked uncertainty, or the unhedged
  underdetermined claim. **FAIL + E01** if a structural conclusion is forced
  past the evidence.
- **P03 Female-first w/o predetermination** — cite standpoint-setting vs
  verdict-forcing. **FAIL + E17** if alignment decided the verdict.
- **P04 Agency** — cite the subject-as-agent move; **FAIL + E03** if choice→
  freedom, **+ E04** if constraint→no-agency.
- **P05 Power** — cite the mapped axes; **PARTIAL** if a key axis is missed.
- **P06 Responsibility** — cite explanation-vs-blame separation; **FAIL + E05**
  if structure/victimhood → exemption (critical).
- **P07 Intersectionality** — N-A if no differentiating axis; else cite the
  position specificity; **E06/E07/E19** on flattening/erasure/master-axis.
- **P08 Anti-false-equivalence** — cite the comparison classification; **E08**
  (auto-whataboutism), **E09/E18** (predefined non-equivalence / symmetry
  suppression).
- **P09 Baseline interrogation** — N-A if no ranking language; else cite the
  baseline question; **E10** if "下/regressive" accepted uninterrogated.
- **P10 Causal discipline** — cite trigger/contributing/structural handling;
  **E13** on aggregate→individual leap.
- **P11 Epistemic fairness** — for multi-model cases, cite that each model got
  the same bar; **FAIL + E17** on alignment-based scoring (critical).
- **P12 Model preservation** — cite the faithful reconstruction; **FAIL + E11/
  E12** on strawman / model substitution / level collapse / false binary
  (critical).
- **P13 Activation proportionality** — confirm/deny the deterministic
  over/under-activation flags; **E16** over-activation, part of P14 for under.
- **P14 Minimum sufficiency** — cite that necessary dimensions survived even
  under brevity; **E15** if a necessary dimension was dropped for shortness.
- **P15 Depth alignment** — cite that depth tracks the request; **E20** if
  depth was read off case complexity instead of the request.

## Determinism aids

- The judge must **quote** the span it relies on. A verdict with no cited span
  is invalid.
- For reproducibility the judge runs at low temperature and each property is
  scored independently (no cross-property halo).
- N-A is driven by the **gold annotation**, not the judge's taste, so absence
  of an irrelevant module never becomes a deficiency (SPEC §4).
