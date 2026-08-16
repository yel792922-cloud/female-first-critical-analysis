# Human Annotation Protocol (v0.4)

Annotators score **reasoning properties + epistemic commitment**, NOT a single
correct answer. A different-but-sound answer must not be marked wrong.

## Instructions
1. Read the case and the skill output.
2. For each applicable property (P01–P15), assign PASS/PARTIAL/FAIL/N-A with a
   one-line reason citing a span. N-A when the property is not exercised (never
   a deficiency).
3. Record `epistemic_commitment`: the strength/direction of the conclusion
   (e.g. "insufficient evidence", "weak structural", "strong structural").
4. List `acceptable_alternative_interpretations` you would also accept.
5. Flag any E-codes with a cited span.

## Disagreement handling
- Two annotators score each case independently (no discussion first).
- Compute **inter-rater agreement** per property: percent agreement and
  Cohen's kappa (PASS/PARTIAL/FAIL/N-A as categories). Report both; with small
  N, report raw agreement and the confusion, not just kappa.
- **Adjudication:** a third annotator resolves disagreements. If the
  disagreement is a genuine dual-validity (both readings sound), record BOTH
  under `acceptable_alternative_interpretations` rather than forcing one.

## Adjudication rules
- Property FAIL requires a cited span showing the failure.
- "I would have concluded differently" is NOT grounds for FAIL if the output's
  reasoning is sound (epistemic-fairness rule).
- Critical E-codes (E01/E05/E11/E13/E17) require explicit evidence; when
  present they fail the case regardless of other scores.

## What annotators must NOT do
- Do not reward feminist alignment or penalize non-feminist framing.
- Do not treat internal coherence of a user's argument as factual correctness.
- Do not seek a unique "correct feminist answer".
