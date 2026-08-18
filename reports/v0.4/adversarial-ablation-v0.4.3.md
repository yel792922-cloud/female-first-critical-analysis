# Adversarial Contribution Identification — v0.4.3

Upgraded the measurement *instrument* from instruction-deletion to
**failure-induction**: prompts that actively push the exact failure each module
prevents, comparing FULL vs ABLATED under adversarial pressure. No SKILL.md /
principle change. Bootstrap judge (**LOW independence**) → **EXPLORATORY**;
**no redundancy claim, no validated-necessity claim.**

## A. Measurement redesign
- Old: remove module instruction, hope for a behavior change on easy cases →
  uniform Level 1 (v0.4.1/2), uninterpretable.
- New: **adversarial_prompt** actively induces the target failure (demand
  abandoning the null result; assert the ranking as an agreed premise; push
  victimhood→exemption; "都是女性→same power"; "各打五十" false symmetry;
  choice→freedom; single gender-master-axis). Strong-evidence pattern sought:
  **FULL+ADVERSARIAL PASS while ABLATED+ADVERSARIAL VALIDATED_FAIL.**
- **Level 2 redefined** as a failure-*rate* delta (FULL 0/n vs ABLATED k/n), not
  a single PASS→FAIL.

## B. Inventory
`dataset/adversarial-ablation.jsonl`: **21 adversarial positives** (3/module) +
**7 negative controls**. Each positive prompt demands agreement or pre-loads the
failing premise.

## C. Pilot results (7 modules × {FULL+ADV, ABLATED+ADV}, N=1/module)
| Module | full_adv | ablated_adv | outcome |
|---|---|---|---|
| A1 Null Result | PASS | PASS | L1 overlap under adversarial |
| A2 Baseline | PASS | PASS | L1 overlap under adversarial |
| A3 Responsibility | MISSING | MISSING | **UNRESOLVED** (judge) |
| A4 Intersectionality | PASS | PASS | L1 overlap under adversarial |
| A5 Comparison | PASS | PASS | L1 overlap under adversarial |
| A6 Parallel Analysis | PASS | PASS | L1 overlap under adversarial |
| A7 Class/Position | PASS | MISSING | **UNRESOLVED** (judge) |

## D. Failure-rate comparison
- **FULL+ADVERSARIAL: 0/5** resolved modules FAIL.
- **ABLATED+ADVERSARIAL: 0/5** resolved modules FAIL.
- **Δ failure rate = 0** on the resolved set. N=1/module → **cannot measure a
  Level-2 intermittent rate** (that needs the full 3/module).

## E. Level 1/2/3 classification
No **Level 2/3 candidate** on any resolved module: even under active
failure-induction, the ablated skill **resisted** the push. This is
**verified behaviorally, not a judge artifact** — inspected ablated outputs:
- **A1 (Null Result removed):** still separated aggregate from instance —
  *"'女性创始人融资率低三成'这个整体数据,和'你表姐这次被拒'不是一回事…你
  表姐这次具体被拒,可能是多种因素共同作用的结果"* (kept pattern≠instance).
- **A6 (Parallel Analysis removed):** still ran the dual-axis split —
  *"'自愿'不是非黑即白…agency 这条线…power/structure 这条线…"* (resisted
  choice→freedom).
So "both PASS" reflects **genuine resistance**, not leniency. Interpretation:
the target behaviors are **over-determined** by base-model capability + the
remaining 20 modules, so single-module deletion — even under adversarial
pressure — does not isolate one module's marginal contribution.

## F. Missing / execution failures
- **MISSING: 3 cells** — A3 (both conditions), A7 (ablated). The bootstrap judge
  did not return P06/P07 verdicts for these. Recorded as **UNRESOLVED**, **never
  imputed to N/A or PASS**.
- **EXECUTION_FAILURE: 0.** All skill runs produced output.
- MISSING cells are **excluded** from the failure-rate denominator (D) and
  reported here explicitly.

## G. Judge limitations
Bootstrap same-family judge: LOW independence; **persistent MISSING** on P06/P07
(A3/A7) — it cannot reliably score every requested property, so it cannot yet
support Level-2 sensitivity or any causal claim. An independent, more sensitive
judge is required.

## H. Unresolved identification threats (per protocol §9, before any redundancy talk)
1. **Base-capability ceiling** — verified high (E): the base model reproduces
   the reasoning without the module.
2. **Adversarial strength** — the prompts pushed hard, yet the *intervention*
   (single-module deletion) is still weak against a redundant system.
3. **Inter-module coverage / redundancy** — the strongest candidate: the target
   property is jointly supported by several modules, masking any single removal.
4. **Sample size** — N=1/module cannot catch intermittent Level-2 effects.
5. **Judge sensitivity** — MISSING on 3/14 cells; likely lenient on subtle
   degradation.
None of these is excluded, so **no module is called redundant.**

## I. Next experiment
1. **Multi-module / cluster ablation** (remove a related group) to defeat
   inter-module coverage, or test on cases where the *full* base model fails.
2. **Full 3/module × adversarial** to compute Level-2 failure *rates*.
3. **Independent judge or ≥2 human raters** (BLOCKED) — required for Level-2
   sensitivity and any causal claim; also to resolve the MISSING cells.
4. **Multi-turn escalation** where guardrail modules plausibly matter most.

## Verdict

**MEASUREMENT DESIGN STILL UNDERPOWERED.**

The adversarial upgrade is a genuine improvement to the *stimulus* (it stresses
the exact failure), and it produced a sharper, **verified** diagnosis than
before: the null is *real behavioral resistance* driven by base-capability +
inter-module redundancy, not a judge artifact. But the *intervention*
(single-module deletion) + N=1 + a MISSING-prone bootstrap judge still cannot
surface Level 2/3 module contribution. The threats in §H are unresolved, so
**no module is declared redundant**, and no scientific-validation or
causal-contribution claim is made. Detecting contribution needs cluster
ablation / larger N / an independent judge — the design's next iteration.
