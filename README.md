# female-first-critical-analysis

A **female-centered critical analysis framework** packaged as a
[Claude Code](https://claude.com/claude-code) Skill. It examines gender,
power, agency, resources, institutions, language, culture, media, work,
family, and social norms — prioritizing women as analytical subjects while
holding a high bar for evidence, causal reasoning, intersectional analysis,
and resistance to false equivalence.

> **This project is feminist-centered, not epistemically unconditional. It
> prioritizes women as analytical subjects without treating women as
> infallible or treating feminist conclusions as exempt from evidence.**

Supports **Chinese and English**.

---

## What this skill is

- A **reasoning engine** that makes gendered power structures legible and
  keeps analysis rigorous.
- A structured procedure (11 steps) for fact-checking, power-mapping,
  agency analysis, intersectionality, causal inference, double-standard
  detection, and steelmanning.
- A set of guardrails against the common failure modes of gender debate —
  on *both* sides of the argument.

## What this skill is **not**

- **Not** a "feminist opinion generator" that agrees with any pro-woman
  conclusion.
- **Not** an ideology prompt that blames patriarchy for everything
  regardless of input.
- **Not** a rulebook that grades women's lives against a "correct feminist"
  standard.
- **Not** a tool for erasing men's real, specific gendered harms (it
  refuses *derailment*, not their *existence*).

## Core principles (all four must hold at once)

1. **Female-first** — women as the primary analytical subject; male
   experience is not the default yardstick.
2. **High evidence standard** — a favorable conclusion never lowers the bar
   for fact, causation, or logic.
3. **Anti-false-equivalence** — "men suffer too" / "both sides" / "split
   the blame" cannot bury the specific structural problems women face.
4. **No prescribed correct life** — feminism is not a new set of rules every
   woman must obey.

## How agency is defined

The engine keeps nine concepts distinct and never collapses them: **choice,
autonomy, agency, capability, constraint, coercion, adaptive preference,
empowerment, liberation** (see `references/agency-and-capability.md`). Two
rules follow:

- "She chose it" ≠ "she was free" ≠ "it was liberatory."
- "It fits a patriarchal norm" ≠ "she has no agency."

Both the **agency trap** ("her choice, so it's liberation") and the
**paternalism trap** ("she's just brainwashed") are forbidden.

## How structural analysis works

Structure is examined **first** but attributed **only with evidence**. A
structural cause explains a *rate or pattern* across many cases; moving from
pattern to a specific instance requires case-level evidence. Structural
explanation does not cancel individual responsibility, and individual
responsibility does not deny structure (see `references/causal-reasoning.md`).

## How evidence is handled

Five-tier scale (Tier 1 primary sources → Tier 5 rumor). Tier 4/5 cannot
support strong causal conclusions. For social-media events, the engine
separates "publicly confirmed," "circulating online," and "inference from
narration," and says "not determinable" when sources are absent. See
`SKILL.md` → *Evidence tiers*.

## How to install

This is a Claude Code Skill. Install by placing the folder where Claude Code
discovers skills:

```bash
# Personal (all projects)
git clone https://github.com/yel792922-cloud/female-first-critical-analysis.git \
  ~/.claude/skills/female-first-critical-analysis

# Or per-project
git clone https://github.com/yel792922-cloud/female-first-critical-analysis.git \
  .claude/skills/female-first-critical-analysis
```

Claude Code reads the YAML front-matter in `SKILL.md` (`name`,
`description`) to register and route to the skill.

## How to invoke

- **Explicitly:** `/female-first-critical-analysis` followed by your
  question.
- **By reference:** ask Claude to "analyze this with the female-first
  framework."

## How automatic invocation works

Claude Code matches a request against each skill's `description`. When a
prompt involves analyzing a gendered situation, event, choice, conflict,
policy, or media — especially with women as primary subjects — this skill's
description makes it a candidate, and Claude loads `SKILL.md`. Reference
files are loaded **on demand**, only when relevant, to keep context lean.

## How to extend references

Add a new `references/<topic>.md` and link it from the relevant STEP or
policy section in `SKILL.md`. Keep theory *out* of `SKILL.md` (the engine
stays stable) and *in* references. Read references on demand — never load
all at once.

## How to add tests

Add a `cases.md` entry under the matching `tests/<category>/` folder (or a
new numbered case in `tests/adversarial/cases.md`). Each case needs:
**Input · Expected reasoning properties · Common failure mode · Pass
criteria.** Do **not** require a single fixed answer — use Reasoning
Property Testing (see `tests/README.md`).

## How to report failures

Open a GitHub issue with: the input, the actual output, which of the four
core principles or which failure mode (`SKILL.md` → *Forbidden failure
modes*) it violated, and the expected reasoning property that was missing.
A failing case makes a good new test.

## Known limitations

- v0.1 tests are **rubrics graded by a human or an LLM**, not executable
  asserts. Automated evaluation is planned (see roadmap).
- No real-case benchmark yet (planned for v0.2).
- Only Chinese and English language policies exist.
- The framework encodes a **stated philosophical position** (below); it is
  not value-neutral, and does not claim to be.
- Reference files are concise skeletons, not exhaustive literature reviews.
- LLM-dependent: correct routing and adherence depend on the underlying
  model following `SKILL.md`.

## Political / philosophical position

This project is **feminist-centered**. It foregrounds women as analytical
subjects and treats gendered power as a primary object of analysis. It is
**not** epistemically unconditional: women are not treated as infallible,
feminist conclusions are not exempt from evidence, and the framework
explicitly refuses to prescribe a "correct" way for women to live. It also
refuses to erase men's specific, real gendered harms — while refusing to let
those harms *derail* a women's issue under discussion. The stance is
"female-first + rigorous logic + high evidence standard + no prescribed
correct life," all four at once.

## Roadmap

- **v0.1** — core framework + Chinese/English language policy + 30+ tests
- **v0.2** — real-case benchmark suite (33 cases) + iterative principle
  hardening (Null Result, Baseline Interrogation, Responsibility,
  Intersectionality Invocation, Comparison discipline, Class/Position Power,
  Parallel Analysis) + Activation Architecture calibration + architecture
  audit + **full dual-mode validation pass** *(current)*
- **v0.3** — automated reasoning-property evaluation harness *(offline
  scaffold landed: `tests/evaluation-v0.3/` — deterministic layer runnable;
  semantic + pairwise layers specified behind an execution adapter, not faked)*
- **v0.4** — domain-specific references
- **v1.0** — stabilized core axioms

**Validation status.** The skill is **principle-complete, activation-
calibrated, and validated**: all 33 benchmark cases were run in concise and
deep modes (66 runs) with **0 material drift** and stable epistemic
calibration. Verdict: **READY FOR v0.3**, contingent only on the automated
judge scoring *epistemic consistency, not textual sameness*. See
[`tests/validation-summary.md`](tests/validation-summary.md) and the full
[`tests/validation-v0.2-full-pass.md`](tests/validation-v0.2-full-pass.md);
the whole-skill audit is in
[`tests/architecture-audit.md`](tests/architecture-audit.md). The skill also
**passes the epistemic-system stress test** — reconstructing a whole
internally-coherent multi-party dispute and grading its reasoning quality
without treating political alignment as a truth condition — in
[`tests/epistemic-system-stress/`](tests/epistemic-system-stress/) (the
existing architecture supports this as a procedural mode; no core rule added).

Note: concrete political opinions are never written into the core engine.
The engine stays stable; stance, theory development, and cases live in
`references/`.

## License

MIT — see [LICENSE](LICENSE).
