# Provenance (v0.4)

Every research artifact carries provenance; UNKNOWN is explicit.

## Fixed per run (schema/run-schema.json)
case_id · prompt · mode · condition · skill_version (git commit or ablation
variant) · fixture_hash · model · model_version · judge · judge_version ·
judge_independence · temperature · timestamp · output · reproducible.

## Current environment provenance (this round)
- model: reachable via `claude -p` (CLI OAuth). **model_version = UNKNOWN**
  (alias, not pinned). temperature = UNKNOWN (not exposed).
- judge: BOOTSTRAP (same vendor/family) — **independence = LOW**. Independent
  judge = **BLOCKED** (no endpoint).
- skill_version baseline: git commit at build time; ablation variants tagged
  `ablate-AX`.
- Known missing data: full ablation sweep + full 20-case OOD live runs are
  **execution-pending** under nested-CLI rate limits; recorded as such, never
  as PASS.

## Non-negotiable
- Do not write UNKNOWN or BLOCKED as PASS.
- Do not claim "scientifically validated" or "universally generalizable".
- Bootstrap evidence is always tagged BOOTSTRAP / LOW INDEPENDENCE.
