# Recruitment Criteria (v0.4.7)

## Target N

- **15–24 participants** for the pilot (not powered for hypothesis testing;
  descriptive + exploratory only).
- Minimum to report *any* human signal: **15**. Below 15 real participants →
  record **`HUMAN_PILOT_BLOCKED`** and report nothing as a human result.

## Subgroups (recorded, NOT admission gates)

Feminist familiarity is **not** an inclusion requirement. Participants need only
be able to read a Chinese argument and compare two AI answers. Record for
*exploratory* subgroup analysis only:

| Group | Description | Target share |
|---|---|---|
| **G1** | gender-studies / feminist-familiar | ~1/3 |
| **G2** | general critical-thinking / educated, non-specialist | ~1/3 |
| **G3** | low-involvement / non-specialist | ~1/3 |

Do **not** require participants to endorse feminism. Do **not** interpret any
subgroup difference as causal.

## Recorded covariates (coarse, exploratory only)

- gender-studies familiarity (none / some / formal study)
- prior feminist reading (none / casual / substantial)
- AI-usage frequency (never / occasional / daily)
- educational background (coarse bucket: secondary / undergrad / postgrad)
- self-rated critical-reading familiarity (1–5)
- participant's own gender (self-described, optional, never an inclusion gate)

These are stored hashed/de-identified in the response record; no direct
identifiers are retained.

## Minimum comprehension screen

One warm-up item: read two short AI answers on a neutral topic and state one way
they differ. Purpose is only to confirm the participant can perform the reading
task — it is **not** scored and **not** used to exclude on the basis of *which*
difference they name.

## Exclusion (pre-registered)

- Fails the comprehension warm-up (cannot state any difference).
- Straight-lines every Likert item (zero variance across all cases) — flagged as
  low-effort, reported separately, not silently dropped.
- Completes the full multi-case survey implausibly fast (< a pre-set floor,
  e.g. under ~2 min/case) — flagged, reviewed, reported.

## Consent & ethics

- Informed consent: participants are told they are comparing AI-generated
  analyses and rating them; they are **not** told which answer came from which
  system, nor which outcome the project "wants."
- Debrief after completion: reveal the conditions and the study aim.
- No sensitive personal data collected beyond the coarse covariates above.
- Participants may withdraw; withdrawn data is deleted.

## Blocked-state rules (no substitution)

- **< 15 real participants** → `HUMAN_PILOT_BLOCKED`. Do not simulate
  participants with an LLM.
- **< 2 real annotators** for open-response coding → `HUMAN_CODING_BLOCKED`. Do
  not substitute an LLM coder and report it as human agreement.
- **No humans reachable at all** → status remains `HUMAN PILOT EXECUTION
  PENDING`; only the instruments are delivered.
