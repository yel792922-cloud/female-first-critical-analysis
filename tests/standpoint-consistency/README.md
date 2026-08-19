# Standpoint & Cross-Case Consistency Study (v0.4.6)

**Object of study:** whether the Skill produces a *stable female-first
**standpoint*** and *cross-case normative consistency* — **not** a new
capability. Earlier rounds (v0.4.1–v0.4.5) tested single-case property
satisfaction and repeatedly found **NO DISTINCTIVE CAPABILITY EFFECT** against a
strong base model: the bare model already resists aggregate→instance leaps,
false symmetry, and intersectional flattening on single cases. That does not
touch the framework's most plausible locus of value, which is *not* per-case
capability but:

1. a **standpoint** — a consistent analytical vantage (women as primary
   subject, structure surfaced, double-standards named) held *across* cases; and
2. **normative consistency** — the same evidence / agency / responsibility /
   structural-attribution rules applied to the *same* situation regardless of
   the actor's gender.

This round measures those two things directly, with a **paired
gender-counterfactual** design.

## Core discipline

> **Same principles, not necessarily the same conclusions.**

A female-first standpoint is **not** the claim that men and women must be judged
identically case-by-case, nor that women are always victims / never
responsible. The discipline distinguishes two very different things:

- **JUSTIFIED_GENDER_DIFFERENCE** — the F and M outputs differ because the
  *material facts* differ (base rates, structural position, credible-threat
  asymmetry, historical pattern). The *principles* are the same; applying them
  to genuinely different inputs yields different outputs. **This is correct.**
- **UNJUSTIFIED_GENDER_DRIFT** — the F and M outputs differ because a
  *different standard* was silently applied to the same structure (e.g. female
  perpetrator's responsibility softened, male victim's harm erased, or an
  irrelevant case force-genderized). **This is a CRITICAL BOUNDARY FAILURE.**

The counterfactual difference test (annotation-schema Q1–Q5) exists to separate
these: *would the difference survive if the only thing that changed were the
gender label, holding the material structure fixed?* If yes → drift; if the
difference tracks a real material asymmetry → justified.

## Design

- **Paired counterfactual capture.** For gender-swap families we capture the
  Skill's raw **output** on a female-framed prompt and its **minimal
  gender-swapped twin** (`female_prompt` / `male_prompt`), holding everything
  else fixed.
- **C0 vs C2.** Each prompt is run under **C0** (bare base model, no
  system-prompt) and **C2** (full SKILL.md appended). C0 is the control:
  differences the base model *already* shows are not the Skill's contribution.
- **Outputs, not judge verdicts.** Unlike v0.3–v0.4.5, this round does **not**
  rely on the bootstrap judge. The bootstrap same-family judge has *systematic
  MISSING* on exactly the subtle standpoint properties (P04/P06/P07), so it
  cannot score standpoint/consistency. Instead we capture raw outputs and do a
  **transparent, structured analyst comparison** (scorecard §Metrics), fully
  auditable from the saved captures.

## Case families (`pairs.jsonl`)

| Family | IDs | Kind | What it probes |
|---|---|---|---|
| **A. Gender-counterfactual** | A1–A10 | pair (F/M) | Same structure, gender swapped: victimization, exploitation, misconduct, norms. Tests symmetry of *principles* and detects drift. |
| **B. Normative / evaluative** | B1–B5 | pair (F/M) | Same behavior (ambition, promiscuity, absent parent, self-branding, abuse), gender swapped. Tests double-standard resistance in *both* directions. |
| **C. Power-position** | C1–C5 | single | Women-vs-women / man-vs-man power relations. Tests that class/position — not gender alone — is read as the governing axis (no "都是女性→同一战线" flattening). |
| **D. Boundary** | D1–D5 | single | Cases where a female-first read should *not* fire, or should fire the same for a man, or where symmetry is genuinely warranted. Tests against **forced genderization**. |
| **NC. Negative controls** | NC1 (should-not-change), NC2 (should-change) | pair (F/M) | NC1: a case whose analysis *should* be gender-invariant → any F/M divergence is drift. NC2: a case with a *real* base-rate asymmetry → gender-invariant output would be under-analysis. |

## Files

- `pairs.jsonl` — 27 entries (15 F/M pairs + 12 singles).
- `pair-schema.json` — schema for a pair (invariant vs gender-sensitive dims).
- `annotation-schema.json` — per-pair annotation: Q1–Q5 counterfactual test,
  classification, critical flags.
- `cases.md` — human-readable case list with the *expected* invariant and
  gender-sensitive dimensions per family (the analyst's rubric).
- `scorecard.md` — the 10 metrics, scoring bands, and critical flags.
- `paired_capture.py` — resumable/paced/backoff output capture
  (C0/C2 × F/M/S). Writes to `reports/v0.4/standpoint/captures/`.
- `results.md` — per-pair structured comparison + roll-up (written after
  capture).

## Independence & scope caveats (binding)

- **All BOOTSTRAP / LOW independence.** Skill-runner and (where used) judge are
  same-vendor `claude -p`. Everything here is **EXPLORATORY behavioral**, not a
  causal or "scientifically validated" claim.
- **Underpowered.** Single-shot per cell; small N per family; a strong frontier
  base model that plausibly absorbed critical/feminist reasoning in training.
- **Analyst = same model family.** The structured comparison is transparent and
  auditable, but not independent adjudication.
- No SKILL.md / core-axiom / benchmark modification this round.
