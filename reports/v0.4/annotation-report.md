# Annotation Report (v0.4)

## Protocol status
The human-annotation protocol is **complete and ready**
(`../../tests/research-protocol/annotation/protocol.md`,
`schema/annotation-schema.json`): property + epistemic-commitment annotation
(not a single correct answer), two independent annotators, per-property percent
agreement + Cohen's kappa, third-annotator adjudication, dual-validity recorded
rather than forced.

## Execution status
- **Human annotators run this round: 0.** No human raters are available in this
  automated environment, so no inter-rater agreement statistic is produced.
  This is recorded as **execution-pending**, not as a pass.
- The **acting-model / bootstrap** judge can pre-populate candidate annotations
  for human review, but bootstrap output is **LOW independence** and is not a
  substitute for human inter-rater agreement.

## What is ready vs missing
- Ready: instructions, schema, disagreement handling, adjudication rules,
  agreement-calculation method.
- Missing (pending): actual human annotations + measured inter-rater agreement.
  Written as UNKNOWN, never PASS.
