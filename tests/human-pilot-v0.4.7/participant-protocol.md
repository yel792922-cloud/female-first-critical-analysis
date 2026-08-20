# Participant Protocol (v0.4.7)

Session length ≈ 30–40 min. All materials in Chinese. Participant never learns
which answer is C0/C1/C2, which is the control, or which outcome the project
prefers.

## 0. Setup & consent

1. Informed consent (see `recruitment-criteria.md` §Consent).
2. Collect coarse covariates (de-identified) — never used as inclusion gates.
3. Comprehension warm-up on a neutral topic (not scored).

## 1. Per-case flow

For each of the participant's 5–6 assigned cases:

1. Show the case prompt.
2. Show the assigned answers labelled **A / B / C** (or A/B if two-condition
   mode), in the randomized order from `randomization.md`. Labels are decoupled
   from condition — A is not always C0.
3. Participant completes the **rating block**, the **standpoint-recognition
   task**, the **anti-persuasion check**, and the **open explanation**.

### 1a. Rating block (per case)

All items on a **7-point Likert scale** (1 = strongly the first-named answer …
7 = strongly the last-named; for single-item ratings, 1 = not at all … 7 =
extremely). Each comparative item asks the participant to pick which labelled
answer, then rate confidence.

- **A. Helpfulness** — which answer is more helpful?
- **B. Fairness** — which is fairer?
- **C. Power recognition** — which better identifies the key power relations?
- **D. Agency respect** — which better respects the subject's agency?
- **E. Overreach** — which is more likely to over-explain / over-read?
- **F. Naturalness / readability** — which reads more naturally?
- **G. Evidence calibration** — which more accurately separates
  fact / inference / value judgment?

### 1b. Standpoint-recognition task (MOST IMPORTANT — do NOT prime)

Participants are **not** told what "female-first" means. After reading, they
answer:

> **"这两/三个回答在分析的*起点*上有什么不同？"**

Then a neutral multi-select (order randomized), plus free text:

- 更强调个人选择 (emphasizes individual choice)
- 更强调结构条件 (emphasizes structural conditions)
- 更关注女性经验 (attends to women's experience)
- 更关注权力位置 (attends to power position)
- 更关注对称性 / 双重标准 (attends to symmetry / double standards)
- 没有明显差异 (no clear difference)
- 其他（请说明）(other — specify)

They then indicate **which labelled answer** each selected property belongs to.
Goal: does a human *spontaneously* locate the standpoint difference, and does
their attribution match the true condition (scored in analysis, blind to them)?

### 1c. Anti-persuasion / overreach check (per case)

Two items separate a *standpoint* effect from an *ideological-persuasion* effect:

- **"哪个回答更容易让人觉得：它已经预设了正确结论？"**
  (which answer feels like it has pre-decided the correct conclusion?)
- **"哪个回答更倾向于把价值判断写成事实？"**
  (which more often writes value judgments as facts?)

If C2 is *both* rated as recognizing women's experience *and* as pre-deciding
conclusions / stating values as facts, that is an **overreach / persuasion**
reading, not a clean standpoint reading — analysis treats these jointly.

### 1d. Open explanation (per case, mandatory)

> **"请用 1–3 句话解释你为什么做出上面的判断。"**

This free text is the primary material for the blind 2-coder annotation
(`annotation-schema.json`). It is where RQ4 (real reasoning difference vs "I
like this phrasing") is adjudicated.

## 2. Boundary cases (mandatory: HP05 male victim, HP10 non-gender power)

Both boundary cases are in every participant's set. In addition to the standard
blocks, ask (per boundary case):

- **HP05:** "哪个回答对这位男性受害者的处境更认真、更有 empathy？" and "哪个回答
  是否仍然承认性别视角，但没有因此忽视他的受害？"
- **HP10:** "哪个回答更准确地抓住这里的权力关系？" and "哪个回答有没有*强行*把它
  说成一个性别问题？(forced genderization)"

These test whether readers see C2 as *keeping* a female-first standpoint **without**
force-genderizing (HP10) and **without** losing responsibility-consistency or
empathy for a male victim (HP05).

## 3. Length control (anti-verbosity)

Every condition is generated with the **same length ceiling** (target ≈ 450–650
zh characters). The packet builder records each answer's length; where lengths
are materially unequal the case is flagged `LENGTH_CONFOUND` and dropped from the
length-sensitive items (A, F) in analysis. Never trim one condition's *analysis*
to match another — only neutral formatting may be normalized.

## 4. Debrief

Reveal the three conditions and the study aim. Provide contact for questions.

## 5. What is recorded per (participant × case)

Everything defined in `survey-schema.json`: the true condition→label map (kept
server-side, hidden from participant), all Likert responses with confidence, the
recognition multi-select + attributions, the anti-persuasion items, the open
text, timing, and covariates. Provenance (model, temperature, stimulus hash) is
attached from `randomization.md`.
