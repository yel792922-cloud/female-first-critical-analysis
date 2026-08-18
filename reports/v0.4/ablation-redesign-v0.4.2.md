# Ablation Redesign & Measurement Validity — v0.4.2

Redesigns the ablation measurement after v0.4.1, then pilots it. No SKILL.md /
schema / rubric change. All results **EXPLORATORY / LOW INDEPENDENCE**
(bootstrap same-family judge). **No redundancy claim; no scientific-validation
claim.**

## A. Why the old ablation could not identify contribution
v0.4.1 removed a module and asked a lenient same-family judge on *easy* cases.
Three defects: (1) **capability overlap** — the base model already performs the
reasoning, so removing the *instruction* doesn't remove the *capability*
(demonstrated: A2 ablated still interrogated the baseline); (2) **judge
unreliability** — missing / false-positive verdicts; (3) **N/A vs MISSING
confusion** — a non-response was indistinguishable from "not applicable". So a
null result was uninterpretable.

## B. New Level 1/2/3 framework
- **Level 1 Capability overlap** — removal → no change (full=PASS, ablated=PASS).
  **NOT redundancy.**
- **Level 2 Capability enhancement** — removal → partial/intermittent
  degradation (ablated=PARTIAL, or FAIL on some of a set).
- **Level 3 Capability necessity** — removal → systematic VALIDATED_FAIL;
  restoration recovers it. Strongest contribution evidence.

## C. Diagnostic corpus (28)
21 **capability-challenging** positives (3/module, engineered so the base model
can *plausibly fail without* the module — e.g. A1 aggregate+anecdote leap lure;
A2 user pre-loads "倒退/向下"; A5 surface "各打五十" symmetry lure; A6 agency-/
structure-first framing lock) + 7 **negative controls** (one/module, where the
module is irrelevant). File: `tests/research-protocol/dataset/
ablation-diagnostic.jsonl`.

## D. Pilot (14 designed; 6 executed this round)
Executed under the nested-CLI rate limit: 4 hardest positives (A1-P1, A2-P1,
A5-P1, A6-P2) + 2 negative controls (NC-A1, NC-A6). Remaining 8 of the 14-case
pilot: **execution-pending** (rate limit), recorded, not imputed.

| Case | Type | Prop | full | ablated | effect |
|---|---|---|---|---|---|
| A1-P1 | positive | P02 | PASS | PASS | **LEVEL1_OVERLAP** |
| A2-P1 | positive | P09 | PASS | PASS | **LEVEL1_OVERLAP** |
| A5-P1 | positive | P08 | PASS | PASS | **LEVEL1_OVERLAP** |
| A6-P2 | positive | P05 | PASS | PASS | **LEVEL1_OVERLAP** |
| NC-A1 | negative | P02 | PASS | PASS | **CONTROL_OK** |
| NC-A6 | negative | P04 | PASS | MISSING | **UNRESOLVED** |

## E. State distribution (strict 4-state schema)
- PASS: 9 (of 12 verdicts) · MISSING: 1 (NC-A6 ablated) · VALIDATED_FAIL: 0 ·
  EXECUTION_FAILURE: 0 · N/A: 0.
- **The schema worked as designed.** NC-A6's judge non-response was recorded as
  **MISSING → UNRESOLVED**, *not* laundered into PASS or N/A — exactly the
  discipline v0.4.1 lacked. NC-A1 was **CONTROL_OK** (ablating Null Result did
  not change a well-evidenced case → no over-trigger).

## F. Did we detect a Level 2/3 effect?
**No.** All 4 hardest positives came back **Level 1 overlap** — even the
capability-challenging prompts did not break the ablated skill. Per protocol
§8, this is **not** grounds to declare redundancy. Diagnosis of the null:
1. **Base-model capability ceiling** — the base model + remaining 20 modules
   still produce the target reasoning even on the harder cases.
2. **Ablation strength** — deleting one `##` section from a 44k-char prompt is
   a **weak intervention**; the behavior is over-determined by the rest.
3. **Judge sensitivity** — the bootstrap judge detects gross failure (Level 3)
   but likely misses subtle Level-2 degradation, and still emits MISSING.
4. **Single-shot, N=1/module** — Level 2 is *intermittent*; it needs multiple
   cases per module to surface as a rate, not one case.
5. **Inter-module coverage** — a target property may be jointly supported by
   several modules, so removing one is masked by the others.

## G. Judge limitations
Bootstrap same-family judge: LOW independence; observed MISSING (NC-A6); cannot
support any "validated causal contribution" claim. Level-2 detection in
particular needs a more sensitive and independent judge.

## H. Next experimental design
1. **Stronger intervention** than section-deletion: *adversarial prompting that
   actively pushes the exact failure the module prevents* (e.g. escalating
   multi-turn pressure toward the pattern→instance leap), so the ablated
   condition is genuinely stressed.
2. **Multi-case-per-module** (the full 21) to measure Level-2 as a *failure
   rate*, not a single verdict.
3. **Independent judge or ≥2 human raters** (currently BLOCKED) for any causal
   claim and for Level-2 sensitivity.
4. Multi-turn tests where guardrail modules matter most.

## Verdict

**MEASUREMENT DESIGN NEEDS REVISION.**

Precisely: the **classification schema is validated** — the 4-state schema
(N/A vs MISSING vs EXECUTION_FAILURE vs VALIDATED_FAIL) and the negative-control
framework worked correctly on the pilot (UNRESOLVED for MISSING, CONTROL_OK for
the control), fixing v0.4.1's uninterpretability. But the **measurement
*instrument* — prompt-ablation + bootstrap judge — needs revision**: it did not
produce any Level 2/3 signal even on harder cases, so it cannot yet answer the
causal-contribution question. The next iteration must strengthen the
intervention (adversarial/multi-turn), scale to multi-case-per-module for
Level-2 rates, and obtain an independent judge. **No module is declared
redundant; the null is attributed to instrument power, not module value.**
