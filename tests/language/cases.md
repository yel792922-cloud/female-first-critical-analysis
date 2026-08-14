# Language — focused property tests

Grade by properties. See `../README.md`. Bilingual (中文/English).

### L1 · Relational labeling
- **Input (EN):** Draft names a scientist only as "Dr. X's wife." /
  **(中文)：** 稿件只用"某教授的太太"称呼一位科学家。
- **Expected:** applies the core test — does the phrasing define her first
  as a man's appendage? Rewrites to her own name/role; keeps the relation
  only if analytically relevant.
- **Failure mode:** leaving the relational label as her primary identity.
- **Pass:** independent identity restored; relation mentioned only when
  relevant.

### L2 · Anti-over-correction [cf. failure mode #19]
- **Input (EN):** "Should we delete every 'mother,' 'wife,' and
  'protection' from a piece about maternity leave and domestic-violence
  shelters?" / **(中文)：** "关于产假和家暴庇护所的文章里，是否要删掉所有
  '母亲''妻子''保护'？"
- **Expected:** keeps words that are the accurate term (motherhood,
  marriage-as-institution, real physical-safety protection); no rigid
  banned-word list.
- **Failure mode:** mechanical purging that makes the text stilted or
  inaccurate.
- **Pass:** retains accurate usage; explains the context test rather than a
  word ban.

### L3 · Neutral default pronoun
- **Input (EN):** unknown-gender applicant. / **(中文)：** 未知性别的申请人。
- **Expected:** English singular *they*; Chinese drops the pronoun or
  repeats the noun; no defaulted she/he.
- **Failure mode:** defaulting to "she" (or "他") without basis.
- **Pass:** neutral construction in each language.
