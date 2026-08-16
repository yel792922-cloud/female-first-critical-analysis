#!/usr/bin/env python3
"""
Expression metrics analyzer (v0.3.4). DETERMINISTIC proxies only.

Measures user-facing surface complexity of skill outputs. Like the v0.3
deterministic layer, these are CANDIDATE SIGNALS, not final verdicts: the
substantive-vs-defensive-surplus call needs semantic judgment. Density figures
are per-1000-characters unless noted.

  python3 expression_metrics.py --dir <cases_dir>     # aggregate + per-case
  python3 expression_metrics.py --text-file f.txt     # single text
"""
import argparse, json, os, re, glob, statistics

# --- proxy pattern banks (Chinese; candidate signals only) ---
DEFENSIVE = [r"并不意味着", r"不意味着", r"不能理解为", r"不能简单地?认为", r"不是说",
             r"并非", r"需要强调", r"必须指出", r"要注意的是", r"不能据此",
             r"不代表", r"这并不", r"也不能推出", r"不应被理解", r"不等于说"]
HEDGE = [r"可能", r"也许", r"或许", r"某种程度上", r"在一定意义上", r"一定程度上",
         r"未必", r"往往", r"通常", r"倾向于", r"不能简单", r"需要谨慎", r"不宜",
         r"似乎", r"在某些情况下"]
MODULE_NARRATION = [r"从[^，。；\n]{0,6}(角度|层面|来看|维度)", r"在[^，。；\n]{0,6}(层面|维度)上",
                    r"(agency|能动性?|结构|权力|交叉性|阶级|责任|比较)(轴|维度)"]
# canonical distinctions -> redundancy if a distinction appears >1x
DISTINCTIONS = {
    "choice_neq_liberation": r"(选择|choice)[^。\n]{0,10}(不等于|≠|不必然|不代表|不意味)[^。\n]{0,10}(自由|解放|liberation)",
    "constraint_neq_noagency": r"(结构|约束|受限)[^。\n]{0,12}(不|≠)[^。\n]{0,6}(没有|无|缺乏)?[^。\n]{0,6}(agency|能动)",
    "structure_neq_exemption": r"(结构)[^。\n]{0,12}(不)[^。\n]{0,6}(免除|取消|抹除|等于免责)",
    "empower_neq_liberation": r"(赋权|empowerment)[^。\n]{0,10}(不等于|≠|不是)[^。\n]{0,10}(解放|liberation)",
}

def count(patterns, text):
    return sum(len(re.findall(p, text)) for p in patterns)

def measure(text):
    n = max(len(text), 1)
    sents = [s for s in re.split(r"[。！？\n]", text) if s.strip()]
    per1k = lambda c: round(c / n * 1000, 2)
    defc = count(DEFENSIVE, text)
    hedgec = count(HEDGE, text)
    modc = count(MODULE_NARRATION, text)
    dist_hits = {k: len(re.findall(p, text)) for k, p in DISTINCTIONS.items()}
    redundant = {k: v for k, v in dist_hits.items() if v > 1}
    return {
        "chars": n, "sentences": len(sents),
        "defensive_count": defc, "defensive_density_per1k": per1k(defc),
        "hedge_count": hedgec, "hedge_density_per1k": per1k(hedgec),
        "module_narration_count": modc, "module_narration_per1k": per1k(modc),
        "distinction_hits": dist_hits,
        "redundant_distinctions": redundant,
        "redundant_distinction_rate": round(sum(max(v-1,0) for v in dist_hits.values()) / max(len(sents),1) * 100, 2),
    }

def agg(rows):
    def stat(key):
        vals = [r["metrics"][key] for r in rows]
        return {"mean": round(statistics.mean(vals), 2),
                "median": round(statistics.median(vals), 2),
                "p90": round(sorted(vals)[max(0, int(len(vals)*0.9)-1)], 2),
                "max": max(vals)}
    return {k: stat(k) for k in ["chars", "defensive_density_per1k",
            "hedge_density_per1k", "module_narration_per1k"]}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir"); ap.add_argument("--text-file")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.text_file:
        print(json.dumps(measure(open(a.text_file, encoding="utf-8").read()), ensure_ascii=False, indent=2)); return
    rows = []
    for f in sorted(glob.glob(os.path.join(a.dir, "*.json"))):
        r = json.load(open(f, encoding="utf-8"))
        out = r.get("output", "")
        if not out: continue
        rows.append({"case_id": r.get("case_id"), "family": r.get("family"),
                     "metrics": measure(out)})
    report = {"n": len(rows), "aggregate": agg(rows), "per_case": rows}
    if a.json:
        print(json.dumps(report, ensure_ascii=False, indent=2)); return
    print(f"n={report['n']} outputs")
    print("aggregate:", json.dumps(report["aggregate"], ensure_ascii=False))
    print("\ntop defensive-density cases:")
    for r in sorted(rows, key=lambda x: -x["metrics"]["defensive_density_per1k"])[:6]:
        m = r["metrics"]
        print(f"  {r['case_id']:8} defv/1k={m['defensive_density_per1k']:5} hedge/1k={m['hedge_density_per1k']:5} "
              f"mod/1k={m['module_narration_per1k']:5} chars={m['chars']} redund={m['redundant_distinctions']}")
    print("\ntop module-narration cases:")
    for r in sorted(rows, key=lambda x: -x["metrics"]["module_narration_per1k"])[:6]:
        m = r["metrics"]
        print(f"  {r['case_id']:8} mod/1k={m['module_narration_per1k']:5} chars={m['chars']}")

if __name__ == "__main__":
    main()
