# User-Facing Expression Audit (v0.3.4)

Audits whether the skill, because of its many internal safeguards, leaks
**defensive verbosity / rhetorical over-engineering** into user-facing answers
— and whether expression can be made more efficient **without** weakening any
reasoning property. It does **not** change the reasoning architecture (frozen).

> **Think deeply. Surface only what matters.**
> Internal: deep, rigorous, adversarial. External: clear, economical, natural.

## The two errors this audit holds in tension

- *Do not make the reasoning shallower to make the answer shorter.*
- *Do not make the answer longer merely to display that the reasoning was
  careful.*

So concision is **not** the goal; **reasoning-to-expression efficiency** is:
preserve core judgment, evidence calibration, agency, power/structure,
responsibility (where relevant), and *necessary* uncertainty — then surface
only what carries information.

## Key distinctions

- Deep reasoning ≠ verbose exposition
- Reasoning rigor ≠ rhetorical density
- Internal safeguards ≠ user-facing disclaimers
- Information density > raw brevity
- **Necessary uncertainty ≠ unnecessary hedging**
- **Substantive clarification ≠ defensive surplus** (see `metrics.md`)

## Files

- `cases.md` — 12 expression cases (4 low / 4 medium / 4 high complexity),
  each run in 3 expression modes (A natural-concise, B deep-analytical,
  C research-oriented).
- `metrics.md` — the 5 expression metrics, the substantive-vs-defensive rule,
  the X01–X10 critical expression failures.
- `scorecard.md` — 10-dimension expression scorecard (0–2).
- `results.md` — measured findings + the minimal tuning proposal.
- `baseline-v0.3.4/` — recorded outputs + metrics + provenance (expression
  baseline; does **not** touch the immutable 58-case bootstrap baseline).
- `harness/expression_metrics.py` — deterministic proxy analyzer (candidate
  signals only; substantive-vs-defensive needs semantic judgment).

## Relationship to prior work

- The immutable 58-case bootstrap baseline (`evaluation-v0.3/reports/
  bootstrap-baseline/`) is **not modified**. This audit reuses its outputs as
  the natural-mode expression corpus and adds a small A/B/C mode experiment.
- Same layer discipline as v0.3: deterministic proxies **pre-flag**; the
  substantive/defensive verdict is semantic.
