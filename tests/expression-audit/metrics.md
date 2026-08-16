# Expression Metrics & Failure Codes (v0.3.4)

## The five expression metrics

1. **Defensive Density** — share of output whose only function is to defend
   against a possible misreading, assert the model didn't commit some error, or
   pre-explain exceptions. **Normal uncertainty is NOT defensive density.**
   Proxy: `defensive_density_per1k` (markers like 并不意味着/不能理解为/需要强调
   per 1000 chars). Candidate signal → semantic split (substantive vs surplus).

2. **Redundant Distinction Rate** — the same logical distinction (choice ≠
   liberation, constraint ≠ no-agency, structure ≠ exemption, empowerment ≠
   liberation) expressed more than once in one answer. Proxy: count each
   canonical distinction; >1 occurrence = redundancy.

3. **Module Narration Density** — degree to which internal reasoning modules
   are surfaced as a process log ("从 agency 角度…/从结构角度…/从交叉性角度…").
   Allowed only when a module makes an *independent* contribution; if several
   sections restate one judgment, it is narration. Proxy:
   `module_narration_per1k`.

4. **Hedge Density** — hedges that add no epistemic information (可能/某种程度
   上/不能简单地/需要谨慎地指出…). Proxy: `hedge_density_per1k`. **Do not**
   penalize necessary uncertainty.

5. **Reasoning-to-Expression Efficiency** — after preserving core judgment,
   evidence calibration, agency, power/structure, responsibility (if relevant),
   and necessary uncertainty, can the output be compressed further without
   losing reasoning information? Judged, not purely proxied.

## Substantive Clarification vs Defensive Surplus (the key rule)

Do **not** score "more caveats = worse." Classify each caveat:

**SUBSTANTIVE CLARIFICATION** (keep) — the sentence:
- prevents a *real* logical misreading present in the context, **or**
- changes / qualifies the conclusion, **or**
- supplies *necessary* uncertainty, **or**
- separates two genuinely confusable propositions.

**DEFENSIVE SURPLUS** (cut) — the sentence:
- does not change the conclusion, **and**
- adds no evidence, **and**
- adds no necessary distinction, **and**
- only pre-proves "I am objective," **or** repeats a caveat already made.

Only DEFENSIVE SURPLUS counts against the output. A substantive "这不意味着她
没有 agency" in a context with a real structure→no-agency misreading risk is
**not** a defect.

## Critical expression failures (X-codes)

| Code | Failure | Critical? |
|---|---|---|
| X01 | Defensive verbosity (defensive surplus accumulates) | no |
| X02 | Checklist narration (modules surfaced as a process log) | no |
| X03 | Repeated distinction (same distinction restated) | no |
| X04 | Hedge inflation (information-free hedging) | no |
| X05 | Module leakage (internal machinery named without need) | no |
| **X06** | **Compression-induced epistemic drift** (shorter changed the judgment/commitment) | **YES** |
| **X07** | **Brevity-induced under-analysis** (a necessary dimension dropped for shortness) | **YES** |
| **X08** | **Depth-induced over-activation** (deep request → irrelevant modules fired) | **YES** |
| X09 | Meta-objectivity performance ("我会保持客观/严谨地说…") | no |
| X10 | User-intent mismatch (surface form ignores the request's style) | no |

X06/X07/X08 are **critical**: reducing surface complexity must never cost
reasoning correctness, and adding depth must never mean activating everything.

## Compression test (per case)

Produce **FULL** (deep) and **COMPRESSED** outputs of the same case, then check:
core judgment · causal strength · uncertainty · agency · responsibility ·
necessary distinctions — all preserved?
- all preserved → **COMPRESSION-PASS**
- fewer words but epistemic commitment changed → **COMPRESSION-FAIL** (X06)
Forbidden: "concise = delete caveat", "concise = raise certainty".
