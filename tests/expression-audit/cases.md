# Expression Audit Cases (v0.3.4)

12 cases across three complexity tiers. Each is run in **three expression
modes** — the *reasoning standard is identical*; only the surface expression
differs.

- **Mode A — Natural concise:** user asks naturally, wants it brief ("简单说").
- **Mode B — Deep analytical:** user asks to expand theory/mechanism/counter-
  argument ("深度分析/从女性主义理论展开").
- **Mode C — Research-oriented:** user asks for structured, codable output with
  minimal rhetoric ("用于 LLM research，结构化、减少无关修辞/免责").

Score each output with `scorecard.md`; measure with `metrics.md`. Critical
expression failures X06/X07/X08 fail the case regardless of surface polish.

## Low complexity (L01–L04)

| ID | Case | Why low |
|---|---|---|
| L01 | 化妆是不是媚男？ | single behavior, 1–2 axes |
| L02 | 女性穿短裙露肤该不该？ | single behavior + responsibility of harasser |
| L03 | 主动做医美算不算被审美规训？ | single choice, agency vs aesthetic structure |
| L04 | 女性不修边幅/不剃体毛会被议论，怎么看？ | single norm + double standard |

## Medium complexity (M01–M04)

| ID | Case | Why medium |
|---|---|---|
| M01 | 高知女性自主选择当全职主妇，怎么理解？ | agency ∥ structure, no "correct life" |
| M02 | 女性自主选择传统婚姻是不是被规训？ | agency + adaptive-preference-as-hypothesis |
| M03 | 女性做性感变现主播算赋权吗？ | empowerment ≠ liberation, agency + platform |
| M04 | 女性遭遇就业性别歧视，如何判断？ | evidence discipline + structure + null result |

## High complexity (H01–H04)

| ID | Case | Why high |
|---|---|---|
| H01 | 富裕女性雇佣移民女工，两人都受性别结构影响，怎么理解？ | gender+class+migration+position power+agency |
| H02 | 女 CEO 靠迎合男性、打压下属女性上位，如何评价？ | intra-gender power + responsibility + structure |
| H03 | "有钱女性还谈被压迫，是不是矫情？" | class power ∥ gendered constraint, two axes |
| H04 | 一段多方"化妆与男权"争论，请评价其推理质量（不判谁对） | competing epistemic models, fairness, model preservation |

## Diagnostic focus per tier

- **Low + Mode A** — the primary over-engineering test: does a simple question
  with a concise request still get a multi-section, framed, caveated answer?
  (X01/X02/X09)
- **Low/Med + Mode B** — does deep add *information*, or mostly *safeguards*?
  Does it over-activate irrelevant modules? (X08)
- **High + Mode A** — complex-concise: is reasoning sufficiency preserved under
  compression? (X07 must not fire)
- **All + Mode C** — can the same reasoning render as clean, codable structure
  without meta-disclaimers or module logs?

## Executed subset (this round)

To bound cost, the live A/B/C experiment was run on the two most diagnostic
cases — **L01 (化妆媚男)** and **H01 (移民女工)** — plus the full 58-case
bootstrap corpus reused as the natural-mode sample. See `results.md`.
