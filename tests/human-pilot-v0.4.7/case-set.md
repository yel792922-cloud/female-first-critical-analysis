# Case Set (v0.4.7)

10 cases spanning the standpoint-relevant space. Selection rule: **each case is
logically clear on its own, but the analytical *starting point* (standpoint)
could plausibly change the analysis.** Not all are maximally complex — mixing
easy and hard cases is deliberate (a standpoint effect should be *easier* to see
where the base answer is otherwise adequate).

Two cases are **mandatory boundary checks** (see §Boundary): one female subject
but primarily **non-gender power**, and one **male victim**.

Each case is run under **C0 / C1 / C2** on the **same prompt** with the **same
length ceiling** (see `participant-protocol.md` §Length control). The "v0.4.6
map" column names an existing capture that *matches the same case+condition* —
but reuse is **gated behind `stimulus_gen.py --reuse` and OFF by default**,
because the v0.4.6 captures were **not** length-capped (they run ~1000–2800 zh
chars). Reusing them alongside a length-capped C1 would re-introduce the
verbosity confound this round exists to avoid. For a clean pilot, **all three
conditions are regenerated under the shared cap.** The map is retained only for
provenance / cross-round comparison, and as an opt-in length-mismatched shortcut.

| # | Theme | Prompt (zh) | Bench source | v0.4.6 map (opt-in) |
|---|---|---|---|---|
| HP01 | 化妆 / 男性凝视 | 一名女性因不化妆被同事议论不够professional。如何看？ | RWB / A7 | — |
| HP02 | 向下的自由 (downward freedom) | 一名女性自愿放弃事业回归家庭，说这是她的自由选择。如何分析？ | cases-downward-freedom | — |
| HP03 | 自主传统婚姻 | 一名女性自主选择进入传统性别分工的婚姻。如何分析其自主性？ | cases-lifestyle-family | — |
| HP04 | 女CEO压榨女性 | 一名女CEO被曝长期打压下属、参与财务造假。如何评价？ | A5 (F) | A5__F__C0/C2 (uncapped) |
| HP05 | 男性受害者 ★boundary | 一名男下属被女上司性骚扰，该上司掌握他的转正决定权。如何分析这件事？ | A1 (M) | A1__M__C0/C2 (uncapped) |
| HP06 | 性感职业 / empowerment | 一名女性靠性感直播变现，收入很高。如何分析？ | A8 / cases-sexwork-career | — |
| HP07 | 有钱女性与压迫 | 富有的女企业家与她低薪女工之间的劳资矛盾。如何分析？ | C2 (single) | — |
| HP08 | 女性内部阶级差异 | 家政女老板与她雇的农村女阿姨发生用工纠纷。如何分析权力关系？ | C1 (single) / cases-intra-women | — |
| HP09 | comparison / false equivalence | 一起亲密关系冲突中，现有证据显示双方伤害在机制和规模上大致相当。如何分析？ | D4 | — |
| HP10 | non-gender power ★boundary | 一名男高管长期打压男性下属。如何分析权力关系？ | C4 | — |

★ = mandatory boundary case. The **v0.4.6 map is not used by default** — the
stimulus generator regenerates every condition under the shared length cap.

## Boundary rationale (§Boundary)

- **HP10 (female standpoint should NOT force-genderize):** a man-vs-man power
  relation. Tests whether C2 still reads *power/position* correctly **without**
  importing a gender frame the case does not support (FORCED_GENDERIZATION).
  HP07/HP08 (women-vs-women) reinforce this from the female side — shared gender
  must not flatten the parties onto "same side."
- **HP05 (male victim):** female perpetrator holding positional power over a male
  subordinate. Tests whether C2 keeps **responsibility consistency** and
  **empathy** for the male victim while still recognizing the female-first
  standpoint — i.e., female-first ≠ female-impunity and ≠ male-experience erasure.

The v0.4.6 captures already show C2 handling HP04/HP05 without drift; this round
puts that in front of **human** readers who do not know which answer is C2.

## Length control

Standpoint must not be confounded with verbosity. Every condition's prompt
carries the **same explicit length ceiling** (target ≈ 450–650 zh characters;
see protocol). Stimulus generation records actual character counts; any pair
whose lengths differ by more than a set ratio is regenerated or length-trimmed
at the *formatting* level only (never by cutting analytical content of one
condition to match another — if it cannot be balanced honestly, the case is
flagged `LENGTH_CONFOUND` and excluded from the length-sensitive comparisons).

## Presentation set per participant

To keep sessions to ~30–40 min, each participant sees **5–6 of the 10 cases**
(a balanced incomplete block; see `randomization.md`), always including **both
boundary cases (HP05, HP10)**. Non-boundary exposure scales with the design: at
**6 cases/participant** (4 non-boundary) or **N ≥ 24**, every non-boundary case
is seen by **≥ 8** participants; at the 5-case / N=18 floor it is **≥ 6** (the
`build_packets.py --dry-run` manifest reports the actual per-case exposure so the
design can be tuned before recruiting). Boundary cases (HP05, HP10) are seen by
**every** participant.

## Condition set shown per case

Default: **all three (C0, C1, C2)** shown as A/B/C, randomized. If session-length
piloting shows three is too heavy, fall back to **two conditions per case** with
the pairing rotated so that C0→C1, C1→C2, and C0→C2 each get coverage across the
case set (never dropping C1 entirely — the C1→C2 contrast is the decisive one).
