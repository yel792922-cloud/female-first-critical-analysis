#!/usr/bin/env python3
"""
Real judge SMOKE + REPRODUCIBILITY harness (v0.3.2).

Invokes a REAL model via the `claude` CLI in print mode (-p) as a Layer-2
property judge, on the 3 smoke fixtures, N times each. Records full provenance.

IMPORTANT / honesty:
  - The reachable model is a Claude model = SAME VENDOR/FAMILY as the skill
    author -> SELF-JUDGING / BOOTSTRAP. Results are tagged judge_type accordingly
    and MUST NOT be treated as independent evaluator calibration.
  - The model is addressed by an ALIAS, not an immutable pinned version, so
    model_version is recorded UNKNOWN and reproducible=false.
  - This harness proves the CHAIN works (endpoint->adapter->structured verdict->
    report) and measures semantic variability. It does NOT certify readiness.

Usage:
  python3 real_judge_smoke.py --repeats 3 [--model <alias>]
"""
import argparse, json, os, subprocess, sys, time, hashlib, re

HERE = os.path.dirname(os.path.abspath(__file__))
EVAL_ROOT = os.path.dirname(HERE)
SMOKE = os.path.join(EVAL_ROOT, "fixtures", "smoke")

JUDGE_SYSTEM = (
    "You are a reasoning-property judge for a female-first critical-analysis skill. "
    "Score ONLY the listed properties for the ANSWER about the CASE. "
    "Score REASONING QUALITY, not political alignment: a feminist framing earns no "
    "bonus and a non-feminist framing earns no penalty; apply the same evidence and "
    "inference bar. Consider E-codes: E01 forced-oppression (a strong structural/"
    "patriarchy conclusion past the evidence), E11 strawman (rebuilding a view as a "
    "version it disclaims), E13 aggregate->individual causal leap. "
    "Output ONLY a compact JSON object, no prose, no markdown fences, of the form: "
    '{"verdicts":{"P02":"PASS|PARTIAL|FAIL|N-A"},"flagged_ecodes":["E11"],'
    '"evidence":{"P02":"short reason"}}'
)

def fixture_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]

def build_prompt(fx):
    return (f"CASE:\n{fx['case']}\n\nANSWER:\n{fx['answer']}\n\n"
            f"PROPERTIES TO SCORE: {', '.join(fx['properties_to_check'])}\n"
            f"Return ONLY the JSON object.")

def call_claude(prompt, model, timeout=120):
    cmd = ["claude", "-p", prompt, "--output-format", "text",
           "--append-system-prompt", JUDGE_SYSTEM]
    if model:
        cmd += ["--model", model]
    t0 = time.time()
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return {"ok": r.returncode == 0, "stdout": r.stdout.strip(),
                "stderr": r.stderr.strip()[:400], "secs": round(time.time()-t0, 1)}
    except subprocess.TimeoutExpired:
        return {"ok": False, "stdout": "", "stderr": "TIMEOUT", "secs": timeout}

def extract_json(text):
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        return None

def run(repeats, model):
    fixtures = sorted(f for f in os.listdir(SMOKE) if f.endswith(".json"))
    runs = []
    for fn in fixtures:
        fx = json.load(open(os.path.join(SMOKE, fn), encoding="utf-8"))
        prompt = build_prompt(fx)
        for i in range(repeats):
            res = call_claude(prompt, model)
            parsed = extract_json(res["stdout"]) if res["ok"] else None
            runs.append({
                "provenance": {
                    "adapter": "claude-cli-print",
                    "judge_type": "same_vendor_family__BOOTSTRAP",
                    "independence_level": "LOW (same vendor; alias model)",
                    "judge_model_alias": model or "DEFAULT",
                    "model_version": "UNKNOWN (alias, not pinned)",
                    "prompt_version": "real_judge_smoke.py@v0.3.2",
                    "runtime": "UNKNOWN",
                    "temperature": "UNKNOWN (not exposed by CLI)",
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "case_id": fx["id"],
                    "fixture_hash": fixture_hash(fx["case"] + fx["answer"]),
                    "reproducible": False,
                    "mock": False,
                    "run_index": i + 1,
                },
                "raw_ok": res["ok"], "secs": res["secs"],
                "parsed": parsed,
                "raw_head": (res["stdout"][:200] if res["ok"] else res["stderr"]),
                "reference_expectation": fx.get("reference_expectation"),
            })
            print(f"[{fx['id']} run{i+1}] ok={res['ok']} {res['secs']}s parsed={'yes' if parsed else 'NO'}",
                  file=sys.stderr)
    return runs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repeats", type=int, default=3)
    ap.add_argument("--model", default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    runs = run(a.repeats, a.model)
    blob = json.dumps(runs, ensure_ascii=False, indent=2)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(blob)
        print(f"wrote {a.out}", file=sys.stderr)
    else:
        print(blob)

if __name__ == "__main__":
    main()
