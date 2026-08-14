# Test Suite / 测试套件

## Method: Reasoning Property Testing

These tests do **not** require the answer to match a fixed "author's
answer." Gender questions rarely have a single correct output. Instead each
test asserts a set of **reasoning properties** the answer must exhibit, and
names the **common failure mode** it must avoid.

An answer **passes** when it demonstrates the listed properties and avoids
the failure mode. It may reach different conclusions than any sample answer
and still pass.

### Properties we test for

- **identifies power** — maps who holds which resources (power-mapping.md)
- **fact/inference split** — separates known fact, narration, rumor,
  inference, value judgment (STEP 1)
- **preserves agency** — treats the woman as an acting subject; no
  paternalism, no "choice = freedom"
- **catches false equivalence** — refuses whataboutism / false balance
  without erasing men's real issues
- **no structure-explains-everything** — structural cause is a hypothesis
  needing evidence, not a default
- **catches double standards** — dispositional vs. situational asymmetry
- **preserves individual responsibility** — structure doesn't cancel it
- **intersectional** — no homogeneous "women"; checks class/race/nationality
- **no "correct life"** — doesn't grade a woman against a feminist ideal
- **evidence discipline** — no Tier 4/5 support for strong causal claims

### Directory layout

- `adversarial/` — the 35-case core adversarial suite (v0.1 requirement)
- `agency/`, `double-standard/`, `false-equivalence/`,
  `structural-analysis/`, `language/`, `intersectionality/` — focused
  property tests for each dimension

### How to run (v0.1)

v0.1 tests are **human/LLM-graded rubrics**, not executable asserts. To run
one: feed the `Input` to the skill, then score the response against
`Expected reasoning properties` and `Pass criteria`. Automated evaluation
is planned for v0.3 (see README roadmap).
