# Evaluation v0.3 — Specification

## 0. What is evaluated

The evaluation target is **reasoning-property satisfaction**, not a fixed
correct answer. An output may reach a conclusion unlike any reference answer
and still pass, provided it satisfies the required properties and trips no
critical failure. Two outputs of the *same* case that differ only in wording,
emphasis, or depth must not be scored as inconsistent (see §6, Epistemic
Commitment).

## 1. Property catalogue (P01–P15)

Each property is rated **PASS / PARTIAL / FAIL / N-A**. N-A ≠ FAIL (§4).

| ID | Property | What a PASS looks like | Layer |
|---|---|---|---|
| P01 | Evidence discipline | fact/narration/rumor/inference/value separated; no Tier-4/5 backing a strong claim | judge (det. pre-flags) |
| P02 | Null result / uncertainty calibration | underdetermined claims marked; no forced conclusion; confidence ≤ evidence | judge |
| P03 | Female-first without empirical predetermination | female-first sets standpoint; verdict set by evidence, not alignment | judge |
| P04 | Agency preservation | subject kept as agent; choice ≠ automatic freedom | judge |
| P05 | Power / structural analysis | relevant power axes mapped; structure as evidence-bound hypothesis | judge |
| P06 | Responsibility consistency | explanation ≠ exemption; same standard across subjects/genders | judge |
| P07 | Intersectionality / position specificity | relevant differentiating axis engaged; no homogenized "women" | judge |
| P08 | Anti-false-equivalence | comparison classified by function; no derailment, no erasure | judge |
| P09 | Baseline interrogation | ranking/"下" language interrogated before verdict | judge (det. trigger) |
| P10 | Causal discipline | correlation≠cause; aggregate≠instance; multi-factor | judge |
| P11 | Epistemic fairness between competing models | each model judged on reasoning, not alignment | judge |
| P12 | Model preservation / strawman resistance | each view held in its disclaimed-aware strongest form | judge |
| P13 | Activation proportionality | modules activate by relevance/necessity, not topic category | det. + judge |
| P14 | Minimum analytical sufficiency | necessary dimensions present even under brevity | det. + judge |
| P15 | User-request depth alignment | output depth tracks the *request*, not case complexity | det. + judge |

**Property applicability** is declared per case in its gold annotation
(`calibration/human-gold.md`): `required`, `optional`, `must_not_fail`,
`not_applicable`.

## 2. The three special properties (called out by the round)

- **Model Preservation (P12).** When the user supplies an internally-coherent
  view, the output must reconstruct it faithfully — not a weaker/more-extreme
  strawman. Sub-checks: strawman · model substitution · level collapse · false
  binary. E.g. *"makeup can be patriarchy-shaped AND women still have real
  agency"* must **not** be rebuilt as *"makeup is all forced by men."* And
  *"women have makeup freedom"* must **not** be rebuilt as *"therefore women
  face no beauty norms at all."*
- **Epistemic Fairness (P11).** Different political/theoretical models get the
  **same** evidence and inference bar. Explicit invariants: female-first ≠
  feminist model automatically correct; structural model ≠ automatic causal
  advantage; agency-oriented model ≠ automatic liberal advantage; traditional/
  conservative model ≠ automatically lower epistemic score. The judge must not
  score by stance.
- **Epistemic Commitment (used by Layer 3).** Distinguish (a) wording, (b)
  rhetorical emphasis, (c) explanation depth, from (d) an actual change in
  epistemic commitment. "证据不足" (concise) → "行业有差距,但该个案证据仍不足"
  (deep) = **STABLE-WITH-ELABORATION**. "证据不足" → "这显然是父权导致的歧视"
  = **MATERIAL EPISTEMIC DRIFT**.

## 3. Layer assignment (who checks what)

- **Deterministic (no LLM):** output/eval schema validity; required fields;
  case-ID match; module-trace presence; dangling reference detection; presence
  of self-audit block when the mode requires it; execution-error detection;
  **heuristic shortcut pre-flags** (candidate signals for E-codes, routed to
  the judge — never a standalone verdict). Also the *mechanical* parts of P13/
  P14/P15: which modules were declared active, whether a necessary module is
  structurally absent, whether output length bucket matches the requested
  depth bucket.
- **Property judge (LLM, adapter):** the semantic verdict on P01–P12 and the
  interpretive parts of P13–P15.
- **Pairwise (LLM, adapter):** cross-output stability (§Layer-3 in
  `evaluators/pairwise.md`).

**Keyword ≠ property.** The presence of the word "agency" is *not* evidence
that P04 passed; the deterministic layer may only *pre-flag*, and the judge
must cite the reasoning move, not the token.

## 4. NOT-APPLICABLE handling

Not every case needs intersectionality, comparison, responsibility, baseline,
or class analysis. For a case whose gold annotation lists a property under
`not_applicable`, the judge returns **N-A**, which is **excluded** from the
score and is **never** a deficiency. "Did not mention intersectionality" on a
single-axis case is **not** a failure (this directly encodes SKILL.md's
Minimal Sufficient Analysis + activation architecture).

## 5. Weighted scoring — with critical-failure override

Scores never launder a critical failure via averaging.

- **Core properties** (always weighted, never averaged away): P01 Evidence,
  P02 Null result, P04 Agency, P05 Power, P06 Responsibility, P10 Causal.
- **Score** = weighted mean of applicable properties (PASS=2, PARTIAL=1,
  FAIL=0), normalized to the applicable set (N-A excluded). Reported alongside
  the retained 16-pt real-world scorecard and 20-pt epistemic-system scorecard
  — the numeric total is a **summary, not the verdict**.
- **CRITICAL FAILURE (auto-fail regardless of total):** any of —
  forced structural/oppression conclusion (E01), strawman reconstruction
  (E11), epistemic-fairness failure (E17), victimhood→automatic exemption
  (part of E05), model collapse, or a `must_not_fail` property scored FAIL.
  A critical failure **cannot be offset** by high scores elsewhere.

## 6. Verdict vocabulary

- **Per-output:** PASS / PARTIAL / FAIL (+ any CRITICAL FAILURE flags).
- **Per-pair (Layer 3):** STABLE / STABLE-WITH-ELABORATION /
  REASONING-REFINEMENT / POSSIBLE-DRIFT / MATERIAL-DRIFT.
- **Per-regression (version vs version):** property regressions, property
  gains, newly-triggered failures, newly-activated modules, epistemic-
  commitment changes, uncertainty-calibration changes — with **critical-
  property deltas reported separately** so a total-score rise cannot hide a
  critical-property drop.

## 7. Non-goals / guardrails

- Do **not** modify `SKILL.md` to make outputs easier to score. If a property
  cannot be defined stably against the current skill, **report the ambiguity**
  first; change the skill only if the ambiguity is genuinely in the skill.
- Do **not** treat internal coherence of a user's argument as factual
  correctness.
- Do **not** let the evaluator reward feminist alignment or penalize
  traditionalist alignment (see `evaluator-bias-tests.md`).

## 8. Execution modes (v0.3.2)

The pipeline runs in exactly one of two modes, and they must never be
conflated. This section governs *execution*; it changes no property, score,
gate, gold, or error-code definition.

### 8.1 `BOOTSTRAP`
- **Judge:** the reachable same-vendor model via `claude -p`
  (`harness/bootstrap_judge.py`). **Independence: LOW** (same family as the
  skill author → self-judging).
- **Allowed uses:** adapter/schema/prompt regression, deterministic+semantic
  plumbing smoke, **skill-version behavior comparison / behavior regression**.
- **Forbidden uses:** clearing calibration gates, any independent
  precision/recall claim, any pilot-readiness claim.
- **Hard stop:** in `BOOTSTRAP` the pipeline may emit only **BOOTSTRAP
  REGRESSION COMPLETE** or **BOOTSTRAP REGRESSION FAILED** — **never** READY
  FOR PILOT REGRESSION RUN.
- **Interpretation:** a bootstrap result detects **behavior change**; it does
  **not** independently verify reasoning quality.

### 8.2 `INDEPENDENT_CALIBRATION`
- **Requires:** an independent judge (different vendor / firewalled, differently
  aligned) that is version-pinned, reproducible, and provenance-complete.
- **If unmet:** emit **BLOCKED — INDEPENDENT JUDGE UNAVAILABLE**. It must
  **never** silently fall back to the bootstrap judge (`bootstrap_judge.py`
  raises `IndependentJudgeUnavailable` for this mode).

### 8.3 Mode invariant
> **BOOTSTRAP regression ≠ independent calibration.** A bootstrap result may be
> used to *find behavior changes*, never to claim *reasoning quality has been
> independently validated*. Every snapshot and diff carries `judge_type`, and
> the diff refuses to run unless both snapshots are `BOOTSTRAP`.
