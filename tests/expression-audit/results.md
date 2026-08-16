# Expression Audit — Results (v0.3.4)

Measurement of user-facing expression efficiency. **No skill change made this
round.** Evidence base: (1) deterministic expression metrics over the **58 real
skill outputs** in the immutable bootstrap baseline (natural/default mode);
(2) a live concise-mode datapoint (makeup, Mode A). The full A/B/C live
experiment was **largely rate-limited** by the environment's nested-call
throttle — only Mode A landed cleanly; this is stated wherever it limits a
claim.

## 1. Corpus-level metrics (58 real outputs, deterministic proxies)

| Metric (per 1000 chars) | mean | median | p90 | max |
|---|---|---|---|---|
| **Defensive density** | 0.41 | **0.00** | 0.68 | 9.9* |
| **Hedge density** | 1.83 | 1.69 | 3.35 | 6.45 |
| **Module-narration density** | 0.80 | 0.84 | 1.64 | 2.55 |
| Output length (chars) | 2090 | 1976 | 3237 | 4718 |
| Redundant distinctions | ~0 across the set (none in the top cases) | | | |

\* the 9.9 max is MS-01, a 101-char one-liner where a single clarifier inflates
the per-1k rate — a length artifact, not verbosity.

**Reading:** defensive markers are **absent in the median output**; redundant
distinctions are essentially nil; hedging is moderate; module narration is
low, elevated only in a handful of cases. The dominant surface variable is
**raw length**, which in this corpus tracks case depth (epistemic-system mean
2807, deep DR-01 3555) rather than safeguards.

## 2. Concise-mode datapoint (makeup, Mode A: "化妆是不是媚男？简单说。")

346 chars, 10 short sentences. Deterministic: **0 defensive markers, 0 module
narration, 0 redundant distinctions**, 2 hedges. Content: conclusion-first, 4
bullets each carrying *distinct* information (motive multivalence/agency;
anti-"correct-woman"; double-standard; the reframed real question), one-line
close. Reasoning properties present (agency, anti-correct-life, double
standard, baseline-interrogation) in a compact, clean answer — **no defensive
surplus, no checklist narration.**

## 3. Substantive vs defensive split (top-signal cases)

The highest defensive-density real cases were inspected against the
`metrics.md` rule:
- **RWB-23** ("有钱女性还算压迫", 1.61/1k) — its clarifications are **substantive**:
  the case has a genuine two-axis confusion (class power vs gendered
  constraint), so "有钱不等于不受性别约束" *changes/qualifies* the reading.
  Not surplus.
- **RWB-03 / RWB-20** — clarifications tie to real double-standard / derailment
  misreadings. Substantive.
- No case showed a run of information-free "这并不意味着…/也不能推出…" surplus.

The highest module-narration cases (**RWB-12 2.55, AS-01 2.41, RWB-06 2.28**)
are the one mild, real pattern: occasional "从 agency 角度…/从结构角度…" framing
where the sections could be merged. This is **X02/X05 (checklist narration /
module leakage)** at low frequency — present, not systematic.

## 4. Answers to the round's questions

- **A. Systematic defensive verbosity?** **No.** Median defensive density 0.0;
  concise-mode output has zero defensive markers; the elevated cases are
  substantive clarifications, not surplus.
- **B. Which class worst?** None severe. The mildest real signal is **module
  narration** in a small minority of real-world/architecture cases.
- **C. Which metric dominates?** Ranked: (1) **overall length** (default mode,
  ~2090 mean) > (2) module narration (few cases) > (3) hedging (moderate) >
  (4) defensive ≈ (5) redundancy (both ~0). No metric rises to a defect.
- **D. Simple-question over-engineering?** **Mild, not severe.** Concise makeup
  = 346 clean chars; slightly fuller than a minimal reply (4 bullets), but each
  bullet is distinct information with no surplus.
- **E. Does deep add info or safeguards?** **Partially measured (rate-limited).**
  Corpus proxy: deep/complex outputs have *low* defensive density (0.79–0.84)
  and moderate hedging while being long — i.e. length comes from mechanisms,
  steelman, and distinctions, **not** safeguards. Tentative: adds information.
  A full live A/B/C confirmation is **pending** (nested-call throttle).
- **F. Complex-concise sufficiency preserved?** **Not re-measured live this
  round** (maid-concise rate-limited). Prior evidence (v0.2.7 AC-C, validation
  full pass) showed the multi-axis core survives compression; carried forward,
  live re-confirmation pending.
- **G. Is expression efficiency independent of reasoning quality?** **Yes.**
  makeup-A shows full reasoning rigor in 346 clean chars — length and rigor are
  separable axes (exactly the audit's premise).
- **H. Clear tuning target?** At most **one, low-leverage**: gently discourage
  "从 X 角度" module-narration phrasing where sections restate one judgment. The
  data does **not** justify more.

## 5. Verdict

**NO SYSTEMATIC ISSUE.**

The deterministic evidence over 58 real outputs plus the clean concise-mode
datapoint does **not** support a systematic defensive-verbosity / rhetorical-
over-engineering problem: defensive density is zero at the median, redundant
distinctions are nil, hedging is moderate, and the elevated-caveat cases are
*substantive*. The only real (mild, non-systematic) signal is occasional module
narration in a minority of cases.

### Optional micro-note (NOT a required change; hold recommended)

If, later, module narration is judged worth trimming, the **minimal** and
**only** change would be one sentence in the Activation Architecture's *output*
guidance (not a principle, not a reasoning rule):

> *"Conceal module names in the output: surface conclusions, not a 'from-agency
> / from-structure' process log. Merge sections that restate one judgment."*

This is a **presentation** nudge (aligns with the existing "modules activate by
relevance" spirit and the parallel-analysis 'both-true close'), touches **no**
feminist principle, and affects only surface form. **Recommendation: do not
apply it this round** — the measured frequency (a handful of cases) does not
justify even this, and the reasoning architecture is frozen. Log it as a
candidate for a future presentation-only pass if a larger sample confirms the
pattern.

## 6. Known limitations

- Metrics are **deterministic proxies** (candidate signals); the substantive-
  vs-surplus final call is semantic (done by inspection here, at small scale).
- The live **A/B/C mode experiment was rate-limited**; only Mode A (makeup)
  landed. Deep/research-mode and complex-concise live confirmation are
  **pending** environment headroom — their claims above are marked tentative or
  carried from prior rounds, never asserted as fresh measurement.
- Corpus is single-version (frozen skill), same-family generated — an
  expression *baseline*, not a cross-model finding.
