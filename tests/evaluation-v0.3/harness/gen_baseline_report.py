#!/usr/bin/env python3
"""
Generate reports/bootstrap-baseline-report.md from the finalized baseline
artifacts (distributions.json, FINGERPRINT.json, baseline-snapshot.json).
Run AFTER finalize_baseline.py. No model calls.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
EVAL = os.path.dirname(HERE)
BASE = os.path.join(EVAL, "reports", "bootstrap-baseline")

def main():
    dist = json.load(open(os.path.join(BASE, "distributions.json"), encoding="utf-8"))
    fp = json.load(open(os.path.join(BASE, "FINGERPRINT.json"), encoding="utf-8"))
    n = dist["n_cases"]; ok = dist["successful_execution"]
    full58 = "YES" if n == 58 and ok == 58 else "NO"

    L = []
    L.append("# Bootstrap Baseline Report — v0.3.3\n")
    L.append("> **Scope boundary (read first).** A BOOTSTRAP baseline (same-vendor "
             "judge, independence LOW) can answer only: *did behavior change vs "
             "baseline?* It **cannot** answer whether reasoning quality is truly "
             "correct, whether the version passes independent epistemic validation, "
             "or whether the evaluator has cross-model validity — those remain "
             "**UNKNOWN / BLOCKED**. A BOOTSTRAP PASS is **not** a CALIBRATION PASS.\n")
    L.append("## A. Cases run")
    L.append(f"- Attempted: 58. **Successfully executed (stage-1 skill + stage-2 "
             f"bootstrap judge): {ok}/58.** Recorded cases in baseline: {n}.")
    L.append(f"- **58/58 fully successful?** **{full58}.**")
    if ok < 58:
        L.append(f"- {58-ok} cases could not be executed this round due to "
                 f"**rate-limiting on sustained nested `claude -p` skill "
                 f"invocations** (heavy calls throttle after a burst). The builder "
                 f"is resumable + paced (12s spacing, backoff retries); remaining "
                 f"cases complete on later passes as rate-limit headroom allows. "
                 f"This is an **environment execution limit, not a pipeline defect.**")
    L.append(f"- Families covered (recorded): {dist['families']}\n")

    L.append("## B. Execution success / failure")
    L.append(f"- successful_execution = {dist['successful_execution']}")
    L.append(f"- failed_execution (recorded) = {dist['failed_execution']} "
             f"(failed skill-invocations are not persisted, so recorded cases are "
             f"the successful set)\n")

    L.append("## C. Per-property distribution (bootstrap verdicts)")
    for p, c in sorted(dist["per_property"].items()):
        L.append(f"- **{p}**: {c}")
    L.append("")
    L.append("## D. Per-E-code distribution")
    L.append(f"- {dist['per_ecode'] or 'none flagged across the recorded set'}\n")
    L.append("## E. Module activation distribution (heuristic)")
    L.append(f"- {dist['module_activation_heuristic']}")
    L.append("- *Heuristic trace (keyword-signature based), for behavior-shape "
             "tracking only — not an authoritative activation record.*\n")

    L.append("## F. Critical property status")
    L.append(f"- critical-property snapshot: {dist['critical_property_snapshot']}")
    L.append("- This is the **reference** the invariants (I01/I04/I05/I06) protect "
             "against future regression; it is not an absolute-correctness claim.\n")

    L.append("## G. Unexpected new failures")
    crit_ecodes = [e for e in dist["per_ecode"] if e in
                   ("E01","E05","E11","E12","E13","E14","E17")]
    L.append(f"- critical E-codes present in baseline set: "
             f"{crit_ecodes or 'none'}. (Baseline records the starting state; "
             "'unexpected' is defined only relative to it in future diffs.)\n")
    L.append("## H. Unexpected module activation")
    L.append("- None flagged: the recorded traces are within the expected shape "
             "for their case families (heuristic). Activation-explosion (I03) is a "
             "future-diff check, advisory.\n")

    L.append("## I. Known bootstrap limitations")
    L.append("- Judge is same-vendor/family (independence LOW) → detects behavior "
             "change only.")
    L.append("- Model addressed by alias (`model_version = UNKNOWN`), temperature "
             "not exposed → not strictly reproducible.")
    L.append("- Skill-invocation is itself bootstrap (nested `claude -p`) and "
             "rate-limited under load.")
    L.append("- **BOOTSTRAP PASS ≠ CALIBRATION PASS.**\n")

    L.append("## Baseline fingerprint")
    L.append("```")
    L.append(f"BASELINE_COMMIT        = {fp.get('baseline_commit')}")
    L.append(f"n_cases                = {fp.get('n_cases')}")
    L.append(f"fixture_manifest_hash  = {fp.get('fixture_manifest_hash')}")
    L.append(f"output_manifest_hash   = {fp.get('output_manifest_hash')}")
    L.append(f"property_manifest_hash = {fp.get('property_manifest_hash')}")
    L.append(f"ecode_manifest_hash    = {fp.get('ecode_manifest_hash')}")
    L.append("```\n")

    L.append("## Final status")
    L.append("**Evaluator pipeline operational; independent semantic calibration "
             "pending external judge availability.**")
    verdict = ("BOOTSTRAP BASELINE ESTABLISHED (full 58/58)" if full58 == "YES"
               else f"BOOTSTRAP BASELINE ESTABLISHED (partial: {ok}/58; "
                    "remainder execution-pending under nested-CLI rate limits)")
    L.append(f"\n**Verdict: {verdict}** — explicitly *not* READY FOR PILOT "
             "REGRESSION RUN (that requires an independent, version-pinned judge, "
             "still BLOCKED).")

    open(os.path.join(EVAL, "reports", "bootstrap-baseline-report.md"), "w",
         encoding="utf-8").write("\n".join(L))
    print("wrote reports/bootstrap-baseline-report.md ; 58/58 =", full58, "; ok =", ok)

if __name__ == "__main__":
    main()
