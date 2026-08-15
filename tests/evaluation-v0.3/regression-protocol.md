# Regression Protocol

Purpose: after any change to `SKILL.md`, `references/`, triggers, output
templates, or module definitions, re-run the suite and compare **new version
vs previous version** — surfacing property regressions that a rising total
score could otherwise hide.

## Procedure

1. Capture outputs for the suite under **version N-1** and **version N** (same
   cases, same prompts).
2. Layer-1 deterministic on both.
3. Layer-2 property judge on both.
4. Layer-3 pairwise on each `(N-1, N)` pair with `axis: "version"`.
5. Emit a **regression report** (below).

## Regression report contents

- **Property regressions** — properties that went PASS→PARTIAL/FAIL. Listed
  **per property**, never averaged away.
- **Property gains** — PARTIAL/FAIL→PASS.
- **Newly-triggered failures** — E-codes present in N, absent in N-1.
- **Newly-activated modules** — modules active in N, not N-1 (watch for E16
  over-activation creeping in from a wording change).
- **Epistemic-commitment changes** — pairwise MATERIAL-DRIFT on any case.
- **Uncertainty-calibration changes** — cases where marked-uncertain claims
  changed status.

## The critical-property rule (non-negotiable)

> A version may **not** be accepted if any **critical property** (P02, P06,
> P11, P12) or any **critical E-code** (E01, E05-victimhood, E11, E14-if-flips,
> E17) regressed — **even if the overall numeric total rose.**

The report prints a dedicated **CRITICAL DELTA** block at the top, before any
total. A total-score improvement with a critical-property regression is a
**FAILED** regression, reported as such.

## Example header

```
REGRESSION  v0.2.6 → v0.2.7      suite: first-suite (Null/Agency/Comparison/Epistemic)
CRITICAL DELTA:  P02 stable · P06 stable · P11 stable · P12 stable · E01 none · E17 none  → OK
totals:  property-normalized 0.94 → 0.95   (informational only)
property regressions: none
property gains: P15 (2 cases) — depth alignment improved
newly-triggered failures: none
newly-activated modules: none
verdict: ACCEPT
```

## Scope discipline

The regression suite is for detecting **skill** change effects. It must not be
used to justify editing the skill to please the judge (SPEC §7). If a
regression is really a *judge* artifact, fix the judge and re-run, do not
touch `SKILL.md`.
