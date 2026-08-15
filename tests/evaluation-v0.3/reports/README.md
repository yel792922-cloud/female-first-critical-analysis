# Reports

A report is produced per `evaluation-schema.json` and rendered to markdown by
`../harness/run_eval.py`. There are three report shapes:

- **Per-output** — the three layers + verdict for one captured output.
- **Per-pair (pairwise)** — stability across two outputs (`ADAPTER_PENDING`
  until the judge adapter is wired).
- **Regression** — version N-1 vs N, with the **CRITICAL DELTA** block first
  (`../regression-protocol.md`).

`sample-run.md` is a **real** run of Layer 1 on the `../fixtures/` — not a
mock. Layers 2–3 appear as `ADAPTER_PENDING` because no judge model is wired in
this environment; that is reported honestly, never faked.
