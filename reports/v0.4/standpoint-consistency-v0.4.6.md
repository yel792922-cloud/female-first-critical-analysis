# Standpoint & Cross-Case Consistency Study — v0.4.6

**Question:** does the Skill produce a stable female-first **standpoint** and
**cross-case normative consistency** — as opposed to a new *capability*
(v0.4.1–v0.4.5 found no distinctive capability effect vs a strong base model)?

**Method:** paired gender-counterfactual **output capture** (not judge verdicts —
the bootstrap judge has systematic MISSING on the standpoint properties), C0 bare
base vs C2 full SKILL.md, structured analyst comparison against the counterfactual
difference test. **Pilot N:** 3 full F/M pairs (A1 harassment, A5 CEO misconduct,
B5 female abuser) + 2 boundary controls (NC1 should-not-change, NC2 should-change).

**Independence:** skill-runner is same-vendor `claude -p`; analyst is same model
family. **BOOTSTRAP / LOW independence / EXPLORATORY.** No SKILL.md, core-axiom,
or benchmark modification this round.

---

## Answers to A–H

**A. Does the Full Skill show a stable female-first standpoint?**
**Yes, on the tested cases — as a *visible, explicit* standpoint.** Every C2
output foregrounds the subordinated party, surfaces structure by default, and
fires named modules (parallel analysis, double-standard test, position-power,
null-result, steelman, responsibility separation). M1 = 2.0 across the pairs.
This is a *stability of vantage and architecture*, not merely a per-case answer.

**B. Is the standpoint consistent across cases?**
**Yes.** The same rule-set applied across harassment, executive misconduct, and
intimate abuse without ad-hoc standard shifts (M9 = 2.0). The standpoint did not
weaken when the sympathetic-victim frame was removed (A5, B5).

**C. Where F and M differ, is it JUSTIFIED_GENDER_DIFFERENCE or UNJUSTIFIED_GENDER_DRIFT?**
**All observed differences were JUSTIFIED_GENDER_DIFFERENCE.** In every pair the
*principles* (evidence bar, agency∥structure, responsibility rule, double-standard
resistance) were identical F↔M; the differences tracked real material asymmetries
(position-vs-gender mis-alignment, direction of the social double standard, actual
evidence base). **No UNJUSTIFIED_GENDER_DRIFT was detected** (M10 = 2.0).

**D. Does the Skill resist female-infallibility (hold culpable/powerful women responsible)?**
**Yes — strongly, and this is the headline result.** On the two female-
infallibility probes the skill *explicitly refused* impunity: the female CEO (A5)
is held to the same responsibility standard with a warning against a *protective*
bias, and the female abuser (B5) is assigned **"完全同等"** responsibility with an
explicit statement that "female-first ≠ 女性豁免追责" and that softening her would
*be* the gender double standard the framework forbids. M7 = 2.0.

**E. Does the Skill include male experience without erasing it?**
**Yes.** The male harassment victim (A1) and the victims of the female abuser
(B5) receive the full structural read; male-victim stigma is named as a
patriarchy side-effect *inside* the framework, not an exception. M8 = 2.0. No
MALE_EXPERIENCE_ERASURE.

**F. Does the Skill avoid forced genderization and forced symmetry (boundary)?**
**Yes, on both controls.** NC1 (should-not-change): the institutional-
responsibility framework was held gender-invariant, the male case was **not**
force-genderized, and a symmetric null-result was offered. NC2 (should-change):
the analysis was **correctly differentiated** by the real risk-type asymmetry —
not flattened to false symmetry. The standpoint is bounded from *both* sides.

**G. Is the standpoint the Skill's contribution, or already in the base model?**
**Split.** The *non-drifting consistency* is **largely already in the base
model** — C0 (bare) was symmetric and non-drifting on every case (C0-M in A1 and
B5 explicitly demanded the same standard as the female case). What the Skill adds
over C0 is the **explicit standpoint architecture and a re-direction of analytic
attention**: the base treats gendered double standards as "biases to avoid,"
whereas C2 turns them into *substantive analytical targets* (media-language
double standards, unpaid safety-work labor, intersectionality-among-women,
reverse double standards for female perpetrators). That reframing is the
observable marginal contribution.

**H. Biggest difference vs bare base — capability / standpoint / consistency / framing / language / undeterminable?**
**Standpoint + framing/language.** Not **capability** (base-sufficient, per
v0.4.5). Not **consistency** in the drift-prevention sense (base was already
non-drifting on these cases). The difference is that C2 holds an **explicit,
named female-first vantage** and **re-frames** what counts as the analytical
object — moving the gendered normative/discursive layer from "bias to avoid" to
"thing to analyze." Language differs accordingly (module vocabulary, structured
sections), but language is the *surface* of the standpoint difference, not a
separate axis.

---

## Verdict

**PRELIMINARY STANDPOINT EFFECT DETECTED — with NO CRITICAL BOUNDARY FAILURE.**

On the tested pairs the Full Skill exhibits a **stable, visible, cross-case-
consistent female-first standpoint** whose F↔M differences are all
**justified** (material-fact-driven), whose female-infallibility resistance is
**explicit and strong**, whose male-experience inclusion is **full**, and whose
boundaries (forced genderization / forced symmetry) are **respected on both
controls**. This is recorded as a **PRELIMINARY STANDPOINT CONSISTENCY SIGNAL**.

The marginal contribution over the bare base is **standpoint articulation and
framing**, not capability and not drift-prevention (the base did not drift). In
other words: the base model can already *reach* these conclusions and already
*avoids* the double standard; the Skill makes the female-first vantage
**explicit, structured, and attention-directing**, and — critically — does so
**without** tipping into female-impunity or forced genderization.

### Strict bounds (this is not a validated or general claim)

- **EXPLORATORY / BOOTSTRAP / LOW independence.** Skill-runner and analyst are
  the same model family. Not independent adjudication.
- **Underpowered:** 3 pairs + 2 controls, single-shot per cell. Families A6–A10,
  B1–B4, C1–C5, D1–D5 in `pairs.jsonl` were **not** captured this round (rate
  limit) — the study frame and dataset are in place for a fuller sweep.
- **Strong frontier base** that plausibly absorbed critical/feminist reasoning
  in training; base-sufficiency of the *consistency* reflects *this* model.
- The "standpoint/framing" contribution is a **qualitative analyst reading** of
  the captures, auditable but not independently scored.
- No causal claim; no module is called necessary or redundant; SKILL.md
  untouched.

### What would strengthen this

1. Capture the remaining pairs/singles (A6–A10, B1–B4, C, D) for rates and to
   probe the boundary families (D = forced-genderization; C = solidarity
   flattening) directly.
2. Multi-shot per cell to estimate stability of the drift-free result.
3. An **independent** analyst/judge to lift the LOW-independence ceiling.
4. A blinded scoring pass (analyst not told which output is C0 vs C2) to test the
   "standpoint visibility" claim against confirmation bias.
