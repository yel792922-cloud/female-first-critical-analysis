# Validation Summary (v0.2 full pass)

One-screen summary of the dual-mode validation. Full detail:
[`validation-v0.2-full-pass.md`](validation-v0.2-full-pass.md).

**Design.** All 33 scored benchmark cases run twice — **Mode A (concise)** and
**Mode B (deep)** — 66 runs. Goal: **epistemic consistency, not textual
sameness.** Deep mode may add theory/mechanism/qualifiers; it must not silently
change the core judgment, causal strength, confidence, agency, or
responsibility.

**Results.**

| Classification | Count |
|---|---|
| STABLE | 14 |
| STABLE WITH ELABORATION | 14 |
| REASONING REFINEMENT | 2 |
| POSSIBLE DRIFT (presentation-emphasis only) | 3 |
| **MATERIAL DRIFT** | **0 / 66** |

**Key findings.**

- **Judgment invariance:** core judgments unchanged across A/B in all 33.
- **Epistemic calibration:** confidence did **not** scale with length —
  showcase NR-01 keeps its null result even in deep mode; no verbosity→stronger
  conclusion, no brevity→omitted conclusion.
- **Module invariance:** necessary module set identical in A/B; deep mode never
  activated an irrelevant module.
- **Compression quality:** 33/33 concise runs preserved minimum sufficiency —
  *brevity ≠ superficiality*.
- **Decoupling holds:** simple case + deep request → deep (no auto-module
  sweep, no raised certainty); complex case + concise request → brief but
  multi-axis core preserved.
- **Only variance:** mild *presentation* emphasis on `opposite-valid`
  sexualized-labor + false-balance cases (RWB-10, DF-02, RWB-22) — not
  epistemic drift.

**Verdict: READY FOR v0.3**, contingent only on a *judge-calibration*
requirement — the automated evaluator must score epistemic consistency (not
textual sameness) and treat emphasis variance on `opposite-valid` cases as
stable-with-elaboration. **No core-architecture tuning required before v0.3.**
