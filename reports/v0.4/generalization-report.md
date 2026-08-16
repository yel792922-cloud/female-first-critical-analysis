# Generalization / OOD Report (v0.4)

**Dataset + boundary design complete. Live OOD runs execution-pending under
nested-CLI rate limits — NO generalization pass/fail is claimed from data.**

## Dataset (ready)
`../../tests/research-protocol/dataset/generalization.jsonl` — 20 OOD cases,
NO feminist vocabulary, 4 categories:
- non-feminist-vocab power (platform/algorithm, non-compete, eviction, gig
  labor, advisor power),
- male-subject (male harassment victim, emotional-suppression norm, low-status
  man vs executive, custody default, male nurse stereotype),
- gender-neutral institutional (triage, exam reform, KPI, visa policy,
  insurance pricing),
- AI/media/org bias (hiring AI, recommender, one-sided media, "LLM has a
  stance", promotion-rate aggregate).

`boundary.jsonl` — 5 female-first boundary controls: F+gender-structure,
M+gender-structure, F+non-gender-power, M+non-gender-power, mixed-gender
institution.

## Research question (to be tested)
Does the skill still execute evidence/agency/power/responsibility/comparison/
null-result **without** feminist vocabulary — and does **female-first wrongly
gate rigor to women's topics** or **genderize non-gender power**? Metrics:
property-execution rate, over-genderization rate (target 0), male-subject
engagement (target high).

## Live evidence this round
- **0 OOD cases successfully executed** — the two attempted (G-B1 male-subject,
  G-C5 insurance) were rate-limited before completion. Recorded as
  **execution-pending**, not as a result.
- Indirect prior signal (not OOD, not a substitute): the 58-case bootstrap
  baseline already includes male-subject and comparison cases (RWB-20 "men
  suffer too", RWB-26 male DV victim, RWB-27 occupational segregation) which
  scored on the same properties — suggesting the machinery is not gated to
  women-only inputs. This is **suggestive, not an OOD finding.**

## Status
Generalization **benchmark READY**; generalization **results execution-pending**.
No generalization or female-first-boundary finding is asserted from data this
round.
