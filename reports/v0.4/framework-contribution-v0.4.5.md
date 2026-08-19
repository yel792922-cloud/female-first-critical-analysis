# Framework Contribution Decomposition — v0.4.5

Stopped module/cluster ablation. Decomposed contribution with three conditions
on the SAME adversarial prompts: **C0** bare base model, **C1** generic
critical-reasoning scaffold (no gender/feminist content), **C2** full
female-first skill. No SKILL.md change. Bootstrap judge (**LOW independence**)
→ **EXPLORATORY behavioral only; no causal, no scientific-validation claim.**

## A. Experimental conditions
- **C0 bare-base:** `claude -p <prompt>` — no system-prompt append.
- **C1 generic:** `+ GENERIC-SCAFFOLD.md` — evidence discipline, null result,
  aggregate≠instance, agency∥constraint, power mapping, responsibility,
  comparison discipline, baseline interrogation, steelman, minimal sufficiency —
  **zero female-first/gender content.**
- **C2 full-skill:** `+ SKILL.md`.

## B. Cases (pilot)
3 adversarial positives + 1 negative control, chosen to span generic-reasoning
vs female-first-specific properties: A1-P1 (P02 null result, generic), A5-P1
(P08 comparison, generic), A4-P1 (P07 intersectionality-among-women, female-
first-specific), NC-A4 (control). Wording unchanged from the adversarial set.

## C. Property-level results
| Case | Property | C0 bare | C1 generic | C2 full | pattern |
|---|---|---|---|---|---|
| A1-P1 | P02 null result | **PASS** | PASS | PASS | PATTERN1_BASE_SUFFICIENT |
| A5-P1 | P08 comparison | **PASS** | PASS | PASS | PATTERN1_BASE_SUFFICIENT |
| A4-P1 | P07 intersectionality | MISSING | MISSING | PASS | **UNRESOLVED** |
| NC-A4 | P07 (control) | MISSING | PASS | EXECUTION_FAILURE | **UNRESOLVED** |

## D. C0 vs C1
On both resolved properties (P02, P08) **C0 already PASSed**, so C1 could add no
observable behavioral gain — there is **no C0-FAIL→C1-PASS pattern** anywhere in
the resolved set. The generic scaffold's contribution over the bare model is
**not observed** on these cases (the base model already resists the adversarial
pushes).

## E. C1 vs C2
On the resolved properties, C1=C2=PASS (no observable difference). The only
place C2 differs from C1 is **A4-P1 (P07)**: C2=PASS while C1=MISSING — but
MISSING is a judge non-response, **not** a validated C1 failure, so this is
**UNRESOLVED**, not a demonstrated C2>C1 effect.

## F. C0 vs C2
Resolved properties: C0=C2=PASS (base sufficient). A4-P1: C2=PASS, C0=MISSING →
UNRESOLVED. No resolved case shows C2 succeeding where C0 failed.

## G. Negative-control behavior
NC-A4 is **UNRESOLVED** (C2 EXECUTION_FAILURE, C0 MISSING). The intended check —
whether C1/C2 wrongly genderize an irrelevant case — could not be completed this
round (rate limit). No over-genderization evidence either way; recorded as
pending, not as pass.

## H. Base-capability ceiling
**High across all three probed properties.** The bare base model (C0) already
resisted the aggregate→instance leap (P02), the false-symmetry push (P08), **and**
— on qualitative capture — the intersectional flattening (P07), naming the
class/position axis as governing. This is the dominant observation and is
consistent with v0.4.1–4: the target reasoning is largely within *this* strong
base model's capability. (Not a universal claim — see Verdict bounds.)

## I. Generic scaffold effect
**Not observed.** Because C0 already passed the resolved cases, the generic
scaffold produced no measurable increment. (This does not prove a scaffold has no
value in general — only that on these single adversarial cases the base model
already sufficed.)

## J. Female-first-specific candidate effects — **candidate REFUTED**
The A4-P1 (P07) candidate — the one probe most likely to show a female-first-
specific effect — was **qualitatively refuted** on re-capture. The judge's
MISSING on C0/C1 was a **judge failure, not absent reasoning**: the actual C0 and
C1 outputs both surface the intersectional class/position asymmetry and reject
the flattening:
- **C0 bare:** *"不太对…阶级(城乡/雇佣关系)在这里不是可以'别扯太远'的旁枝,而是
  决定她俩关系性质的主轴"* — the bare model refuses "都是女性→同一战线" and names
  the employer/rural-urban axis as governing.
- **C1 generic:** *"这个等同不成立…'阶级那套别扯太远'这句话本身就是在排除对这段
  具体关系最有解释力的那个维度…谁付钱、谁定薪"* — the generic scaffold also refuses
  the flattening and surfaces the asymmetric axis.
So **even the property chosen as most female-first-specific is handled by the
bare model and the generic scaffold.** No female-first-specific behavioral effect
was detected on the tested cases. (Note: a deterministic keyword scan flagged
`accepts_flatten=True` for both — a **false positive**; the text clearly rejects
the flattening. Consistent with the over-genderization-proxy false positives in
v0.4.1, deterministic proxies remain unreliable and require semantic reading.)

## K. Judge limitations
Bootstrap same-family judge, LOW independence. **Systematic MISSING on P07**
(and P04/P06 in prior rounds) is the binding constraint: exactly the female-
first-specific properties most likely to reveal a distinctive effect are the
ones the judge fails to score. No causal or Level-C claim is possible.

## L. Residual confounds
- **Length mismatch:** C1 GENERIC-SCAFFOLD (~5k chars) vs C2 SKILL.md (~44k
  chars). On the resolved cases this did not matter (C0 already passed), but any
  future C1-vs-C2 claim must control it — a longer, structure-matched generic
  scaffold is needed.
- **Same-family judge + skill authored by the same model family** (bootstrap).
- **N=1/property**; single-shot; no failure rates.
- **Rate-limiting** truncated the negative control and the A4 qualitative capture.

## M. Next experiment
1. **Reliable/independent judge** to resolve P07 (and P04/P06) — without it the
   female-first-specific question cannot be answered.
2. **Save model outputs** in the runner (this round's runner stored only states),
   so MISSING cells can be characterized qualitatively without re-running.
3. **Length-matched generic scaffold** for a fair C1-vs-C2 comparison.
4. **Multi-case-per-property** for rates, and completion of the negative control.

## Verdict

**NO DISTINCTIVE EFFECT DETECTED (on the tested cases) — measurement underpowered
for any general claim.**

On all three probed adversarial properties the **bare base model already produced
the target reasoning**: P02 null result and P08 comparison judged base-sufficient,
and P07 intersectionality-among-women **qualitatively base-sufficient** (C0 and C1
both surfaced the class/position asymmetry and rejected the flattening; the judge
MISSING was a judge failure, not absent reasoning). Neither the generic scaffold
(C1) nor the full female-first skill (C2) added an **observable** behavioral gain
on these cases — including the property chosen as most female-first-specific.

Strict bounds on this verdict (it is **not** "no effect exists"):
- **Level A behavioral, N=1/property, single-shot**, bootstrap judge (LOW
  independence) with systematic MISSING — cannot generalize.
- Measures **property satisfaction on single adversarial cases only** — it does
  **not** test the framework's likely loci of value: the female-first *standpoint*
  (a normative/framing commitment, not a judge-scored property), consistency
  across many cases, gendered double-standards, language policy, or edge cases.
- The "base" is a **strong frontier model** that plausibly absorbed critical/
  feminist reasoning in training; base-sufficiency here reflects *this* model, not
  a universal claim.
- The negative control did not complete (rate limit); C1/C2 length is unmatched.

So: **no distinctive female-first-specific or generic-scaffold effect was
detected on the tested adversarial cases**, but the design remains **underpowered
to conclude the framework has no effect in general.** No module is called
redundant; no causal or scientific-validation claim is made. Answering the
central question needs a reliable/independent judge, output-saving runs,
multi-case rates, a length-matched scaffold, and tests of the framework's
normative/standpoint role — which single-property adversarial ablation does not
capture.
