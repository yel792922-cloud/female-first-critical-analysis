# Ablation Measurement Protocol (v0.4.2)

Redesign after v0.4.1 found that prompt-ablation on easy cases could not
isolate module contribution (the base model already had the capability, and the
same-family judge was unreliable). This protocol adds an effect-level framework,
capability-challenging case design, negative controls, and a strict state
schema. **It changes no SKILL.md rule.** All results are **EXPLORATORY / LOW
INDEPENDENCE** until an independent judge or ≥2 human raters exist.

## 1. Three effect levels

| Level | Meaning | Ablation signature |
|---|---|---|
| **Level 1 — Capability overlap** | base model already has the capability; the module is not the sole source | removing the module → **no behavior change** (full=PASS, ablated=PASS). **Does NOT prove redundancy.** |
| **Level 2 — Capability enhancement** | module improves consistency / robustness / error-resistance; base model *sometimes* succeeds alone | removing → **partial / intermittent degradation** (ablated=PARTIAL, or FAIL on some cases of a set) |
| **Level 3 — Capability necessity** | removing the module produces a **systematic, predictable failure**; adding it restores | full=PASS, ablated=**VALIDATED_FAIL** across the module's diagnostic set |

Level 3 is the strongest contribution evidence. Level 1 alone is **not**
grounds to call a module redundant (it may be Level 2/3 on harder cases, or
carry load only under adversarial pressure).

## 2. Capability-challenging case design

A diagnostic case must be one the base model can **plausibly get wrong without
the module** — not one it answers correctly by default. Per module:

- **A1 Null Result** — aggregate pattern + a vivid plausible anecdote + a
  leading detail, engineered to tempt a pattern→instance leap.
- **A2 Baseline Interrogation** — the *user* pre-loads the ranking ("倒退/向下/
  堕落"); the model must actively unpack the baseline or the conclusion is
  pre-decided.
- **A3 Responsibility** — a subject who is a structural victim *and* an actual
  perpetrator, so the explanation↔blame separation is under load.
- **A4 Intersectionality** — two same-gender subjects with sharp class/position/
  migration asymmetry, with a "都是女人" flattening lure.
- **A5 Comparison** — surface "both harmed" where power/scale/mechanism are
  asymmetric, with a "各打五十" symmetry lure.
- **A6 Parallel Analysis** — agency-first *or* structure-first framing designed
  to induce framing lock (choice→freedom, or structure→no-agency).
- **A7 Class/Position** — one subject subordinate on gender *and* dominant on
  class/institution, to induce single-axis collapse.

**≥3 positive diagnostic cases per module** (21 total), all in
`dataset/ablation-diagnostic.jsonl`.

## 3. Negative controls

Each module has ≥1 **negative control**: a case where the module is *irrelevant*
(no ranking language for A2, well-evidenced facts for A1, a pure definition for
A6, etc.). Ablating that module must **not** change behavior on the control.
- **CONTROL_OK** — full == ablated (module does not over-trigger).
- **CONTROL_OVERTRIGGER** — ablating changes an unrelated case (module was
  firing where it should be inactive) — itself a finding.

7 controls (one per module) in the dataset. Minimum corpus: 21 + 7 = **28**.

## 4. Strict state schema (never conflate)

Per (case, condition) the target-property verdict is exactly one of:
- **N/A** — property genuinely not applicable (judge returned N-A).
- **MISSING** — judge returned no verdict for the target property.
- **EXECUTION_FAILURE** — model/adapter/runner call failed.
- **VALIDATED_FAIL** — property actually FAIL.
- **PASS / PARTIAL** — held / partially held.

**Forbidden:** MISSING→PASS, MISSING→N/A, EXECUTION_FAILURE→anything-but-failure.
UNRESOLVED (any MISSING/EXECUTION_FAILURE in a pair) is reported as such, never
imputed.

## 5. Judge requirement
No causal-contribution claim may rest on the bootstrap same-family judge alone.
Without an independent judge or ≥2 human raters, the experiment may run but its
conclusions are labeled **EXPLORATORY / LOW INDEPENDENCE**; the phrase
"validated causal contribution" is not used.

## 6. Pilot-first
Run 1 hardest positive per module + the negative controls (≤14) before any full
sweep, to confirm the protocol can *produce* differentiated Level 1/2/3 patterns
at all. If the pilot still shows uniform no-difference, diagnose (base-model
ceiling · case difficulty · ablation strength · judge sensitivity · property
design · inter-module coverage) before scaling — **do not** declare redundancy.
