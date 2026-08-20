# Human Pilot Results (v0.4.7) — TEMPLATE (no data yet)

**STATUS: `HUMAN PILOT EXECUTION PENDING`.** This file is a template. It is
filled **only** with real participant and real annotator data. No LLM-generated
participants or annotators. Every `<…>` is a placeholder.

## Provenance

- Stimuli generated: `<yes/no>` · runner commit `<sha>` · model `<id>` ·
  temperature `<t>`
- Participants recruited (real humans): `<N>` (need ≥ 15, else HUMAN_PILOT_BLOCKED)
- Annotators (real humans): `<K>` (need ≥ 2, else HUMAN_CODING_BLOCKED)
- Blinding manifest: `packets/manifest.json` seed `<seed>`

## Sample

| Subgroup | n |
|---|---|
| G1 feminist-familiar | `<n>` |
| G2 general | `<n>` |
| G3 low-involvement | `<n>` |

Excluded/flagged: `<n low-effort>`, `<n length-confound>`.

## RQ1 — Standpoint detection

- Spontaneous recognition rate (attributed to true C2): `<x%>` vs chance `<y%>`.
- `no_clear_difference` rate: `<z%>`.

## RQ2 — Value vs verbosity/ideology

Per contrast (C0→C1, **C1→C2**, C0→C2), proportion favoring the higher condition:

| Item | C0→C1 | C1→C2 | C0→C2 |
|---|---|---|---|
| helpfulness | | | |
| fairness | | | |
| power_recognition | | | |
| agency_respect | | | |
| evidence_calibration | | | |
| readability | | | |
| overreach (higher = worse) | | | |
| predecided_conclusion | | | |
| values_as_facts | | | |

Clean-standpoint vs persuasion cross-tab (women's-experience × overreach):
`<summary>`.

## RQ3 — Subgroup (exploratory, non-causal)

`<G1 vs G2 vs G3 recognition & preference; note self-selection>`

## RQ4 — Reasoning vs preference

- `reasoning_difference`: `<x%>` · `preference_only`: `<y%>` · `mixed`: `<z%>`.

## Boundary checks

- **HP05 male victim:** C2 empathy rating vs C0/C1 `<…>`; erasure flagged? `<…>`.
- **HP10 non-gender power:** C2 forced-genderization flag rate `<…>`.

## Inter-annotator reliability

| Code | agreement | κ |
|---|---|---|
| standpoint_recognized | | |
| agency_recognized | | |
| structure_recognized | | |
| overreach_identified | | |
| double_standard_recognized | | |
| male_experience_retained | | |
| reasoning_quality (4-way) | | |

Disagreement records + adjudication: `<…>`.

## Decomposition verdict

- C0→C1 (generic scaffold) effect: `<present/absent/size>`
- **C1→C2 (female-first-specific) effect: `<present/absent/size>`**
- If C2 > C0 but C2 ≈ C1 → *"generic scaffolding may explain the observed
  improvement."*

## Final status (choose exactly one, only with real data)

- [ ] `PRELIMINARY HUMAN STANDPOINT SIGNAL` — all 5 composite conditions met.
- [ ] `NO HUMAN STANDPOINT SIGNAL`
- [ ] `HUMAN RESULTS INCONCLUSIVE`
- [ ] `HUMAN_PILOT_BLOCKED` (< 15 participants)
- [ ] `HUMAN_CODING_BLOCKED` (< 2 annotators)

**Do NOT output "scientifically validated." Preference ≠ truth.**

## Limitations

small self-selected pilot · preference ≠ truth · residual
familiarity/position/label bias · same-vendor model-family stimuli · independent
judge still BLOCKED · case-selection effect · Chinese-only · single-shot stimuli.
