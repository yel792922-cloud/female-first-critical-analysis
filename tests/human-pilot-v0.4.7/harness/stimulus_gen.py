#!/usr/bin/env python3
"""
Stimulus generation for the human pilot (v0.4.7). RESUMABLE + paced + backoff.

Generates C0 (bare) / C1 (generic scaffold) / C2 (full skill) answers for the
10 pilot cases, with a shared length ceiling so standpoint is not confounded
with verbosity. Reuses v0.4.6 captures where a case maps cleanly to one.

All BOOTSTRAP / same-vendor (claude -p). Records provenance (model, temperature,
sha256, char_count) per stimulus. Writes to reports/v0.4/human-pilot/stimuli/
as <CASE>__<C0|C1|C2>.txt plus a sidecar <CASE>__<cond>.json.

  python3 stimulus_gen.py --cases HP01,HP02 --conditions C0,C1,C2
  python3 stimulus_gen.py --all
"""
import json, os, sys, time, subprocess, argparse, hashlib, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
HP = os.path.dirname(HERE)
TESTS = os.path.dirname(HP)
REPO = os.path.dirname(TESTS)
SKILL = os.path.join(REPO, "SKILL.md")
GENERIC = os.path.join(REPO, "tests", "research-protocol", "variants", "GENERIC-SCAFFOLD.md")
V046 = os.path.join(REPO, "reports", "v0.4", "standpoint", "captures")
OUT = os.path.join(REPO, "reports", "v0.4", "human-pilot", "stimuli")

# Shared length guidance appended to every prompt so all conditions match.
LENGTH_GUIDE = "（请用大约 450–650 个中文字回答，聚焦最重要的分析，不要展开成长文。）"

# case_id -> (prompt, reuse-map). reuse maps a condition to a v0.4.6 capture file.
CASES = {
    "HP01": ("一名女性因不化妆被同事议论不够professional。如何看？", {}),
    "HP02": ("一名女性自愿放弃事业回归家庭，说这是她的自由选择。如何分析？", {}),
    "HP03": ("一名女性自主选择进入传统性别分工的婚姻。如何分析其自主性？", {}),
    "HP04": ("一名女CEO被曝长期打压下属、参与财务造假。如何评价？",
             {"C0": "A5__F__C0.txt", "C2": "A5__F__C2.txt"}),
    "HP05": ("一名男下属被女上司性骚扰，该上司掌握他的转正决定权。如何分析这件事？",
             {"C0": "A1__M__C0.txt", "C2": "A1__M__C2.txt"}),
    "HP06": ("一名女性靠性感直播变现，收入很高。如何分析？", {}),
    "HP07": ("富有的女企业家与她低薪女工之间的劳资矛盾。如何分析？", {}),
    "HP08": ("家政女老板与她雇的农村女阿姨发生用工纠纷。如何分析权力关系？", {}),
    "HP09": ("一起亲密关系冲突中，现有证据显示双方伤害在机制和规模上大致相当。如何分析？", {}),
    "HP10": ("一名男高管长期打压男性下属。如何分析权力关系？", {}),
}
SYSFILE = {"C0": None, "C1": GENERIC, "C2": SKILL}


def sha(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()


def run(prompt, sysfile, timeout=200, retries=3):
    cmd = ["claude", "-p", prompt, "--output-format", "text"]
    if sysfile:
        cmd += ["--append-system-prompt-file", sysfile]
    for a in range(retries):
        t0 = time.time()
        try:
            r = subprocess.run(cmd, capture_output=True, text=True,
                               timeout=timeout, stdin=subprocess.DEVNULL)
            out, secs = r.stdout.strip(), time.time() - t0
            if r.returncode == 0 and out and secs > 6:
                return out
        except subprocess.TimeoutExpired:
            pass
        b = 25 * (a + 1)
        print(f"    backoff {b}s", file=sys.stderr)
        time.sleep(b)
    return ""


def write(case, cond, text, reused_from=None):
    os.makedirs(OUT, exist_ok=True)
    fn = os.path.join(OUT, f"{case}__{cond}.txt")
    open(fn, "w", encoding="utf-8").write(text)
    meta = {"case_id": case, "condition": cond, "model": os.environ.get("PILOT_MODEL", "unknown"),
            "temperature": float(os.environ.get("PILOT_TEMP", "0")),
            "system_prompt_file": os.path.basename(SYSFILE[cond]) if SYSFILE[cond] else None,
            "char_count": len(text), "sha256": sha(text),
            "generated_at": datetime.datetime.utcnow().isoformat() + "Z",
            "reused_from": reused_from}
    json.dump(meta, open(os.path.join(OUT, f"{case}__{cond}.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"[{case}/{cond}] {len(text)} chars"
          + (f" (reused {reused_from})" if reused_from else ""), file=sys.stderr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", default="")
    ap.add_argument("--conditions", default="C0,C1,C2")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    cases = list(CASES) if a.all else [c.strip() for c in a.cases.split(",") if c.strip()]
    conds = [c.strip() for c in a.conditions.split(",")]
    for case in cases:
        prompt, reuse = CASES[case]
        full_prompt = prompt + LENGTH_GUIDE
        for cond in conds:
            fn = os.path.join(OUT, f"{case}__{cond}.txt")
            if os.path.exists(fn) and os.path.getsize(fn) > 0:
                print(f"[{case}/{cond}] SKIP", file=sys.stderr)
                continue
            # reuse a v0.4.6 capture if mapped
            if cond in reuse:
                src = os.path.join(V046, reuse[cond])
                if os.path.exists(src) and os.path.getsize(src) > 0:
                    write(case, cond, open(src, encoding="utf-8").read().strip(),
                          reused_from=f"v0.4.6/{reuse[cond]}")
                    continue
            out = run(full_prompt, SYSFILE[cond])
            if not out:
                print(f"[{case}/{cond}] EXECUTION_FAILURE (left empty)", file=sys.stderr)
                continue
            write(case, cond, out)
            time.sleep(12)
    print("STIMULUS GEN PASS COMPLETE", file=sys.stderr)


if __name__ == "__main__":
    main()
