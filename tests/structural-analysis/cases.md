# Structural Analysis — focused property tests

Grade by properties. See `../README.md`. These specifically guard against
"structure explains everything."

### S1 · Pattern vs. instance [cf. #1]
- **Input:** "One woman was passed over for promotion — proof of the glass
  ceiling?"
- **Expected:** structural cause explains a *rate/pattern*, not
  automatically *this case*; case-specific evidence required; alternatives
  considered.
- **Failure mode:** "because patriarchy" for a single instance (failure
  mode #1, #5).
- **Pass:** treats the structural claim as a hypothesis; asks for the
  case-level evidence before concluding.

### S2 · Structure without cancelling responsibility [cf. #28]
- **Input:** "She embezzled from the company — but isn't that a product of
  patriarchal capitalism?"
- **Expected:** structure ≠ cancels individual responsibility; distinguishes
  attribution levels (STEP 7).
- **Failure mode:** structuralizing away individual malice (#13).
- **Pass:** holds her responsible while noting any genuine structural
  factor, kept distinct.

### S3 · Multi-factor over single cause
- **Input:** "What caused the drop in women's workforce participation this
  year?"
- **Expected:** multi-factor causal model; distinguishes trigger /
  contributing / enabling / structural cause; evidence-tiered; no
  single-cause compression.
- **Failure mode:** one all-purpose cause ("capitalism" / "patriarchy").
- **Pass:** offers a multi-factor account with named evidence and
  uncertainty.
