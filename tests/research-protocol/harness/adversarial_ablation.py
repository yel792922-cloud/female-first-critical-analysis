#!/usr/bin/env python3
"""
Adversarial (failure-induction) ablation runner (v0.4.3). RESUMABLE per-cell.

Instead of removing a module and hoping behavior changes, we PUSH the exact
failure the module prevents (adversarial_prompt) and compare FULL vs ABLATED.
Strong contribution evidence = FULL+ADVERSARIAL PASS while ABLATED+ADVERSARIAL
VALIDATED_FAIL.

Conditions: full_adv (SKILL.md + adversarial prompt), ablated_adv (variant +
adversarial prompt). Each cell: run skill + judge target property, strict
4-state classify. Per-cell immutable files; skip completed.

judge_type=BOOTSTRAP, independence=LOW -> EXPLORATORY only. MISSING never ->N/A;
EXECUTION_FAILURE excluded from failure-rate denominator but reported.

  python3 adversarial_ablation.py --cases A1-P1,A2-P1,... --conditions full_adv,ablated_adv
"""
import json,os,sys,time,subprocess,argparse
HERE=os.path.dirname(os.path.abspath(__file__));RP=os.path.dirname(HERE)
TESTS=os.path.dirname(RP);REPO=os.path.dirname(TESTS)
sys.path.insert(0,os.path.join(TESTS,"evaluation-v0.3","harness"))
from bootstrap_judge import judge_output,BOOTSTRAP    # noqa
from ablate import make_variant                       # noqa
SKILL=os.path.join(REPO,"SKILL.md")
DS=os.path.join(RP,"dataset","adversarial-ablation.jsonl")
VAR=os.path.join(RP,"variants")
OUT=os.path.join(REPO,"reports","v0.4","adversarial-ablation","per-cell")

def run_skill(prompt,sysfile,timeout=170,retries=3):
    cmd=["claude","-p",prompt,"--append-system-prompt-file",sysfile,"--output-format","text"]
    for a in range(retries):
        t0=time.time()
        try:
            r=subprocess.run(cmd,capture_output=True,text=True,timeout=timeout,stdin=subprocess.DEVNULL)
            out,secs=r.stdout.strip(),time.time()-t0
            if r.returncode==0 and out and secs>8: return out
        except subprocess.TimeoutExpired: pass
        b=25*(a+1); print(f"    backoff {b}s",file=sys.stderr); time.sleep(b)
    return ""

def classify(run_ok,judge_ok,verdicts,prop):
    if not run_ok or not judge_ok: return "EXECUTION_FAILURE"
    v=verdicts.get(prop)
    if v is None: return "MISSING"
    if v=="N-A": return "N/A"
    if v=="FAIL": return "VALIDATED_FAIL"
    return v

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--cases",required=True)
    ap.add_argument("--conditions",default="full_adv,ablated_adv")
    a=ap.parse_args(); os.makedirs(OUT,exist_ok=True)
    rows={j["case_id"]:j for j in (json.loads(l) for l in open(DS,encoding="utf-8") if l.strip())}
    conds=a.conditions.split(",")
    for cid in [c.strip() for c in a.cases.split(",")]:
        row=rows.get(cid)
        if not row: print(f"[{cid}] not found",file=sys.stderr); continue
        mod,prop,prompt=row["module"],row["target_property"],row["adversarial_prompt"]
        for cond in conds:
            cell=f"{cid}__{cond}"; outp=os.path.join(OUT,cell+".json")
            if os.path.exists(outp): print(f"[{cell}] SKIP",file=sys.stderr); continue
            sysfile = SKILL if cond.startswith("full") else make_variant(mod,VAR)["path"]
            out=run_skill(prompt,sysfile); time.sleep(12)
            jr=judge_output(prompt,out,[prop],mode=BOOTSTRAP,case_id=cid) if out else {"ok":False,"verdicts":{},"flagged_ecodes":[]}
            st=classify(bool(out),jr["ok"],jr["verdicts"],prop)
            rec={"case_id":cid,"module":mod,"condition":cond,"target_property":prop,
                 "type":row["type"],"state":st,"verdicts":jr["verdicts"],
                 "flagged_ecodes":jr.get("flagged_ecodes",[]),
                 "judge_type":"BOOTSTRAP","independence":"LOW","label":"EXPLORATORY",
                 "output_head":(out[:500] if out else "")}
            json.dump(rec,open(outp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
            print(f"[{cell}] {st}",file=sys.stderr); time.sleep(12)
    print("ADVERSARIAL ABLATION PASS COMPLETE",file=sys.stderr)

if __name__=="__main__":
    main()
