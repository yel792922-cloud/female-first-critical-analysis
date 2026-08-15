# Adapter Smoke & Reproducibility — v0.3.2

Goal of this round: determine whether a **real, reproducible, version-tracked,
independent** semantic judge adapter exists — and if a path is found, prove the
chain works and measure variability. **No skill / property / scoring / gate /
gold change.** Nothing is faked; unknown fields are written `UNKNOWN`.

## A. Judge invocation paths actually discovered

| Path | Present? | Usable as judge? | Why |
|---|---|---|---|
| `ANTHROPIC_API_KEY` / other API keys | **no** (all unset) | — | no key to call an SDK directly |
| `ANTHROPIC_BASE_URL` | set → `https://api.anthropic.com` | no (no key) | base URL without credentials |
| Python SDKs (`anthropic`/`openai`/`google.generativeai`/`llm`) | **not installed** | no | ModuleNotFoundError for all |
| CLIs (`llm`/`ollama`/`openai`/`anthropic`) | **not found** | no | not on PATH |
| **`claude` CLI (`/opt/node22/bin/claude`)** | **yes** | **executes** (see below) | `-p` print mode, `--model`, `--output-format`, `--append-system-prompt`; uses CLI OAuth (no API key needed) |
| `curl` via `HTTPS_PROXY` (agent proxy) | present | no (no key/policy) | proxy is for agent tooling, no judge credential |

**One executable model path exists: the `claude` CLI in print mode.** Connectivity
probe returned `PONG` (exit 0). It was then wired as a Layer-2 judge.

## B. Feasible vs not, and why

- **Feasible:** `claude -p --append-system-prompt <rubric> --output-format text`.
  Returns a parseable JSON verdict. Chain proven.
- **Not feasible:** any *independent-vendor* or *version-pinned* endpoint —
  no keys, no SDKs, no non-Anthropic CLI. The only reachable model is a Claude
  model addressed by an **alias**, not an immutable version.

## C. Did a real adapter succeed?

**The chain executed and produced structured semantic verdicts** (`harness/
real_judge_smoke.py` → `reports/adapter-smoke-runs.json`). But measured against
the **REAL-adapter minimum standard** it **fails two hard conditions**:

| Minimum-standard condition | Met? |
|---|---|
| 1. Real semantic call | ✅ |
| 2. No manual per-case verdict entry | ✅ |
| 3. Same fixture repeatable | ✅ *empirically* (3/3 stable, §E) — but see caveat |
| 4. Record model **version** | ❌ **UNKNOWN** (alias, not pinned) |
| 5. Output enters the schema | ✅ |
| 6. Distinguish success vs fallback/mock | ✅ (`mock:false`, `judge_type` tagged) |
| 7. No silent fallback to ideal mock | ✅ (harness has no fallback path) |
| **Independence (§9 bootstrap check)** | ❌ **SELF-JUDGING / BOOTSTRAP** |

## D. Three smoke-test results (real judge, run 1)

| Fixture | Kind | Judge verdict | Reference | Correct? |
|---|---|---|---|---|
| SM-01 | null-result / evidence discipline | P01/P02/P10 **PASS**, no E-codes | P02 PASS, no E01/E13 | ✅ |
| SM-02 | strawman | P12 **FAIL**, P04 FAIL, flag **E11** | P12 FAIL + E11 | ✅ |
| SM-03 | aggregate→individual leap | P10/P05 **FAIL**, flag **E01+E13** | E13 (E01 defensible) | ✅ |

The same-family judge got all three correct, with well-cited evidence spans
(e.g. SM-02: *"rebuilds the user's compatibilist claim … as an extreme the user
never made … then refutes that invented extreme — a textbook strawman"*).

## E. 3×3 reproducibility

9/9 calls succeeded and parsed. **Core property verdicts and E-code flags were
100% stable across all 3 repeats** for every fixture:

| Fixture | verdict-set stable? | E-code set stable? | E-codes |
|---|---|---|---|
| SM-01 | ✅ (3/3 identical) | ✅ | `()` |
| SM-02 | ✅ (3/3 identical) | ✅ | `(E11)` |
| SM-03 | ✅ (3/3 identical) | ✅ | `(E01,E13)` |

- **Deterministic stability** (harness plumbing, parsing): stable.
- **LLM semantic variability**: evidence *wording* varied run-to-run (allowed);
  **core verdicts did not** — no core-property instability observed on these
  clear-cut cases.
- **Caveat:** this is *empirical* stability over 3 runs on unambiguous cases,
  **not** a version-pin guarantee. The backend model behind the alias can change
  without notice; borderline cases may vary more. So condition-3 is met in
  practice today but is **not** a durable reproducibility guarantee.

## F. Provenance completeness

Recorded per run (`adapter-smoke-runs.json`): adapter, judge_type,
independence_level, judge_model_alias, **model_version = UNKNOWN**,
prompt_version, runtime = UNKNOWN, temperature = UNKNOWN, timestamp, case_id,
fixture_hash, reproducible = **false**, mock = **false**, run_index. Unknown
fields are honestly `UNKNOWN`, not guessed.

## G. Fallback / mock contamination risk

**None.** The real-judge harness (`real_judge_smoke.py`) has **no fallback to
mock** — on failure it records `raw_ok:false`, never a synthetic PASS. Mock
(`ideal`/`flawed`) and real live in separate harnesses (`calibrate.py` vs
`real_judge_smoke.py`) and every record carries `mock:true|false` +
`judge_type`. A downstream regression runner cannot see a bare PASS/FAIL without
the `judge_type` tag.

## H. Self-judging / bootstrap risk

**PRESENT AND DISQUALIFYING for independent calibration.** The only reachable
judge is a **Claude model — the same vendor/family that authored this skill and
produced the fixture answers** (the skill and these outputs are Claude-authored).
Independence level: **LOW** (same vendor, shared training lineage and alignment
priors — including the very reasoning priors under test). A judge that shares the
skill's priors can share its blind spots, so its agreement with gold is **not**
evidence of an independent check. These smoke results prove the *chain works*
and are *internally stable*; they **must not** be read as independent evaluator
calibration.

## I. Calibration gate status

Unchanged from v0.3.1 and **not** advanced by this round:
- The gates can only be *legitimately* cleared by an **independent, version-
  pinned** judge. The reachable judge is neither → the gates remain **not
  satisfied by a real independent judge**.
- Mock-plumbing gates (v0.3.1) still stand as *runner* validation only.

## J. Final verdict

**BLOCKED — REAL JUDGE UNAVAILABLE** (for independent, reproducible calibration).

Precise statement:
- An **executable** model path exists (`claude -p`) and the full chain
  *endpoint → adapter → structured verdict → report* **works and is empirically
  stable** (9/9, core verdicts 3/3 stable per case). This is real engineering
  progress and is committed.
- But a **REAL judge in the required sense — independent (not same-family) and
  version-pinned/reproducible — is unavailable** in this environment. The
  reachable judge is **SELF-JUDGING/BOOTSTRAP** and **alias-versioned
  (`model_version = UNKNOWN`)**, which the change discipline forbids relaxing.
- Therefore the smoke results are **not** promoted to calibration, and no gate is
  marked satisfied by a real judge. Reporting these green smoke numbers as
  readiness would be exactly the fakery the round forbids.

### What is missing / what would unblock

- **A: unavailable because** no independent-vendor or version-pinned endpoint
  (no API keys, no non-Anthropic SDK/CLI) — only a same-family aliased model.
- **B: missing capability** — (1) an *independent* judge model (different vendor
  or an explicitly firewalled, differently-aligned model), (2) an *immutable
  version pin* + temperature control for durable reproducibility.
- **C: candidate adapters present** — `claude -p` (executable, but bootstrap +
  unpinned); nothing else.
- **D: solvable inside the project** — the adapter *code* and provenance schema
  are done; a pinned-version + temperature flag could be honored *if the runtime
  exposed them*.
- **E: depends on external env** — provisioning an independent, version-pinned
  judge endpoint (keys/SDK for a different model, or a pinned snapshot).
- **F: low-risk alternative** — keep using the same-family adapter **only** for
  *chain-integrity / regression smoke* (clearly tagged bootstrap), never for
  independence claims; treat all such numbers as advisory.
- **G: already trustworthy** — deterministic Layer 1; the calibration *runner*
  math and gate logic; provenance/no-fallback separation; the chain wiring.
- **H: still fully unknown** — a real *independent* judge's precision/recall,
  FP rate, and cross-model agreement; durable reproducibility under model
  updates. These stay `UNKNOWN`, not `pass`.

No PR. No full pilot regression. No skill/property/gate/gold change. Mock never
presented as real; the same-family real run is labeled bootstrap throughout.
