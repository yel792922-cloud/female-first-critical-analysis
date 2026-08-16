# Research Protocol (v0.4)

Turns the skill into a **research-able methodology system**: reproducible runs,
a research-mode structured output, an ablation framework, an out-of-domain
generalization benchmark, a human-annotation protocol, and provenance-complete
reports. **No feminist principle is added or changed; SKILL.md is not
modified.** Ablation variants are generated as *copies* — the canonical
SKILL.md stays untouched.

> Honesty carries over from v0.3: the only reachable judge is same-vendor
> (**BOOTSTRAP / independence LOW**). This round builds infrastructure and runs
> bootstrap/analyst evidence; it does **not** claim independent evaluator
> validation, "scientifically validated", or "universally generalizable".

## Contents

- `SPEC.md` — research mode, run protocol, ablation design, reproducibility.
- `schema/` — case / prompt / run / annotation / output / research-mode JSON
  schemas. Every run record fixes case·prompt·mode·skill_version·fixture_hash·
  model·model_version·judge·judge_version·timestamp·output (UNKNOWN written
  explicitly).
- `dataset/generalization.jsonl` — 20 OOD cases (non-feminist-vocab power,
  male-subject, gender-neutral institutional, AI/media/org bias).
- `dataset/boundary.jsonl` — 5 female-first generalization-boundary controls.
- `annotation/protocol.md` — human annotation (properties + epistemic
  commitment, not a single correct answer).
- `harness/ablate.py` — single-module ablation variant generator (A1–A7).
- `metrics.md`, `provenance.md`.
- Reports live in `../../reports/v0.4/`.

## Research mode (invoked only on request)

Normal use → natural language. **Research mode** (user asks for it) → the
`research-mode-schema.json` structure: Question · Focal claims (each typed
empirical/causal/normative/interpretive/definitional + evidence status) ·
Power/structure · Agency · Responsibility · Alternative explanations ·
Epistemic uncertainty · Conclusion (not required unique; multiple valid
interpretations allowed). Research mode is **never** mixed into ordinary
answers.

## Execution status

- Infrastructure (schemas, datasets, ablation generator, protocols) is
  **complete and deterministically verified** (ablation generator removes
  exactly one section, SKILL.md unchanged).
- Live model runs (ablation sweeps, full 20-case OOD, reproducibility) are
  **rate-limited** by the nested-CLI throttle; this round executes a **bounded
  demonstration** and marks the remainder execution-pending. Every report shows
  sample size, provenance, and missing data — no UNKNOWN/BLOCKED is written as
  PASS.
