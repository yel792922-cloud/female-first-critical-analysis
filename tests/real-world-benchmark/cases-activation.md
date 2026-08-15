# Activation Benchmark / 激活基准 (v0.2.7)

Tests the **Activation Architecture**, not feminist reasoning quality. The
question here is *what activated, how deep, how long* — and whether those
three stayed independent. **This is not a complexity ladder:** case
complexity and requested depth are separate axes.

Recorded metrics (see `results-v0.2.7-activation.md`): **false activation ·
missed activation · insufficient analysis · over-analysis · depth alignment ·
compression quality.**

---

## Part 1 — Four activation categories (complexity × requested depth)

### AC-A · simple case + shallow request
- **[Prompt]** "化妆是不是媚男?简单说。"
- **[Expected activation]** Necessary: Female-first, Agency, a light
  gender-norm/Power touch. Baseline Interrogation *may* fire ("媚男" implies a
  ranking) but stays light. **Inactive:** intersectionality, class,
  comparison, responsibility.
- **[Expected depth/output]** shallow depth, brief output — **but** minimum
  sufficiency preserved (don't reduce to "是" or "不是").
- **[Pass]** short answer that still keeps agency + norm ("depends; making up
  can be a norm-shaped choice *and* a real one — not automatically 媚男").

### AC-B · simple case + deep request
- **[Prompt]** "化妆是不是媚男?请从男性凝视、身体政治、agency、choice
  feminism 与消费资本主义详细分析。"
- **[Expected activation]** Necessary + the user-named frames: Agency,
  Power/Structure (gaze, body politics), anti-correct-life (choice feminism),
  relevant references (neoliberal-feminism, agency-and-capability). **Still
  inactive unless relevant:** intersectionality/class/comparison/
  responsibility.
- **[Expected depth/output]** deep + long — **even though the case is
  structurally simple.** Must NOT compress just because the case is simple.
- **[Pass]** genuinely deep multi-frame analysis; no auto-compression; no
  forced activation of unrelated modules.

### AC-C · complex case + shallow request
- **[Prompt]** "富裕女性雇佣移民女性家政工,这算不算父权?简单说。"
- **[Expected activation]** Necessary even when brief: Class/Position +
  Intersectionality (the case *is* multi-axis; omitting these misleads).
  Female-first, Power. **Optional/skip:** deep history, comparison.
- **[Expected depth/output]** brief output — **but** the core multi-axis point
  must survive compression.
- **[Pass]** short answer that still says: it's less "父权" than a class/
  nationality power relation between two women (gender not erased) — not a
  one-word yes/no.

### AC-D · complex case + deep request
- **[Prompt]** "富裕女性雇佣移民女性家政工——请深度分析权力结构、交叉性、
  agency 和责任。"
- **[Expected activation]** Class/Position, Intersectionality, Power, Agency,
  Responsibility — all genuinely relevant here — run deep.
- **[Expected depth/output]** deep + long.
- **[Pass]** full multi-axis analysis; the *same case* as AC-C but expanded
  because depth was requested, not because complexity auto-scaled it.

> **AC-A vs AC-B** (same case, different depth) and **AC-C vs AC-D** (same
> case, different depth) are the core decoupling proofs.

---

## Part 2 — Minimum-sufficiency under a brevity request (MS-01…05)

User demands one line, but omitting one dimension would materially mislead.
**Brevity ≠ permission to skip necessary analysis.** Pass = compressed yet
the necessary distinction survives.

### MS-01 · "她自己选了陪酒,所以这是不是自由?一句话。"
- **Necessary (cannot drop):** choice ≠ automatically liberation (agency +
  structural constraint).
- **Fail:** "是,因为是她自己的选择。"
- **Pass (one line):** "不必然——那是她的选择,但在多大程度上'自由'要看她有
  没有别的可行选项和退出能力。"

### MS-02 · "老板暗示下属陪酒才好升职,下属去了,是不是你情我愿?一句话。"
- **Necessary:** power asymmetry / coercion (can't call it mutual consent).
- **Fail:** "是,双方自愿。"
- **Pass:** "不算——上下级+升职要挟下的'同意'是被权力约束的,不是对等自愿。"

### MS-03 · "一句话:女性创业者一次融资失败,是不是因为性别歧视?"
- **Necessary:** Null Result / pattern≠instance (can't assert causation).
- **Fail:** "是,因为投资圈歧视女性。"
- **Pass:** "单看这一次不足以判定——行业确有性别差距,但这一案的具体原因证
  据不足。"

### MS-04 · "全职主妇是不是向下的自由?一句话。"
- **Necessary:** baseline interrogation minimum (who defines "down").
- **Fail:** "是,是向下的自由。"
- **Pass:** "先问'谁定的上/下'——若她保有独立资源和退出能力,就谈不上'向
  下';这标准本身值得质疑。"

### MS-05 · "有钱女企业家还谈被压迫,是不是矫情?一句话。"
- **Necessary:** two axes held (class power + possible gendered constraint);
  no identity-based dismissal.
- **Fail:** "是,都那么有钱了。"
- **Pass:** "两回事——她在阶级上有权力,不等于在性别上不会遇到具体偏见;要
  看具体证据,不能用财富一句否掉。"

---

## Part 3 — Deep request ≠ all modules (DR-01…02)

High requested depth licenses depth on **relevant** modules only — not a
checklist sweep of every module.

### DR-01 · "请深度分析女性化妆是否是一种父权规训。"
- **Should run deep:** Agency, gender norms, Power/body politics, relevant
  feminist theory (male gaze, choice feminism, neoliberal feminism).
- **Should stay OFF (no real relevance):** Intersectionality, Comparison
  (男性), Class/Position mapping, Responsibility, victimhood.
- **[Trap]** treating "深度分析" as "activate every module."
- **[Pass]** deep on the relevant axes; does **not** bolt on class mapping /
  male-comparison / responsibility just to look thorough (over-analysis =
  failure).

### DR-02 · "请从女性主义理论深度分析'素颜羞辱'(shaming women for going bare-faced)。"
- **Should run deep:** aesthetic labor, gender norms, Power, Agency, body
  politics, double standard.
- **Should stay OFF unless the user's framing introduces them:** Class/
  Position, Intersectionality, Comparison, Responsibility.
- **[Pass]** deep on the relevant axes; irrelevant modules remain inactive
  despite the "深度" request.
