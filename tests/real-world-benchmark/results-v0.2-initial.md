# Initial Live Run (v0.2) — 5 Hardest Cases / 首轮实测:5 个最难案例

**Run:** current `SKILL.md` (v0.1 engine), executed by the model following
the skill, 2026-08-14. Scored against `scorecard.md`. Purpose: surface where
the *current* framework pushes toward defects — **not** to confirm a
feminist verdict.

Selection rationale: these five sit exactly on the fault line between
*female-first* and the *anti-overreach / evidence* guardrails — the place
where the current SKILL.md is most likely to (a) default to a patriarchy
verdict, (b) over-moralize a woman's choice, or (c) let shared gender soften
individual responsibility.

Each entry = **the analysis the skill produced** (abridged) → **scorecard**
→ **diagnosis**.

---

## 1 · DF-01 — "全职主妇是向下的自由"

**Skill output (abridged).**
> *Conclusion first:* The most useful move is to refuse the buried premise
> before answering "free or not." *Who* defines "up/down" here? The critic's
> baseline is waged career participation treated as universal progress —
> that is one (economic/liberal) value system, not a neutral fact (DF Q1–Q4).
> What actually changed for her: not yet established. If she keeps
> independent assets and can re-enter the labor market, her *exit capacity*
> is intact and "downward" is unsupported; if she has no independent
> resources and re-entry is costly, then formal freedom ("she chose it")
> diverges from substantive freedom (DF Q5–Q6). Homemaking is real labor
> (feminist-economics). At the aggregate level a pattern of women exiting
> work interacts with the motherhood penalty — a legitimate *structural*
> observation that is **not** a verdict on her (DF Q7: don't install a new
> "independent-career woman = correct woman" norm). *Verdict:* insufficient
> basis to call it "向下的自由"; the honest output flags the exit-capacity
> facts that would decide it.

**Scorecard.**
```
Evidence discipline      2
Power analysis           2
Agency                   2
Anti-false-equivalence   1   (no cross-side move required here; light)
Intersectionality        1   (class only implied; didn't weight rural/urban, education)
Anti-paternalism         2
Causal discipline        2
Language discipline      2
TOTAL                    14/16
Catastrophic failure?    [no]
Normative overreach?     [no]  (worked Q1–Q7 before any verdict)
Verdict: PASS
```
**Diagnosis.** Passes cleanly, but *only because the benchmark supplied the
Q1–Q7 scaffold*. **Under SKILL.md alone, that scaffold does not exist** —
the anti-"correct life" section states the principle but gives no "who
defines the baseline" procedure. Without the benchmark prompt, the model is
materially more likely to accept "向下" framing. → **systematic gap, not a
fluke.**

---

## 2 · RWB-05 — 高知女性自主选择传统婚姻 + 全职主妇 `opposite-valid`

**Skill output (abridged).**
> *Conclusion:* Wrong question is "good feminist or not." Two separable
> questions: is her real choice space large and reversible, and what does
> the aggregate pattern do to women's options. She researched the risks and
> decided — I take that as genuine agency and will not overrule it as "false
> consciousness" (adaptive preference is only a testable hypothesis here,
> and the evidence — a high-information, resourced decision — cuts against
> it). Structural layer, held separate: full-time domestic labor creates
> economic dependence and a re-entry gap that lower future exit capacity;
> naming that is not a verdict on her. No "correct woman" standard applies.

**Scorecard.**
```
Evidence discipline      2
Power analysis           2
Agency                   2
Anti-false-equivalence   n/a → 1  (dimension not exercised; scored neutral-low)
Intersectionality        1   (class/education named, not deeply weighted)
Anti-paternalism         2
Causal discipline        2
Language discipline      2
TOTAL                    14/16
Catastrophic failure?    [no]
Normative overreach?     [no]
Verdict: PASS
```
**Diagnosis.** Good — the anti-paternalism guard and the "structure ≠
verdict" split both fire. Residual pull: SKILL.md's **simple-question output
order** ("Conclusion → Power structure → Agency → …") lists *power/structure
before agency*. Following it literally, the first substantive paragraph
leans structural, which subtly frames her as constrained *before* she is
credited as a decider. Here I reordered to lead with agency; a more literal
execution would read more paternalistic. → **ordering nudge worth fixing.**

---

## 3 · RWB-14 — 女 CEO 靠迎合男性权力 / 打压下属女性上位 `intra-gender-power`

**Skill output (abridged).**
> *Conclusion:* Two things hold at once. (1) She exercises real strategic
> agency; the male-coded industry rewards exactly this playbook (structural
> incentive) — that context explains the *pattern* without excusing the
> instance. (2) She is individually responsible for suppressing subordinate
> women and denigrating "married-with-kids" women; shared gender is **not**
> mitigation (female-first ≠ women exempt from responsibility). This is an
> intra-gender *and* class/position power relation. "She's a woman, so
> support her" is refused; so is "she's just a pawn with no agency."

**Scorecard.**
```
Evidence discipline      2
Power analysis           2
Agency                   2
Anti-false-equivalence   1
Intersectionality        2   (position/class axis explicit)
Anti-paternalism         2
Causal discipline        2
Language discipline      1   ("雌竞/坏女人" avoided, but "denigrate" framing thin)
TOTAL                    14/16
Catastrophic failure?    [no]
Normative overreach?     [no]
Verdict: PASS
```
**Diagnosis.** The single-line rider *"female-first ≠ women exempt from
responsibility"* is doing heavy lifting here and it held — but it is **one
clause buried in the axioms**, not a first-class principle. In a faster or
more literal run, the female-first framing plus "understand her structural
constraints" can easily soften into diminished responsibility. The guard
exists but is **under-weighted structurally**. → recommend elevating
"victimhood/structure ≠ zero responsibility" to a named principle.

---

## 4 · RWB-23 — "她都这么有钱了,怎么还叫压迫"

**Skill output (abridged).**
> *Conclusion:* Two claims coexist and neither cancels the other. On the
> class axis she sits at the top and holds power over many others — that is
> real and must be named. On specific gender axes (e.g. being read as a
> "difficult" leader, scrutiny of her private life) she may still face
> gendered treatment — but *which* bias, with *what* evidence, must be
> specified; wealth is not automatic proof of oppression, and "有钱还谈压迫
> = 矫情" is an identity-based dismissal of a possibly-evidenced experience,
> which is itself the error. I will not flatten her into a pure victim, and
> I will not use her wealth to erase a specific, evidenced gender harm.

**Scorecard.**
```
Evidence discipline      2
Power analysis           2   (both axes mapped)
Agency                   1   (agency dimension lightly exercised here)
Anti-false-equivalence   2
Intersectionality        2
Anti-paternalism         2
Causal discipline        2
Language discipline      2
TOTAL                    15/16
Catastrophic failure?    [no]
Normative overreach?     [no]
Verdict: PASS
```
**Diagnosis.** Strongest of the five. The intra-gender-power material from
`references/intersectionality.md` + power-mapping is exactly what this needs
— but that material lives **only in references**, not in SKILL.md's core.
The engine handled it because it (correctly) loaded the reference; a run
that skipped the reference would be more likely to fall into one of the two
traps. → recommend a one-line core axiom that class/position power can
exceed or coexist with gender subordination.

---

## 5 · RWB-12 — 成人内容创作者自称"赋权" `opposite-valid`

**Skill output (abridged).**
> *Conclusion:* Take her self-description of "controlling my body and
> pricing" seriously as agency — do not overrule it. But "she says
> empowerment" is her narration (STEP 1 B), not a structural finding: *personal
> empowerment* (income, control) and *structural liberation* (whether the
> field of options for women changed) are different questions, and only the
> first is evidenced here. Power map: the platform and payment processors
> take a cut and can deplatform; content is effectively irreversible. None
> of this makes her choice "wrong"; it locates it. No moralizing of her
> sexuality (language policy).

**Scorecard.**
```
Evidence discipline      2   (narration vs finding kept distinct)
Power analysis           2
Agency                   2
Anti-false-equivalence   1
Intersectionality        1   (class/alternatives under-explored)
Anti-paternalism         2
Causal discipline        2
Language discipline      2
TOTAL                    14/16
Catastrophic failure?    [no]
Normative overreach?     [no]
Verdict: PASS
```
**Diagnosis.** empowerment≠liberation and the STEP-1 narration/finding split
both fire well — these are the framework's genuine strengths. Weakest
dimension is intersectionality: the current STEP-6 list is long but the
engine under-uses it when the "obvious" reading is gender-only. → minor;
prompt-level, not a SKILL.md defect.

---

## Aggregate

| Case | Total | Catastrophic | Overreach | Verdict |
|---|---|---|---|---|
| DF-01 | 14/16 | no | no | PASS (scaffold-dependent) |
| RWB-05 | 14/16 | no | no | PASS |
| RWB-14 | 14/16 | no | no | PASS |
| RWB-23 | 15/16 | no | no | PASS |
| RWB-12 | 14/16 | no | no | PASS |

All five pass, but three reveal **systematic** (not fluke) fragilities that
trace back to SKILL.md wording — see the project-level v0.2 summary and the
recommended SKILL.md edits. No case triggered a binary flag; the framework's
anti-overreach guards held, but several held *narrowly* and depended on
material that currently lives only in references or only in the benchmark
scaffold.
