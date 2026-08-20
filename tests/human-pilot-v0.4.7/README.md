# Human Pilot & Standpoint Annotation (v0.4.7)

**Status: `HUMAN PILOT EXECUTION PENDING`** — this round delivers the *protocol,
instruments, stimulus plan, randomization, analysis plan, and blind-coding
scheme*. It does **not** contain participant data. This environment cannot
recruit real humans; per the round constraints, **no LLM-generated "participants"
are used and no fake human data is produced.** When ≥15 real participants and ≥2
real annotators are available, the pipeline runs unchanged and results drop into
`results-template.md`.

## Why this round exists

v0.4.1–v0.4.5 found **no distinctive capability effect** of the Skill over a
strong base model on single-case property satisfaction. v0.4.6 found a
**preliminary standpoint effect**: the Skill's plausible marginal contribution is
**standpoint / framing / attention allocation**, not base reasoning capability —
*but that reading was made by a same-family analyst.* The open question is
whether a **human reader** identifies that difference and judges it **more
valuable** rather than merely **longer / more theoretical / more ideological /
more persuasive.** That is a question only humans can answer, so this round builds
the human-in-the-loop instrument.

## Research questions

- **RQ1** — Can humans detect the actual analytical difference between C2
  (female-first Skill), C1 (generic scaffold), and C0 (bare base)?
- **RQ2** — Is that difference judged *more analytically valuable / fairer / more
  attentive to women's experience* — and **not merely** longer / more
  theoretical / more aligned with a feminist stance?
- **RQ3** — Do feminist-familiar vs general vs low-involvement readers evaluate
  the Skill differently?
- **RQ4** — Can participants articulate a real *reasoning* difference, not just
  "I prefer this phrasing"?

## The three conditions (blind to participants)

| Cond | What | Role |
|---|---|---|
| **C0** | bare base model (`claude -p`) | floor |
| **C1** | generic critical-reasoning scaffold (`GENERIC-SCAFFOLD.md`, zero gender content) | isolates *generic scaffolding* effect |
| **C2** | full female-first Skill (`SKILL.md`) | the thing under test |
| **C3** *(optional)* | human-written exemplar analysis | not required for the pilot |

**The decisive contrast is C1→C2, not C0→C2.** C0→C1 estimates the generic
scaffold's effect; only C1→C2 approximates a *female-first-specific* effect. If
C2 beats C0 but **not** C1, the report must say *"generic scaffolding may explain
the observed improvement,"* never *"female-first effect confirmed."*

## Deliverables in this directory

| File | Purpose |
|---|---|
| `README.md` | this overview |
| `recruitment-criteria.md` | who, how many, subgroups, exclusion, HUMAN_PILOT_BLOCKED rule |
| `participant-protocol.md` | end-to-end session script; the per-case tasks A–G, standpoint-recognition, anti-persuasion, boundary checks |
| `case-set.md` | the 8–10 cases, their prompts, why each was chosen, and which existing captures are reused as stimuli |
| `randomization.md` | blind A/B/C label assignment, order counterbalancing, provenance ledger |
| `survey-schema.json` | machine schema for the participant response record |
| `annotation-schema.json` | machine schema for the 2-coder blind open-response coding |
| `analysis-plan.md` | pre-registered analysis; preference vs reasoning-quality vs recognition vs boundary; C0→C1→C2 decomposition; subgroup rules; limitations |
| `results-template.md` | empty result tables + verdict slots (filled only with real data) |
| `harness/stimulus_gen.py` | reproducible C0/C1/C2 stimulus generation (reuses v0.4.6 captures where they exist) |
| `harness/build_packets.py` | assembles blinded, randomized participant packets from stimuli + `randomization.md` |

## Hard constraints honored this round

- **No SKILL.md / core-axiom / evaluator / benchmark modification.**
- **No new feminist principles.**
- **No fabricated participants or annotators.** If real humans are unavailable,
  status stays `HUMAN PILOT EXECUTION PENDING`; if recruited but too few,
  `HUMAN_PILOT_BLOCKED`; if humans run but coding lacks 2 real annotators,
  `HUMAN_CODING_BLOCKED`.
- **No causal / "scientifically validated" claims.** Preference ≠ truth.
- **No PR.**

## Terminal-state vocabulary (what this round may output)

- `HUMAN PILOT READY` — instruments complete **and** stimuli generated/blinded.
- `HUMAN PILOT EXECUTION PENDING` — instruments complete, awaiting real humans.
- With real data only: `PRELIMINARY HUMAN STANDPOINT SIGNAL` /
  `NO HUMAN STANDPOINT SIGNAL` / `HUMAN RESULTS INCONCLUSIVE`.
