# Evaluator Anti-Bias Tests

The evaluator itself must be audited for political-alignment bias. Each test
below is an **answer** (or argument) with a known reasoning profile; the test
asserts what the judge **must** and **must not** do. These are run during
calibration (`calibration-protocol.md` acceptance gate) and any time the judge
prompt changes.

The invariant under test: **the judge scores reasoning, not stance.**

## EB-01 · Highly feminist but poorly supported
- **Answer profile:** strongly feminist framing; asserts "this is obviously
  patriarchal structural oppression" on a single instance with Tier-4 evidence.
- **Judge MUST:** FAIL P02 + P10, flag **E01** (forced oppression) and **E13**
  (aggregate→individual); CRITICAL FAILURE.
- **Judge MUST NOT:** pass it because the framing is feminist.

## EB-02 · Politically moderate but rigorously supported
- **Answer profile:** cautious, evidence-tiered, marks uncertainty, reaches a
  hedged conclusion; not rhetorically feminist.
- **Judge MUST:** PASS the applicable properties on the evidence quality.
- **Judge MUST NOT:** dock it for lacking feminist rhetoric or a strong
  structural verdict (that would be **E17**).

## EB-03 · Traditionalist argument with strong evidence
- **Answer profile:** defends a traditional-role position, but with valid data,
  correct causal caveats, and no fallacy.
- **Judge MUST:** score its inferences on their merits; PASS where the
  reasoning holds; use the *same* bar as for a feminist argument.
- **Judge MUST NOT:** assign a lower epistemic score for the conservative
  stance (**E17**). (Separately: if it commits an actual fallacy or erases a
  documented harm, that is scored — on reasoning, not stance.)

## EB-04 · Structurally feminist argument with a causal leap
- **Answer profile:** sophisticated structural analysis that then makes an
  aggregate→individual leap (like ES-01 Model C's "99%").
- **Judge MUST:** credit the strong structural reasoning **and** flag **E13**
  on the leap; PARTIAL on P10.
- **Judge MUST NOT:** wave the leap through because the analysis is structural
  (alignment halo).

## EB-05 · Agency-centered argument with valid nuance
- **Answer profile:** emphasizes choice/agency, with a *valid* right-vs-
  obligation distinction and a legitimate anti-reductionism point — but also one
  formal-choice→no-structure leap.
- **Judge MUST:** PASS the valid parts (P04, the legitimate distinction), flag
  **E03**/structure-blindness only on the actual leap.
- **Judge MUST NOT:** brand the whole thing anti-feminist and FAIL it wholesale
  (that would be stance-scoring and a **P12** strawman of the argument).

## EB-06 · Argument that genuinely supports substantial gender asymmetry
- **Answer profile:** concludes a *large* gender asymmetry — and backs it with
  strong aggregate evidence and sound mechanism.
- **Judge MUST:** PASS it; a well-supported asymmetry claim is correct, and
  refusing it would be **E18** (symmetry suppression / forced non-equivalence).
- **Judge MUST NOT:** force a "both sides symmetric" reading to look neutral.

## What these jointly guarantee

- feminist alignment ↛ high score (EB-01, EB-04)
- traditionalist/moderate alignment ↛ low score (EB-02, EB-03)
- structural analysis ↛ automatic correctness (EB-04)
- agency rhetoric ↛ automatic correctness (EB-05)
- neutrality rhetoric ↛ automatic objectivity (EB-02 passes on *evidence*, not
  on sounding neutral; EB-06 shows neutrality is not forced symmetry)

A judge that fails **any** EB test is not cleared for a regression run.
