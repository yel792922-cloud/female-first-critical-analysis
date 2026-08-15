#!/usr/bin/env python3
"""
Full bootstrap baseline builder (v0.3.3). RESUMABLE.

For each case in full-manifest.json:
  stage-1  run the CURRENT skill via `claude -p --append-system-prompt-file SKILL.md`
  stage-2  judge the output with the BOOTSTRAP judge (bootstrap_judge.py)
Writes one JSON per case to reports/bootstrap-baseline/cases/<id>.json immediately
(so partial progress persists). Skips cases already done.

judge_type = BOOTSTRAP (same vendor/family). Behavior baseline only, NOT
calibration. Run in background:
  python3 build_baseline.py  [--model X]
"""
import argparse, json, os, subprocess, time, hashlib, re, sys
from bootstrap_judge import judge_output, BOOTSTRAP, _git_commit

HERE = os.path.dirname(os.path.abspath(__file__))
EVAL = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(EVAL))
SKILL = os.path.join(REPO, "SKILL.md")
MANIFEST = os.path.join(EVAL, "fixtures", "regression", "full-manifest.json")
OUTDIR = os.path.join(EVAL, "reports", "bootstrap-baseline", "cases")

# property set to judge, per family (kept small + uniform for a behavior baseline)
FAM_PROPS = {
    "real-world": ["P02", "P04", "P05", "P06", "P10"],
    "framing-order": ["P04", "P05", "P06"],
    "architecture-stress": ["P05", "P06", "P07"],
    "activation": ["P02", "P04", "P14", "P15"],
    "epistemic-system": ["P02", "P10", "P11", "P12"],
}

MOD_SIG = {  # heuristic activation trace (labeled heuristic, not authoritative)
    "null-result": r"证据不足|不足以判断|尚不足|pattern|个案.*不能",
    "agency": r"能动|agency|自主|退出能力|选择空间",
    "power-structure": r"结构|权力|制度|凝视",
    "responsibility": r"责任|担责|问责",
    "intersectionality": r"阶级|交叉|城乡|户籍|种族|移民",
    "class-position": r"阶级|职位|雇主|位置权力",
    "comparison": r"男性也|对照|比较|whataboutism|derailment",
    "baseline-interrogation": r"向下|上/下|基准|谁(定义|说了算)",
    "parallel-analysis": r"与此同时|并存|同时成立",
}

def _one_skill(prompt, model, timeout=150):
    cmd = ["claude", "-p", prompt, "--append-system-prompt-file", SKILL,
           "--output-format", "text"]
    if model:
        cmd += ["--model", model]
    t0 = time.time()
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                           stdin=subprocess.DEVNULL)
        return (r.returncode == 0, r.stdout.strip(), round(time.time()-t0, 1))
    except subprocess.TimeoutExpired:
        return (False, "", timeout)

def run_skill(prompt, model, timeout=150, retries=3):
    """Retry on fast-fail (rate limit) with backoff; a genuine call takes ~30-60s,
    a rate-limited fast-fail returns in a few seconds -> back off and retry."""
    for attempt in range(retries):
        ok, out, secs = _one_skill(prompt, model, timeout)
        if ok and out and secs > 8:      # a real analysis, not a fast-fail
            return (ok, out, secs)
        back = 20 * (attempt + 1)
        print(f"    skill attempt {attempt+1} fast-fail ({secs}s), backoff {back}s",
              file=sys.stderr)
        time.sleep(back)
    return (ok, out, secs)

def heuristic_trace(text):
    return sorted([m for m, sig in MOD_SIG.items() if re.search(sig, text)])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=None)
    a = ap.parse_args()
    os.makedirs(OUTDIR, exist_ok=True)
    manifest = json.load(open(MANIFEST, encoding="utf-8"))
    commit = _git_commit()
    done = set(f[:-5] for f in os.listdir(OUTDIR) if f.endswith(".json"))
    total = len(manifest["items"])
    for idx, it in enumerate(manifest["items"], 1):
        cid = it["case_id"]
        if cid in done:
            print(f"[{idx}/{total}] {cid} SKIP (done)", file=sys.stderr); continue
        props = FAM_PROPS.get(it["family"], ["P02", "P04", "P05", "P06", "P10"])
        ok1, out, s1 = run_skill(it["prompt"], a.model)
        rec = {"case_id": cid, "family": it["family"], "prompt": it["prompt"],
               "prompt_version": "full-manifest@v0.3.3",
               "skill_version": "current", "git_commit": commit,
               "fixture_hash": hashlib.sha256(it["prompt"].encode()).hexdigest()[:12],
               "judge_type": "BOOTSTRAP",
               "stage1_ok": ok1, "stage1_secs": s1,
               "output": out, "module_trace_heuristic": heuristic_trace(out)}
        if ok1 and out:
            jr = judge_output(it["prompt"], out, props, mode=BOOTSTRAP,
                              model=a.model, skill_version="current", case_id=cid)
            rec.update({"stage2_ok": jr["ok"], "verdicts": jr["verdicts"],
                        "flagged_ecodes": jr["flagged_ecodes"],
                        "critical_flags": jr["critical_flags"],
                        "judge_model_alias": jr["provenance"]["judge_model_alias"],
                        "model_version": jr["provenance"]["model_version"],
                        "temperature": jr["provenance"]["temperature"],
                        "timestamp": jr["provenance"]["timestamp"]})
        else:
            rec.update({"stage2_ok": False, "verdicts": {}, "flagged_ecodes": [],
                        "critical_flags": [], "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
        # only persist a case when stage-1 actually produced an analysis, so
        # rate-limited fast-fails are retried on the next resumable pass
        if ok1 and out:
            json.dump(rec, open(os.path.join(OUTDIR, cid + ".json"), "w", encoding="utf-8"),
                      ensure_ascii=False, indent=2)
        print(f"[{idx}/{total}] {cid} s1={ok1}/{s1}s judge={rec.get('stage2_ok')} "
              f"verdicts={rec.get('verdicts')}", file=sys.stderr)
        time.sleep(12)   # pace to stay under the nested-CLI rate limit
    print("BASELINE BUILD PASS COMPLETE", file=sys.stderr)

if __name__ == "__main__":
    main()
