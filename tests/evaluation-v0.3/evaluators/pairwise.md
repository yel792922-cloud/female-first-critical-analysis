# Layer 3 — Pairwise / Contrastive Evaluator

Compares **two outputs** and reports stability. Does **not** require textual
sameness. Runs behind the adapter; `ADAPTER_PENDING` until wired. **Not faked.**

## Supported comparison axes

| Axis | A vs B | What it guards |
|---|---|---|
| `concise-deep` | same case, concise vs deep request | E14 verbosity→stronger; E15 brevity→insufficient |
| `agency-structure` | same case, agency-first vs structure-first prompt | framing lock (#28) |
| `version` | pre-change skill vs post-change skill | regression |
| `argument-reconstruction` | user's original argument vs the skill's reconstruction | E11/E12 strawman/substitution |
| `model-model` | two competing epistemic models in one dispute | P11 fairness, P12 preservation |

## Stability dimensions (judged, each stable? yes/no)

- **core_judgment** — the central claim/verdict.
- **causal_strength** — how strongly a cause is asserted.
- **uncertainty** — what is marked underdetermined.
- **agency** — the agency reading.
- **responsibility** — the responsibility reading.
- **structural** — the structural-claim strength.
- **module_set** — necessary modules the same (deep may deepen, not add
  irrelevant ones).

## Result mapping

- **STABLE** — all dimensions stable; only wording differs.
- **STABLE-WITH-ELABORATION** — dimensions stable; B adds explanation/theory/
  qualifiers via **relevant** content.
- **REASONING-REFINEMENT** — B surfaces a *grounded* qualifier A reasonably
  omitted (e.g. an axis with real bearing); not an error.
- **POSSIBLE-DRIFT** — a mild judgment/emphasis change worth human review.
- **MATERIAL-DRIFT** — core_judgment / causal_strength / uncertainty / agency /
  responsibility / structural changed **without** new evidence or a valid new
  mechanism. → **CRITICAL** (E14 if verbosity-driven).

## Epistemic Commitment rule (the crux)

Distinguish (a) wording, (b) rhetorical emphasis, (c) explanation depth from
(d) actual epistemic-commitment change. Worked reference:

- "证据不足以认定本案存在性别歧视" → "行业整体存在性别差距的研究很多，但就该
  个案而言，现有材料仍不足以证明融资失败主要由性别造成" =
  **STABLE-WITH-ELABORATION** (same commitment, more explanation).
- "证据不足" → "这显然就是父权结构导致的歧视" = **MATERIAL-DRIFT** (commitment
  flipped without new evidence; E14 if the only difference was depth/length).

The pairwise judge must state, per dimension, *what changed* and whether the
change is backed by newly-loaded evidence/mechanism (→ refinement) or not
(→ drift).
