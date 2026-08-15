#!/usr/bin/env python3
"""
Finalize the bootstrap baseline (v0.3.3). Aggregates reports/bootstrap-baseline/
cases/*.json into an immutable baseline snapshot + fingerprint + distributions +
invariant snapshot. No model calls.

  python3 finalize_baseline.py
"""
import json, os, collections
from fingerprint import build as fp_build

HERE = os.path.dirname(os.path.abspath(__file__))
EVAL = os.path.dirname(HERE)
BASE = os.path.join(EVAL, "reports", "bootstrap-baseline")
CASES = os.path.join(BASE, "cases")

CRITICAL_PROPS = ["P02", "P04", "P06", "P11", "P12"]

def main():
    recs = [json.load(open(os.path.join(CASES, f), encoding="utf-8"))
            for f in sorted(os.listdir(CASES)) if f.endswith(".json")]
    n = len(recs)
    ok_exec = sum(1 for r in recs if r.get("stage1_ok") and r.get("stage2_ok"))

    prop_dist = collections.defaultdict(lambda: collections.Counter())
    ecode_dist = collections.Counter()
    module_dist = collections.Counter()
    crit_present = collections.Counter()
    commit = recs[0].get("git_commit", "UNKNOWN") if recs else "UNKNOWN"

    items = []
    for r in recs:
        for p, v in (r.get("verdicts") or {}).items():
            prop_dist[p][v] += 1
        for e in (r.get("flagged_ecodes") or []):
            ecode_dist[e] += 1
        for m in (r.get("module_trace_heuristic") or []):
            module_dist[m] += 1
        for p in CRITICAL_PROPS:
            v = (r.get("verdicts") or {}).get(p)
            if v:
                crit_present[f"{p}:{v}"] += 1
        items.append({"case_id": r["case_id"], "family": r.get("family"),
                      "verdicts": r.get("verdicts", {}),
                      "flagged_ecodes": r.get("flagged_ecodes", []),
                      "critical_flags": r.get("critical_flags", []),
                      "module_trace_heuristic": r.get("module_trace_heuristic", []),
                      "stage1_ok": r.get("stage1_ok"), "stage2_ok": r.get("stage2_ok")})

    snapshot = {"label": "bootstrap-baseline", "judge_type": "BOOTSTRAP",
                "skill_version": "baseline", "baseline_commit": commit,
                "n_cases": n, "items": items}
    json.dump(snapshot, open(os.path.join(BASE, "baseline-snapshot.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    fp = fp_build(CASES)
    fp["baseline_commit"] = commit
    json.dump(fp, open(os.path.join(BASE, "FINGERPRINT.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    dist = {
        "n_cases": n, "successful_execution": ok_exec, "failed_execution": n - ok_exec,
        "per_property": {p: dict(c) for p, c in prop_dist.items()},
        "per_ecode": dict(ecode_dist),
        "module_activation_heuristic": dict(module_dist),
        "critical_property_snapshot": dict(crit_present),
        "families": dict(collections.Counter(r.get("family") for r in recs)),
    }
    json.dump(dist, open(os.path.join(BASE, "distributions.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    print(json.dumps({"n": n, "ok_exec": ok_exec, "fingerprint": fp,
                      "distributions": dist}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
