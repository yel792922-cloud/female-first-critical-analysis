# Experimental Execution — v0.4.1

Executed the defined v0.4 experiments under the nested-CLI rate limit
(paced + backoff + resumable). No SKILL.md / schema / rubric change. Judge is
**BOOTSTRAP (LOW independence)** throughout — this is behavior evidence, not
independent validation, and **not** scientific validation.

## A. Sample counts
| Sweep | Executed | Design target |
|---|---|---|
| Ablation (diagonal pilot) | **7 pairs** (A1–A7 × 1 diagnostic case each) | full 58×7 = 406 |
| OOD generalization | **8 cases** (5 non-feminist-power + 3 male-subject) | 20 |
| Female-first boundary | **5/5** controls | 5 |
| Baseline reused (immutable) | 58 | — |
| Human annotation | **0 human raters** | ≥2 |

## B. Completed / pending
- **Completed:** ablation diagonal (7/7), OOD pilot (8), boundary (5/5) = **20
  new judged cases**.
- **Pending:** full ablation (58×7), remaining 12 OOD, human annotation.

## C. Rate-limit incidents
Sustained nested `claude -p` calls throttle after bursts (earlier round: 1/8
succeeded). Mitigated by 12s pacing + backoff-retry + resumable checkpoints;
the sweeps then completed, but slowly. This bounded scope to pilots — **recorded,
not used to silently shrink claims.**

## D. Ablation findings
**No detected critical regression on any of the 7 pairs** (target property
stayed PASS, or the judge did not score it). **This is NOT "modules are
redundant."** Two confounds make the pilot underpowered:
1. **Base-model-capability confound (demonstrated).** A2 removed the Baseline
   Interrogation module, yet the ablated output *still* interrogated the "向下"
   baseline in depth ("'向下'预设了一条隐藏的价值轴…这条价值轴是谁定的?").
   Prompt-ablation removes the *instruction*, not the base model's *capability*
   — so easy cases can't isolate a module's marginal contribution.
2. **Bootstrap-judge unreliability (demonstrated).** A2 flagged a false-positive
   **E13** (the output explicitly warns against the aggregate→individual leap);
   A3 never scored the requested **P06** (returned P02 instead).

**Conclusion: INSUFFICIENT SAMPLE + confounded design → no causal-contribution
or redundancy claim.** The modules' intended value (stability/guardrails under
adversarial pressure) is exactly what an N=1 easy-case + lenient same-family
judge does **not** stress.

## E. OOD generalization findings
- **Rigor fires without feminist vocabulary:** all property verdicts PASS
  across the 8 OOD cases (evidence/agency/power/responsibility/comparison/
  causal). Female-first does **not** gate rigorous reasoning to women's topics.
- **Over-genderization proxy is false-positive-prone.** It flagged 3
  non-gender-power cases, but semantic inspection of the heaviest (G-A5, advisor
  power, 21 gender-term hits) shows the skill explicitly frames it as *"an
  institutional-power problem, NOT a gender problem"* and offers gender only as
  an optional add-on — **correct non-genderization**, not over-reach. The proxy
  counts the skill's own meta-discussion of *setting gender aside*.

## F. Boundary findings (the direct female-first-boundary test)
**5/5 clean.** All property verdicts PASS; over-genderization flag False on all
five including both non-gender-power controls. Inspected outputs are exemplary:
- **BND-3 (F + non-gender power):** *"还不足以支持'这是性别压迫案例'的结论——
  这正是零结果原则要防的坑:女性本位是分析视角,不是必然结论。"*
- **BND-4 (M + non-gender power):** *"核心矛盾不是性别结构,而是平台资本/算法
  权力对零工劳动者…'男性'这个变量解释力很弱…真正值得深入的轴是阶级/位置权
  力"* — refuses both "父权压迫" and "男性也是受害者所以性别分析作废".
No gender overreach, no female invisibility, no male-experience erasure, no
forced asymmetry/symmetry observed on these 5 controls.

## G. Human annotation status
**HUMAN_ANNOTATION_BLOCKED** — 0 human annotators available in this environment.
Not substituted with an LLM and declared complete; recorded as blocked.

## H. Critical regressions
**None detected** (ablation pilot). Given the confounds (D), absence of
detection is *not* evidence of absence of contribution.

## I. Unexpected findings
1. **Prompt-ablation does not isolate module contribution** for a capable base
   model (D1) — a methodological limit of the whole ablation approach.
2. **Bootstrap judge emits missing / false-positive verdicts** (D2) — reliability
   ceiling of same-family judging.
3. **The over-genderization deterministic proxy is unreliable** (E) — it must be
   paired with semantic inspection.

## J. Hypotheses vs observed results
- Predicted per-module critical regressions (v0.4 ablation-report): **not
  observed** — but underpowered + confounded, so they remain **untested
  hypotheses, not refuted.**
- Generalization hypothesis (rigor survives without feminist vocab): **observed
  positively** on the pilot (bootstrap-caveated).
- Boundary hypothesis (female-first = standpoint, no over-genderization):
  **observed positively** on all 5 controls (bootstrap-caveated).

## K. External blockers
- nested-CLI **rate limit** → full ablation / full OOD execution-pending.
- **no independent judge** → all evidence BOOTSTRAP / LOW independence; no
  independent validation.
- **no human annotators** → inter-rater agreement blocked.

## L. Next experiment
1. **Redesign ablation for power:** independent judge + **harder/adversarial
   cases** (where the base model fails *without* the module) + multiple cases
   per module — the only way to actually isolate contribution past the
   base-model confound.
2. Full 20-case OOD + full 58×7 ablation once rate-limit headroom exists.
3. Recruit ≥2 human annotators for inter-rater agreement.

## Verdict

**EXPERIMENTAL SWEEP PARTIALLY COMPLETE.**

The pilot experiments (20 new judged cases across ablation, OOD, boundary) ran
end-to-end and produced two positive, bootstrap-caveated generalization
findings (rigor generalizes; female-first stays a standpoint without
over-genderization) and one important **negative methodological** finding
(prompt-ablation + same-family judge cannot measure module causal contribution
on easy cases). Full sweeps + independent-judge + human-annotation remain
**pending / blocked** — recorded honestly, never written as PASS, and no
scientific-validation claim is made.
