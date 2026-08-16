#!/usr/bin/env python3
"""
Ablation sweep runner (v0.4.1). RESUMABLE + paced + backoff.

For each (ablation, case) pair:
  1. re-judge the STORED baseline output (no skill call) on the diagnostic props
  2. run the ABLATED skill (paced + backoff retry) on the same prompt
  3. judge the ablated output on the same props
  4. persist an immutable per-pair delta file (skip if it already exists)

Baseline outputs are the immutable 58-case bootstrap baseline (reused, not
re-run). judge_type = BOOTSTRAP (LOW independence). No fabrication: a failed
skill run persists nothing and is retried on the next pass.

  python3 ablation_sweep.py            # runs the pilot diagonal
"""
import json, os, sys, time, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
RP = os.path.dirname(HERE)                     # research-protocol
TESTS = os.path.dirname(RP)
REPO = os.path.dirname(TESTS)
sys.path.insert(0, os.path.join(TESTS, "evaluation-v0.3", "harness"))
from bootstrap_judge import judge_output, BOOTSTRAP   # noqa
from ablate import make_variant                        # noqa

MANIFEST = json.load(open(os.path.join(RP, "fixtures" if os.path.exists(os.path.join(RP,"fixtures")) else "", "full-manifest.json"), encoding="utf-8")) if False else \
           json.load(open(os.path.join(TESTS, "evaluation-v0.3", "fixtures", "regression", "full-manifest.json"), encoding="utf-8"))
BASECASES = os.path.join(TESTS, "evaluation-v0.3", "reports", "bootstrap-baseline", "cases")
VARIANTS = os.path.join(RP, "variants")
OUTDIR = os.path.join(REPO, "reports", "v0.4", "ablation", "per-case")

# each ablation on its single most-diagnostic case + the property it targets
PILOT = [
    ("A1", "NR-01",  ["P02"]),
    ("A2", "DF-01",  ["P09"]),
    ("A3", "RWB-24", ["P06"]),
    ("A4", "RWB-16", ["P07"]),
    ("A5", "RWB-22", ["P08"]),
    ("A6", "FO-01",  ["P04", "P05"]),
    ("A7", "AS-01",  ["P07", "P05"]),
]

def prompt_for(cid):
    for it in MANIFEST["items"]:
        if it["case_id"] == cid:
            return it["prompt"]
    return None

def baseline_output(cid):
    p = os.path.join(BASECASES, cid + ".json")
    if os.path.exists(p):
        return json.load(open(p, encoding="utf-8")).get("output", "")
    return ""

def run_skill(prompt, sysfile, timeout=170, retries=3):
    cmd = ["claude", "-p", prompt, "--append-system-prompt-file", sysfile,
           "--output-format", "text"]
    for attempt in range(retries):
        t0 = time.time()
        try:
            r = subprocess.run(cmd, capture_output=True, text=True,
                               timeout=timeout, stdin=subprocess.DEVNULL)
            out, secs = r.stdout.strip(), time.time() - t0
            if r.returncode == 0 and out and secs > 8:
                return out
        except subprocess.TimeoutExpired:
            pass
        back = 25 * (attempt + 1)
        print(f"    skill fast-fail, backoff {back}s", file=sys.stderr)
        time.sleep(back)
    return ""

def main():
    os.makedirs(OUTDIR, exist_ok=True)
    for abl, cid, props in PILOT:
        tag = f"{abl}__{cid}"
        outp = os.path.join(OUTDIR, tag + ".json")
        if os.path.exists(outp):
            print(f"[{tag}] SKIP (done)", file=sys.stderr); continue
        prompt = prompt_for(cid)
        b_out = baseline_output(cid)
        if not prompt or not b_out:
            print(f"[{tag}] MISSING prompt/baseline -> skip", file=sys.stderr); continue
        variant = make_variant(abl, VARIANTS)["path"]

        # 1. re-judge stored baseline output on diagnostic props
        bj = judge_output(prompt, b_out, props, mode=BOOTSTRAP, case_id=cid)
        if not bj["ok"]:
            print(f"[{tag}] baseline judge failed -> retry next pass", file=sys.stderr)
            time.sleep(30); continue
        time.sleep(12)
        # 2. run ablated skill
        a_out = run_skill(prompt, variant)
        if not a_out:
            print(f"[{tag}] ablated skill failed -> retry next pass", file=sys.stderr)
            time.sleep(20); continue
        time.sleep(12)
        # 3. judge ablated output
        aj = judge_output(prompt, a_out, props, mode=BOOTSTRAP, case_id=cid)
        if not aj["ok"]:
            print(f"[{tag}] ablated judge failed -> retry next pass", file=sys.stderr)
            time.sleep(20); continue

        delta = {p: {"baseline": bj["verdicts"].get(p), "ablated": aj["verdicts"].get(p)}
                 for p in props}
        rec = {"ablation": abl, "case_id": cid, "diagnostic_props": props,
               "judge_type": "BOOTSTRAP", "independence": "LOW",
               "baseline_verdicts": bj["verdicts"], "ablated_verdicts": aj["verdicts"],
               "baseline_ecodes": bj["flagged_ecodes"], "ablated_ecodes": aj["flagged_ecodes"],
               "delta": delta,
               "new_ecodes": sorted(set(aj["flagged_ecodes"]) - set(bj["flagged_ecodes"])),
               "ablated_output": a_out,
               "provenance": aj["provenance"]}
        json.dump(rec, open(outp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"[{tag}] delta={delta} new_ecodes={rec['new_ecodes']}", file=sys.stderr)
        time.sleep(12)
    print("ABLATION SWEEP PASS COMPLETE", file=sys.stderr)

if __name__ == "__main__":
    main()
