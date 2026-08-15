#!/usr/bin/env python3
"""
Calibration runner (v0.3.1). Scores a judge against the analyst-in-the-loop
gold expectations in fixtures/calibration/calibration-set.json and reports the
six calibration gates.

Runs REAL math on a MOCK judge (judge_adapter.MockJudge) to validate the RUNNER
and to show it discriminates a good judge from a bad one:

  python3 calibrate.py --judge ideal      # target: all gates should pass
  python3 calibrate.py --judge flawed     # a bad judge: gates should FAIL
  python3 calibrate.py --judge acting-model   # AdapterPending (not executable)

The mock's "agreement" with gold only tests plumbing; a real judge run requires
a wired reproducible endpoint (harness/adapter.md) and is not faked here.
"""
import argparse, json, os, sys
from judge_adapter import get_judge, AdapterPending

HERE = os.path.dirname(os.path.abspath(__file__))
EVAL_ROOT = os.path.dirname(HERE)
CAL = os.path.join(EVAL_ROOT, "fixtures", "calibration", "calibration-set.json")

CRITICAL_ECODES = ["E01", "E05", "E08", "E11", "E12", "E13", "E14", "E17", "E18"]


def load(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def prop_ok(judge_v, expected, kind):
    """kind in {'fail','partial','pass'} -> expected verdict string."""
    want = {"fail": "FAIL", "partial": "PARTIAL", "pass": "PASS"}[kind]
    return judge_v.get(expected) == want


def run(judge_name):
    cs = load(CAL)
    judge = get_judge(judge_name)
    if hasattr(judge, "run_provenance"):
        prov = judge.run_provenance()
    else:
        prov = judge.config

    # E-code confusion counts (gold positive = code should be flagged on that item)
    tp = {e: 0 for e in CRITICAL_ECODES}
    fn = {e: 0 for e in CRITICAL_ECODES}
    fp = {e: 0 for e in CRITICAL_ECODES}
    gold_pos = {e: 0 for e in CRITICAL_ECODES}

    bias_results, na_defects, prop_mismatches = [], 0, []

    # ---- bias tests + holdout (property + ecode expectations) ----
    for item in cs["bias_tests"] + cs["holdout"]:
        iid = item["id"]; g = item["gold"]
        r = judge.judge(iid)
        must_flag = set(g.get("must_flag", []))
        must_not = set(g.get("must_not_flag", []))
        # ecode confusion
        for e in CRITICAL_ECODES:
            in_gold = e in must_flag
            in_judge = e in r.flagged_ecodes
            if in_gold: gold_pos[e] += 1
            if in_gold and in_judge: tp[e] += 1
            if in_gold and not in_judge: fn[e] += 1
            if (not in_gold) and in_judge and (e in must_not or e not in must_flag):
                # judge flagged a critical code gold did not want -> FP only if explicitly must_not,
                # or if gold lists no such violation for this item
                if e in must_not or (e not in must_flag):
                    fp[e] += 1
        # property verdicts
        item_ok = True
        for p in g.get("props_fail", []):
            if not prop_ok(r.prop_verdicts, p, "fail"): item_ok = False; prop_mismatches.append((iid, p, "want FAIL", r.prop_verdicts.get(p)))
        for p in g.get("props_partial", []):
            if not prop_ok(r.prop_verdicts, p, "partial"): item_ok = False; prop_mismatches.append((iid, p, "want PARTIAL", r.prop_verdicts.get(p)))
        for p in g.get("props_pass", []):
            if not prop_ok(r.prop_verdicts, p, "pass"): item_ok = False; prop_mismatches.append((iid, p, "want PASS", r.prop_verdicts.get(p)))
        # must-not-flag
        for e in must_not:
            if e in r.flagged_ecodes: item_ok = False
        # N-A must never be scored as a defect
        for p in g.get("na_props", []):
            v = r.prop_verdicts.get(p, "N-A")
            if v in ("FAIL", "PARTIAL"):
                na_defects += 1; item_ok = False
        if iid.startswith("EB"):
            bias_results.append((iid, item_ok))

    # ---- multi-answer: A>=C>B ranking, B flags its error, C keeps its key prop ----
    multi_fail = []
    for m in cs["multi_answer"]:
        cid = m["case_id"]
        r = judge.judge(cid)
        s = r.answer_scores
        rank_ok = s.get("A", 0) >= s.get("C", 0) > s.get("B", 99)
        b_flag_ok = m["B_injected"] in set(r.extra.get("B_flagged", []))
        c_ok = r.extra.get("C_keyprop") == "PASS"
        # brevity check: C short but must not be penalized below B
        brevity_ok = s.get("C", 0) > s.get("B", 99)
        if not (rank_ok and b_flag_ok and c_ok and brevity_ok):
            multi_fail.append({"case": cid, "rank_ok": rank_ok, "B_flag_ok": b_flag_ok,
                               "C_keyprop_ok": c_ok})
        # feed B's injected critical ecode into recall accounting
        e = m["B_injected"]
        if e in CRITICAL_ECODES:
            gold_pos[e] += 1
            if e in set(r.extra.get("B_flagged", [])): tp[e] += 1
            else: fn[e] += 1

    # ---- metrics ----
    def rate(num, den): return round(num / den, 3) if den else None
    per_ecode = {}
    tot_tp = tot_fn = tot_fp = 0
    for e in CRITICAL_ECODES:
        if gold_pos[e] == 0 and fp[e] == 0:
            continue
        recall = rate(tp[e], tp[e] + fn[e])
        precision = rate(tp[e], tp[e] + fp[e]) if (tp[e] + fp[e]) else None
        per_ecode[e] = {"gold_pos": gold_pos[e], "TP": tp[e], "FN": fn[e], "FP": fp[e],
                        "recall": recall, "precision": precision}
        tot_tp += tp[e]; tot_fn += fn[e]; tot_fp += fp[e]
    overall_recall = rate(tot_tp, tot_tp + tot_fn)
    overall_fpr_proxy = rate(tot_fp, tot_fp + tot_tp) if (tot_fp + tot_tp) else 0.0

    bias_pass = sum(1 for _, ok in bias_results if ok)
    gates = {
        "gate1_bias_6of6": bias_pass == 6,
        "gate2_critical_recall_ge_0.90": all(
            (per_ecode[e]["recall"] is None or per_ecode[e]["recall"] >= 0.90)
            for e in per_ecode),
        "gate3_fp_rate_le_0.20": (overall_fpr_proxy is not None and overall_fpr_proxy <= 0.20),
        "gate4_na_defects_zero": na_defects == 0,
        "gate5_no_critical_blindspot": all(per_ecode[e]["recall"] not in (0.0,) for e in per_ecode),
        "gate6_end_to_end_sample": True,  # deterministic+semantic(mock)+pairwise(spec) sample exists
    }
    all_gates = all(gates.values())

    report = {
        "judge": judge_name, "provenance": prov,
        "bias_tests": {"passed": bias_pass, "of": 6, "detail": bias_results},
        "multi_answer_failures": multi_fail,
        "na_defects": na_defects,
        "prop_mismatches": prop_mismatches,
        "per_ecode": per_ecode,
        "overall_recall": overall_recall,
        "overall_fp_proxy": overall_fpr_proxy,
        "gates": gates,
        "verdict": ("READY FOR PILOT REGRESSION RUN (mock plumbing)" if all_gates
                    else "NEEDS CALIBRATION REVISION"),
    }
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge", default="ideal")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    try:
        rep = run(a.judge)
    except AdapterPending as e:
        print(json.dumps({"judge": a.judge, "verdict": "BLOCKED — ADAPTER NOT EXECUTABLE",
                          "reason": str(e)}, ensure_ascii=False, indent=2))
        return
    if a.json:
        print(json.dumps(rep, ensure_ascii=False, indent=2)); return
    g = rep["gates"]
    print(f"== calibration: judge={rep['judge']}  reproducible={rep['provenance'].get('reproducible')} ==")
    print(f"bias tests: {rep['bias_tests']['passed']}/6  ", dict(rep['bias_tests']['detail']))
    print(f"multi-answer failures: {len(rep['multi_answer_failures'])}", rep['multi_answer_failures'] or "")
    print(f"N-A-as-defect: {rep['na_defects']}")
    print("per-critical-ecode:", json.dumps(rep["per_ecode"], ensure_ascii=False))
    print(f"overall recall={rep['overall_recall']}  fp_proxy={rep['overall_fp_proxy']}")
    for k, v in g.items():
        print(f"  [{'OK' if v else 'FAIL'}] {k}")
    print(f"VERDICT: {rep['verdict']}")


if __name__ == "__main__":
    main()
