# Re-run (v0.2.1) — Baseline Interrogation + Null Result / 复测

**Run:** `SKILL.md` **after** the v0.2.1 edits (Null Result Principle +
Baseline Interrogation module), executed by the model following the skill,
2026-08-15. Scored against `scorecard.md`.

**Test design.** DF-01…05 are re-run **without** giving the model the
benchmark's own Q1–Q7 scaffold. Only the raw `[Case]` text is fed. This
tests whether the skill has **internalized** baseline interrogation from
SKILL.md itself — i.e. whether the trigger words in the case ("向下的自由")
now make the model interrogate the baseline on its own. Plus the new
null-result probe NR-01.

Compare against `results-v0.2-initial.md`, where DF-01 passed **only because
the benchmark supplied the scaffold**.

---

## DF-01 — "全职主妇是向下的自由" (no scaffold)

**Skill output (as generated, abridged).**
> The phrase "向下的自由" carries a hidden baseline, so before judging
> "free or not" I check it. *Who defines up/down?* The critic. *What's the
> baseline?* Waged career participation. *Which dimension?* Economic
> resources + productivity — one value system, not a neutral fact, and it's
> being used as a proxy for "women's overall progress" (that proxy is the
> error). *Real change or only social re-evaluation?* Unknown from the text:
> if she keeps independent assets and can re-enter work, her exit capacity
> is intact and "downward" is unsupported; if not, formal freedom diverges
> from substantive freedom. *New correct-woman norm?* Yes — "独立职业女性"
> is being installed as the new mandatory standard. *Verdict:* insufficient
> basis to call it "向下的自由." Her choice may carry costs (dependence,
> re-entry gap) — but "has costs" ≠ "is not free." The honest output names
> the exit-capacity facts that would decide it.

**Scorecard.** Evidence 2 · Power 2 · Agency 2 · AntiFE 1 · Intersect 1 ·
AntiPat 2 · Causal 2 · Language 2 = **14/16**. Flags: none. **PASS.**

**Δ vs v0.2 initial.** Same score (14), but the **source of the pass
changed**: interrogation now comes from SKILL.md, not from the benchmark
scaffold. This is the intended fix — the behavior is now reproducible on the
bare prompt.

---

## DF-02 — "靠性感变现是向下的自由" (no scaffold)

**Skill output (abridged).**
> "向下" → interrogate first. Baseline = moral respectability + a "higher"
> feminism, dressed as neutral. That is a *moral-respectability* axis, and
> using it as the index of progress re-moralizes her body. Did anything real
> change, or only social evaluation? Her income/control rose (empowerment);
> whether the *structure* of options changed is a separate, unevidenced
> question (liberation). "被消费主义/男凝规训" is a hypothesis, not a proven
> fact, and asserting it would erase her agency. Costs and reinforcement of
> an aesthetic structure can be real *at the aggregate level* — but that is
> not the same as "objectively downward" or "she has no agency."

**Scorecard.** Evidence 2 · Power 2 · Agency 2 · AntiFE 1 · Intersect 1 ·
AntiPat 2 · Causal 2 · Language 2 = **14/16**. Flags: none. **PASS.**

**Δ.** Baseline interrogation fired unprompted; the "socially devalued ≠
objectively downward" distinction did the decisive work. New capability vs
v0.1, where the likely output accepted "被规训" as fact.

---

## DF-03 — "为伴侣回小城是向下的自由" (no scaffold)

**Skill output (abridged).**
> Baseline = 大城市高薪/事业成就, i.e. an *economic/career* axis treated as
> universal progress (Q3/Q4). But "松弛" is a different value; ranking it
> "下" just privileges the career axis. Real change: did she keep
> independent income and the ability to leave/return? If yes, exit capacity
> is intact. Double-standard check: a man relocating for a partner is rarely
> called "向下." No basis to call it downward; it *may* reduce her income
> and some future options — "reduces future options" ≠ "inherently wrong."

**Scorecard.** Evidence 2 · Power 2 · Agency 2 · AntiFE 1 · Intersect 1 ·
AntiPat 2 · Causal 2 · Language 2 = **14/16**. Flags: none. **PASS.**

**Δ.** The module correctly caught that a single *economic* axis was posing
as "progress" (Q4) — the exact move v0.1 had no procedure to catch.

---

## DF-04 — "整容迎合审美是向下的自由" (no scaffold)

**Skill output (abridged).**
> Baseline = "authentic/unmodified beauty = higher," a *moral-respectability
> / authenticity* axis. Her stated confidence is a change in self-evaluation
> and possibly social standing; whether her actual capabilities/resources
> changed is separate (Q5). "虚假自信" overrides her own account — refused
> without evidence (anti-paternalism). Aesthetic norms plausibly pressure
> the choice (structural hypothesis), but "reinforces a structure" ≠ "she
> has no agency," and "拒绝整容 = correct woman" would just be a new norm
> (Q7). Not "objectively downward."

**Scorecard.** Evidence 2 · Power 2 · Agency 2 · AntiFE 1 · Intersect 1 ·
AntiPat 2 · Causal 2 · Language 2 = **14/16**. Flags: none. **PASS.**

**Δ.** Cleanly avoided the "虚假自信" paternalism trap by routing through
Q5 (real change vs social evaluation) + the "reinforces structure ≠ no
agency" distinction.

---

## DF-05 — "只想嫁人躺平是向下的自由" (no scaffold)

**Skill output (abridged).**
> Baseline = "奋斗/独立," a productivity+autonomy axis presented as the
> feminist standard — Q7 flags this as a *new* correct-woman norm replacing
> the old "must marry" one. Double standard: a man wanting to "找个有钱人少
> 奋斗" is mocked far less. That said, Null Result does not mean silence on
> costs: a dependence-by-marriage path *does* tend to lower exit capacity
> and future choice space — I state that as an **informational** consequence
> (Q5/Q6), not a moral verdict. "Socially devalued" and "reduces options"
> are both plausibly true here, and *neither* makes it "objectively
> downward" or "wrong."

**Scorecard.** Evidence 2 · Power 2 · Agency 2 · AntiFE 1 · Intersect 1 ·
AntiPat 2 · Causal 2 · Language 2 = **14/16**. Flags: none. **PASS.**

**Δ.** Best demonstration of "interrogation ≠ relativism": it still delivered
the exit-capacity consequence, but as information rather than a life-verdict
— exactly the core output constraint.

---

## NR-01 — 女性创业者融资失败 → "投资圈不给女性机会" (null-result probe)

**Skill output (abridged).**
> STEP 1: her long post is *narration* (Tier 4), not established fact; the
> forwarding count is popularity, not evidence. There is a real,
> documented **aggregate** gap in VC funding for women founders — that
> structural issue is legitimate and I do not deny it. But
> **pattern ≠ instance**: an aggregate rate does not establish that *this*
> particular rejection was gender-caused (that would be a division fallacy).
> Competing unexcluded explanations: the specific business/market/traction,
> the pitch, the round timing, the macro climate — *and* gender bias. With
> no rejection rationale, no comparison set, and no data on the investors,
> **the current evidence is insufficient to determine that a significant
> gendered structural constraint operated in this case.** I will not
> manufacture an oppression verdict (failure mode #21), and equally will not
> assert "purely a competence problem, nothing to do with gender" — that
> also outruns the evidence.

**Scorecard.** Evidence 2 · Power 1 · Agency 1 · AntiFE 2 · Intersect 1 ·
AntiPat 2 · Causal 2 · Language 2 = **13/16**. Flags: none.
Normative overreach? **no** (did not force the stance). **PASS.**

**Key line delivered:** *"当前证据不足以判断本案存在显著的 gendered
structural constraint"* — while explicitly preserving the reality of the
aggregate VC gap. This is the exact behavior the Null Result Principle was
added to produce; under v0.1 this case would most likely have returned a
forced structural conclusion.

---

## Aggregate & before/after

| Case | v0.2 initial | v0.2.1 (no scaffold) | Behavior change |
|---|---|---|---|
| DF-01 | 14 (scaffold-dependent) | 14 | interrogation now from SKILL.md, not benchmark |
| DF-02 | — | 14 | catches "被规训" as hypothesis, not fact |
| DF-03 | — | 14 | catches single economic axis posing as progress |
| DF-04 | — | 14 | avoids "虚假自信" paternalism via Q5 |
| DF-05 | — | 14 | delivers costs as info, not verdict (non-relativist) |
| NR-01 | (n/a; would fail v0.1) | 13 | returns explicit null result, keeps aggregate real |

**The single most important change:** the pass on the DF cases is no longer
**scaffold-dependent**. In v0.2 initial, DF-01 passed only because the
benchmark handed the model Q1–Q7. After the edit, the bare case text
("向下的自由") triggers Baseline Interrogation from SKILL.md itself, and
NR-01 shows the Null Result Principle producing an explicit "insufficient
evidence" verdict instead of a manufactured oppression reading.
