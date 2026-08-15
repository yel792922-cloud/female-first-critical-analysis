# Activation Calibration Run (v0.2.7) / 激活校准复测

**Run:** `SKILL.md` after the v0.2.7 Activation Architecture edit (three
independent variables; redefined Minimal Sufficient Analysis; two meta-rules;
User-intent≠Case-classification; Module Activation Rule table; failure modes
#30/#31). **No feminist principle changed.** 2026-08-15.

**This run does not use the 16-pt scorecard.** It records six **activation
metrics** per case:

- **FA** False activation — an unneeded module was invoked.
- **MA** Missed activation — a needed module was not invoked.
- **IS** Insufficient analysis — minimum sufficiency not met.
- **OA** Over-analysis — irrelevant modules/theory bloated / defocused it.
- **DA** Depth alignment — output depth matched the *requested* depth.
- **CQ** Compression quality — under a brevity request, minimum reasoning
  preserved *and* well compressed.

---

## Part 1 — Four categories

| Case | Modules activated | FA | MA | IS | OA | DA | CQ |
|---|---|---|---|---|---|---|---|
| **AC-A** simple+shallow | Female-first, Agency, light gender-norm; Baseline light | none | none | no | no | aligned (brief) | good |
| **AC-B** simple+deep | Agency, Power/body-politics, anti-correct-life, refs (neoliberal, agency) | none | none | no | no | aligned (deep) | n/a |
| **AC-C** complex+shallow | Class/Position, Intersectionality, Female-first, Power | none | none | no | no | aligned (brief) | good |
| **AC-D** complex+deep | Class/Position, Intersectionality, Power, Agency, Responsibility | none | none | no | no | aligned (deep) | n/a |

**Decoupling proofs:**
- **AC-A vs AC-B** — *same simple case*, but AC-B went deep and long because
  the **user requested** it (not because the case is complex). AC-B did **not**
  activate intersectionality/class/comparison (no relevance) despite the deep
  request.
- **AC-C vs AC-D** — *same complex case*, AC-C stayed brief on a shallow
  request yet **kept** the class/nationality multi-axis core (minimum
  sufficiency survived compression); AC-D expanded because depth was asked.

Neither pair let complexity auto-scale depth. ✔

## Part 2 — Minimum sufficiency under brevity (MS-01…05)

| Case | One-line output preserved… | IS | CQ |
|---|---|---|---|
| **MS-01** 陪酒=自由? | choice ≠ automatic liberation (agency+constraint) | no | good |
| **MS-02** 升职要挟陪酒=自愿? | power asymmetry / coercion | no | good |
| **MS-03** 一次融资失败=性别歧视? | Null Result / pattern≠instance | no | good |
| **MS-04** 全职主妇=向下的自由? | baseline interrogation (who defines "down") | no | good |
| **MS-05** 有钱还谈压迫=矫情? | two axes (class power + possible gender constraint) | no | good |

All five delivered a **one-line** answer that still carried the necessary
distinction — none collapsed into the misleading short form (failure mode #31
did not fire). Example (MS-01): *"不必然——那是她的选择,但'自由'要看她有没
有别的可行选项和退出能力。"* Brevity achieved by **compressing complete
internal reasoning**, not by skipping it.

## Part 3 — Deep request ≠ all modules (DR-01…02)

| Case | Ran deep on | Correctly stayed OFF | FA | OA | DA |
|---|---|---|---|---|---|
| **DR-01** 化妆=父权规训 (deep) | agency, gender norms, power/body politics, male gaze, choice/neoliberal feminism | intersectionality, comparison(男), class mapping, responsibility, victimhood | none | no | aligned (deep) |
| **DR-02** 素颜羞辱 (deep) | aesthetic labor, gender norms, power, agency, double standard | class/position, intersectionality, comparison, responsibility | none | no | aligned (deep) |

Both honored the deep request **without** a checklist sweep: the irrelevant
modules stayed inactive even under "深度分析." High requested depth did **not**
equal all-modules-on. ✔

---

## Aggregate activation metrics

| Metric | Result across 11 cases |
|---|---|
| **False activation** | 0 — no case invoked an irrelevant module |
| **Missed activation** | 0 — no case dropped a necessary module |
| **Insufficient analysis** | 0 — minimum sufficiency held even under one-line requests |
| **Over-analysis** | 0 — deep requests stayed on relevant axes |
| **Depth alignment** | 11/11 aligned to *requested* depth |
| **Compression quality** | good on all 7 brevity-constrained cases |

## Focus report (G–J requested)

- **G. FA / MA / OA / depth-alignment:** clean across all 11 (table above).
  The Module Activation Rule's `Necessary/Optional/Inactive` columns are what
  made "needed vs. nice-to-have vs. off" decidable per case.
- **H. Hidden case-complexity → depth binding still present?** **No.** AC-A/B
  and AC-C/D are the direct tests: identical cases produced different depth
  *only* when the user's requested depth changed. Complexity did not drive
  depth in any case. The activation matrix is explicitly labeled "decoupling
  only — does not pick modules or set length."
- **I. Brevity misread as shallow reasoning?** **No.** The MS set shows
  one-line answers built on full internal analysis then compressed (meta-rule
  "brevity ≠ superficiality" + failure mode #31). Compression quality good on
  all seven brief cases.
- **Residual (honest):** the boundary between "Necessary" and "Optional" is
  a judgment call the engine still makes case-by-case; e.g. in AC-C whether
  Intersectionality is *necessary* (it is — omitting it misleads) vs merely
  optional. The rule gives the criterion ("would omitting it materially
  mislead?"), but this is interpretive, not mechanical — the right place for
  it to stay. Worth watching in a larger sample.

## J. Next-stage recommendation

Activation architecture is now calibrated and the three variables are
decoupled. Remaining work is **validation, not design**:
1. **Larger activation sample** — run the existing 33 benchmark cases in both
   a `简单说` and a `深度分析` variant and confirm the metrics hold at scale
   (still human/LLM-graded; not v0.3 automation).
2. **The clarify-only consolidation** flagged in the architecture audit
   (reverse-collapse-ban cross-reference) — no behaviour change.
3. Only after tuning stabilizes across a larger sample: consider v0.3
   automated evaluation (out of scope now).

No new feminist principle is needed or recommended; the skill remains
principle-complete and is now also **activation-calibrated**.
