#!/usr/bin/env python3
"""
Regression diff (v0.3.2, BOOTSTRAP mode). Compares two snapshots (BASELINE vs
CURRENT) per property. No judge calls -- pure diff of stored verdicts.

HARD STOP: in BOOTSTRAP mode this NEVER prints readiness. It prints only
BOOTSTRAP REGRESSION COMPLETE or BOOTSTRAP REGRESSION FAILED. Critical
properties/E-codes are reported BEFORE any total.

  python3 regression_diff.py --baseline B.json --current C.json [--json]
"""
import argparse, json

RANK = {"FAIL": 0, "PARTIAL": 1, "N-A": 2, "PASS": 3}
CRITICAL_PROPS = ["P02", "P04", "P06", "P11", "P12"]
CRITICAL_ECODES = ["E01", "E05", "E11", "E12", "E13", "E14", "E17"]


def classify(base_v, cur_v):
    if base_v == cur_v:
        return "unchanged"
    if base_v is None:
        return "new-activation"
    if cur_v is None:
        return "removed-activation"
    b, c = RANK.get(base_v, -1), RANK.get(cur_v, -1)
    if c > b:
        return "improvement"
    if c < b:
        return "regression"
    return "changed"


def diff(baseline, current):
    b = {i["case_id"]: i for i in baseline["items"]}
    c = {i["case_id"]: i for i in current["items"]}
    rows, crit_regressions, crit_ecode_new = [], [], []
    for cid in sorted(set(b) | set(c)):
        bi, ci = b.get(cid), c.get(cid)
        bv = (bi or {}).get("verdicts", {})
        cv = (ci or {}).get("verdicts", {})
        for p in sorted(set(bv) | set(cv)):
            k = classify(bv.get(p), cv.get(p))
            if k != "unchanged":
                rows.append((cid, p, bv.get(p), cv.get(p), k))
                if p in CRITICAL_PROPS and k == "regression":
                    crit_regressions.append((cid, p, bv.get(p), cv.get(p)))
        be = set((bi or {}).get("flagged_ecodes", []))
        ce = set((ci or {}).get("flagged_ecodes", []))
        for e in sorted(ce - be):
            rows.append((cid, e, "absent", "flagged", "new-ecode"))
            if e in CRITICAL_ECODES:
                crit_ecode_new.append((cid, e))
        for e in sorted(be - ce):
            rows.append((cid, e, "flagged", "absent", "removed-ecode"))
    return rows, crit_regressions, crit_ecode_new


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--current", required=True)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    baseline = json.load(open(a.baseline, encoding="utf-8"))
    current = json.load(open(a.current, encoding="utf-8"))

    # hard mode guard
    if baseline.get("judge_type") != "BOOTSTRAP" or current.get("judge_type") != "BOOTSTRAP":
        print("refusing: snapshots not both BOOTSTRAP judge_type"); return

    rows, crit_reg, crit_new = diff(baseline, current)
    counts = {}
    for *_, k in rows:
        counts[k] = counts.get(k, 0) + 1
    failed = bool(crit_reg or crit_new)

    if a.json:
        print(json.dumps({"rows": rows, "critical_regressions": crit_reg,
                          "critical_new_ecodes": crit_new, "counts": counts,
                          "verdict": "BOOTSTRAP REGRESSION FAILED" if failed
                          else "BOOTSTRAP REGRESSION COMPLETE"}, ensure_ascii=False, indent=2))
        return

    print("== BOOTSTRAP REGRESSION (judge_type=BOOTSTRAP, independence=LOW) ==")
    print(f"baseline={baseline.get('skill_version')}  current={current.get('skill_version')}")
    print("\n--- CRITICAL DELTA (reported before any total) ---")
    print(f"critical-property regressions: {crit_reg if crit_reg else 'none'}")
    print(f"critical new E-codes:          {crit_new if crit_new else 'none'}")
    print("\n--- all property/ecode changes ---")
    for cid, p, bv, cv, k in rows:
        print(f"  {cid:12} {p:5} {str(bv):8} -> {str(cv):8}  [{k}]")
    print(f"\ncounts: {counts}")
    print("\nNOTE: BOOTSTRAP judge (same-family, non-independent). Detects BEHAVIOR")
    print("CHANGE only; does NOT independently verify reasoning quality.")
    print(f"\nVERDICT: {'BOOTSTRAP REGRESSION FAILED' if failed else 'BOOTSTRAP REGRESSION COMPLETE'}")
    # Hard stop: never emit pilot-readiness in bootstrap mode.

if __name__ == "__main__":
    main()
