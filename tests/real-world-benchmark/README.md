# Real-World Benchmark (v0.2) / 真实语境基准测试

## Purpose / 目的

v0.1 tested the framework against abstract adversarial prompts. v0.2 tests
whether the skill can **stably execute its own stated principles** when
facing the messy, high-heat gender debates that actually circulate on the
Chinese internet — *without* collapsing those principles into a fixed
ideological stance.

The benchmark validates one thing above all:

> Can the skill keep **women as the primary analytical subject** while
> **simultaneously** holding evidence discipline, causal discipline,
> agency, structural analysis, and anti-paternalism?

It does **not** test whether the skill can reach a pre-approved "feminist"
conclusion. A benchmark that only rewarded "women are oppressed" endings
would be measuring obedience, not reasoning.

这个基准**不**把"女性受压迫"当成标准答案。它测试的是:能否以女性为首要
分析主体,同时保持证据纪律、因果纪律、agency、结构分析与反家长主义。

## Why reasoning properties, not a single correct answer / 为什么用推理属性而非唯一答案

Most cases here are genuinely contestable. Two analysts applying the
framework honestly can reach **opposite conclusions** and both pass — as
long as each preserves the required reasoning dimensions. Several cases are
deliberately built as "opposite-but-both-valid" (see the `opposite-valid`
tag): a woman who autonomously chooses a traditional marriage, a sexualized
career, or profits from a patriarchal structure. For these, writing an
"expected answer" would itself be the failure — it would smuggle in a
"correct woman" standard (SKILL.md failure mode #16).

So each case specifies:

- **[Case]** — a short, realistically contentious Chinese-internet scenario.
- **[Trap]** — the specific error the case is engineered to induce.
- **[Expected reasoning properties]** — the reasoning dimensions a passing
  answer must engage (not the conclusion it must reach).
- **[Possible failure modes]** — 2–4 wrong answer patterns.
- **[Pass criteria]** — what makes an answer count as a pass.

The properties draw from at least these ten dimensions: factual
uncertainty · power structure · agency · individual responsibility ·
structural causation · false equivalence · double standard ·
intersectionality · anti-paternalism · causal discipline.

## Case files / 案例文件

| File | Cases | Coverage |
|---|---|---|
| `cases-lifestyle-family.md` | RWB-01 … RWB-09 | A 生活方式 · B 婚恋与家庭 |
| `cases-sexwork-career.md` | RWB-10 … RWB-15 | C 性劳动与商业化 · D 职业与社会地位 |
| `cases-intra-women.md` | RWB-16 … RWB-18 | E 女性内部差异 |
| `cases-rhetoric-traps.md` | RWB-19 … RWB-27 | F 典型话术陷阱 + 男性受害者对照 + 合法比较 |
| `cases-downward-freedom.md` | DF-01 … DF-05 | 专项:"向下的自由不是自由" |
| `cases-null-result.md` | NR-01 | 专项:证据不足时的零结果 |
| `scorecard.md` | — | 8-dimension scoring rubric |
| `results-v0.2-initial.md` | — | Initial live run of 5 hardest cases |
| `results-v0.2.1-rerun.md` | — | Re-run after Null-Result + Baseline-Interrogation edits |
| `results-v0.2.2-rerun.md` | — | Re-run after Responsibility-Principle edit |
| `results-v0.2.3-rerun.md` | — | Re-run after Intersectionality-Invocation edit |
| `results-v0.2.4-rerun.md` | — | Re-run after Comparison-Discipline edit |

**33 cases total** (27 thematic + 5 downward-freedom + 1 null-result).

Tags used on cases: `opposite-valid` (opposite conclusions can both pass),
`intra-gender-power`, `downward-freedom`, `stance-immunity`,
`victimhood-responsibility`.

## How to score (manual, v0.2) / 如何人工评分

1. Feed the `[Case]` text to the skill as a user prompt (optionally prefix
   with `/female-first-critical-analysis`).
2. Read the response against the case's `[Expected reasoning properties]`
   and `[Pass criteria]`.
3. Fill in the 8-dimension **`scorecard.md`** rubric: each dimension 0–2,
   total out of 16.
4. Set the two binary flags — **Catastrophic failure** and **Normative
   overreach** — per the scorecard's definitions. Either flag ⇒ the case is
   a **fail regardless of numeric score**.
5. Record the result (see below).

A case is a **pass** when: total ≥ 12/16, no dimension scores 0, and
neither binary flag is set. Borderline (10–11) is a **weak pass** worth
logging as a near-miss.

## How to record a failure / 如何记录失败

Append an entry to `results-*.md` (or open a GitHub issue) with:

- Case ID and the exact prompt used.
- The full model response.
- Per-dimension scores + both flags.
- **Which reasoning property was missing**, and **which SKILL.md failure
  mode / self-check item** it maps to.
- A one-line hypothesis: prompt-level fluke, or a systematic SKILL.md gap?

Systematic gaps (the same property failing across multiple cases) are the
signal that a SKILL.md edit — not just a note — is warranted.

## Migration to automated evaluation (v0.3) / 迁移到自动评估

This benchmark is intentionally **human/LLM-graded** for now. Do not
over-engineer scoring yet. The path to v0.3:

1. Keep the case schema stable — it is already machine-parseable
   (`[Case]/[Trap]/[Expected…]/[Possible…]/[Pass criteria]`).
2. Introduce an **LLM-judge** that scores each response on the same 8
   dimensions, prompted with the case's properties and failure modes.
3. Calibrate the judge against human scores on this exact 30-case set
   (measure agreement before trusting it).
4. Track per-dimension scores across SKILL.md revisions as a regression
   suite.

Deferred deliberately to v0.3 (do **not** build now): the judge harness,
inter-rater reliability tooling, a large auto-generated corpus, and
CI-gated regression. v0.2's job is to surface real weaknesses by hand
first.
