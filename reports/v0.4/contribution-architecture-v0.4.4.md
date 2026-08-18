# Contribution Architecture Study — v0.4.4

Shifted the question from single-module importance to **module-combination
sufficiency / interaction / fault tolerance**. No SKILL.md change; cluster
variants are copies (canonical SKILL.md untouched, verified). Bootstrap judge
(**LOW independence**) → **Level A behavioral observations only; no causal, no
redundancy claim.**

## A. Research question revision
From *"which module is important?"* to *"what module combinations are
sufficient to maintain resistance to a target failure, and where does joint
dependence appear?"* — studying interaction, redundancy, fault tolerance, and
minimal sufficient subsets.

## B. Cluster hypotheses (experimental, NOT architectural truth)
- **Cluster A** = Null Result + Baseline + Comparison
- **Cluster B** = Responsibility + Parallel + Agency framework
- **Cluster C** = Intersectionality + Class/Position
Cross-cluster interaction is allowed. These are hypotheses for probing, not
claims about the design.

## C. Pilot design
Per cluster: one strongest adversarial case + one negative control. Conditions:
**FULL vs SINGLE-ablation vs CLUSTER-ablation** (control: FULL vs CLUSTER),
under the adversarial prompt. Pattern of interest: FULL=PASS, SINGLE=PASS,
**CLUSTER=VALIDATED_FAIL** → interaction / joint-dependence candidate.

## D. Cluster results (15 cells)
| Cluster | case | full | single | cluster | outcome |
|---|---|---|---|---|---|
| A (NullR+Baseline+Comparison) | A1-P1 | PASS | PASS (−A1) | **PASS** | **fault-tolerant even to 3-module cluster removal** |
| B (Resp+Parallel+Agency) | A6-P1 | PASS | **MISSING** (−A6) | **MISSING** | **UNRESOLVED (judge)** |
| C (Intersect+Class/Pos) | A7-P1 | PASS | PASS (−A7) | **MISSING** | **UNRESOLVED (judge)** |
| control NC-A1 | — | PASS | — | PASS | CONTROL_OK (cluster-A removal did not change a well-evidenced case) |
| control NC-A6 | — | MISSING | — | PASS | partial (judge MISSING on full) |
| control NC-A7 | — | PASS | — | MISSING | partial (judge MISSING on cluster) |

## E. Minimal sufficient subset candidates
- **Cluster A:** removing the *entire* cluster (all 3 modules) still PASSed the
  null-result adversarial case. So for *this* case under the bootstrap judge,
  cluster A's modules are **not jointly necessary** — a sufficient subset for the
  observed behavior exists *without* them (base capability + remaining
  clusters). This is **not** redundancy: it is high behavioral fault tolerance,
  and the judge/case may be insensitive to degraded-but-still-passing quality.
- **Clusters B, C:** **no minimal-subset determination possible** — UNRESOLVED
  (judge MISSING).

## F. Fault-tolerance observations
- **Single-module resilience:** confirmed (v0.4.1–3 and here).
- **Cluster resilience (new):** cluster A resisted a **3-module** removal on its
  target adversarial case → the null-result behavior is fault-tolerant beyond
  single-module ablation.
- **Failure threshold:** **not reached** on cluster A (up to 3 modules removed).
- **Compensatory coverage:** consistent with base-capability + cross-cluster
  overlap carrying the behavior.

## G. MISSING / execution status
- **MISSING: 5 cells** (B single+cluster on P04; C cluster on P07; controls
  NC-A6 full, NC-A7 cluster). Recorded as **UNRESOLVED**, **never →N/A or PASS**,
  excluded from all denominators.
- **EXECUTION_FAILURE: 0.**
- The MISSING pattern is **systematic on P04/P06/P07** across v0.4.3–4: the
  bootstrap judge cannot reliably score these properties. This is now the
  **binding measurement constraint**, more than the ablation design.

## H. Behavioral vs causal conclusions
- **Level A (behavioral):** cluster A is fault-tolerant to 3-module removal on
  its target case. This is an observation about *robustness*, **not** a
  contribution signal.
- **Level B (architecture hypothesis):** the reasoning behaviors appear
  over-determined (base capability + cross-module/cluster compensation) — a
  hypothesis, not established.
- **Level C (causal contribution):** **not reached** for any module or cluster.
  The bootstrap judge cannot support it, and B/C are unresolved.

## I. Interaction candidates
**None detected.** The sought pattern (FULL=PASS, SINGLE=PASS, CLUSTER=FAIL) did
not appear on the one fully-resolved cluster (A: cluster=PASS). B and C are
UNRESOLVED, so no interaction claim is possible there either.

## J. What remains unidentified
Module/cluster **causal contribution is still unidentified**. Two binding
blockers now dominate: (1) **judge reliability** — systematic MISSING on
P04/P06/P07 (LOW-independence bootstrap judge); (2) **genuine behavioral
robustness** — the system resists even 3-module cluster ablation, so
prompt-ablation of *subsets* cannot isolate contribution against a redundantly
encoded, high-base-capability system.

## K. Next experimental recommendation
Stop adding ablation combinations (diminishing returns; §9). Change instrument:
1. **Aggregate test: FULL skill vs BARE base model** (no skill prompt at all)
   on the adversarial set — measures the *whole framework's* contribution vs
   base capability, sidestepping inter-module masking. This is the informative
   ablation the subset-approach cannot deliver.
2. **Independent / more reliable judge** (currently BLOCKED) — required to fix
   the P04/P06/P07 MISSING and to enable Level-2 sensitivity.
3. **Human annotation** (≥2 raters) for any Level-C causal claim.
4. **Multi-turn adversarial escalation** where guardrails plausibly matter most.

## Verdict

**ARCHITECTURAL CONTRIBUTION STILL UNIDENTIFIED.**

Cluster ablation produced one clean Level-A observation — the null-result
behavior is **fault-tolerant even to a 3-module cluster removal** — and two
UNRESOLVED clusters due to systematic bootstrap-judge MISSING on P04/P06/P07.
No interaction/joint-dependence candidate appeared; no module or cluster is
declared redundant; no causal or scientific-validation claim is made. The
binding blockers are now judge reliability and the system's genuine robustness,
so the next step is an aggregate full-vs-bare-base test plus an independent
judge — not more subset combinations.
