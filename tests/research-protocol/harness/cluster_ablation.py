#!/usr/bin/env python3
"""
Cluster / interaction ablation (v0.4.4). RESUMABLE per-cell.

Research question: what module COMBINATIONS are sufficient to maintain
resistance to a target failure mode? Compares FULL vs SINGLE-ablation vs
CLUSTER-ablation under the adversarial prompt. Pattern of interest:
FULL=PASS, SINGLE=PASS, CLUSTER=VALIDATED_FAIL  -> interaction / joint-dependence
candidate (NOT "redundant"). Strict 4-state; MISSING->UNRESOLVED, excluded from
denominators. Bootstrap judge (LOW independence) -> Level A behavioral only.

Clusters (experimental hypotheses, NOT architectural truth):
  A = A1 Null Result + A2 Baseline + A5 Comparison
  B = A3 Responsibility + A6 Parallel + AF Agency framework
  C = A4 Intersectionality + A7 Class/Position

  python3 cluster_ablation.py
"""
import json,os,sys,time,subprocess
HERE=os.path.dirname(os.path.abspath(__file__));RP=os.path.dirname(HERE)
TESTS=os.path.dirname(RP);REPO=os.path.dirname(TESTS)
sys.path.insert(0,os.path.join(TESTS,"evaluation-v0.3","harness"))
from bootstrap_judge import judge_output,BOOTSTRAP     # noqa
from ablate import make_variant, make_multi_variant    # noqa
SKILL=os.path.join(REPO,"SKILL.md")
DS=os.path.join(RP,"dataset","adversarial-ablation.jsonl")
VAR=os.path.join(RP,"variants")
OUT=os.path.join(REPO,"reports","v0.4","cluster-ablation","per-cell")

# cluster -> (target adversarial case, target property, primary single module, cluster module set)
PLAN=[
 ("clusterA","A1-P1","P02","A1",["A1","A2","A5"],"NC-A1"),
 ("clusterB","A6-P1","P04","A6",["A3","A6","AF"],"NC-A6"),
 ("clusterC","A7-P1","P07","A7",["A4","A7"],"NC-A7"),
]

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

def cell(cid,prompt,prop,cond,sysfile,cluster):
    outp=os.path.join(OUT,f"{cid}__{cond}.json")
    if os.path.exists(outp): print(f"[{cid}/{cond}] SKIP",file=sys.stderr); return
    out=run_skill(prompt,sysfile); time.sleep(12)
    jr=judge_output(prompt,out,[prop],mode=BOOTSTRAP,case_id=cid) if out else {"ok":False,"verdicts":{},"flagged_ecodes":[]}
    st=classify(bool(out),jr["ok"],jr["verdicts"],prop)
    rec={"case_id":cid,"condition":cond,"cluster":cluster,"target_property":prop,
         "state":st,"verdicts":jr["verdicts"],"flagged_ecodes":jr.get("flagged_ecodes",[]),
         "judge_type":"BOOTSTRAP","independence":"LOW","label":"EXPLORATORY",
         "conclusion_layer":"Level A behavioral only","output_head":(out[:500] if out else "")}
    json.dump(rec,open(outp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    print(f"[{cid}/{cond}] {st}",file=sys.stderr); time.sleep(12)

def main():
    os.makedirs(OUT,exist_ok=True)
    rows={j["case_id"]:j for j in (json.loads(l) for l in open(DS,encoding="utf-8") if l.strip())}
    for cl,cid,prop,primary,mods,ctrl in PLAN:
        prompt=rows[cid]["adversarial_prompt"]
        cell(cid,prompt,prop,"full",SKILL,cl)
        cell(cid,prompt,prop,f"single-{primary}",make_variant(primary,VAR)["path"],cl)
        cell(cid,prompt,prop,"cluster",make_multi_variant(mods,VAR)["path"],cl)
        # negative control: full vs cluster
        cprompt=rows[ctrl]["adversarial_prompt"]; cprop=rows[ctrl]["target_property"]
        cell(ctrl,cprompt,cprop,"full",SKILL,cl)
        cell(ctrl,cprompt,cprop,"cluster",make_multi_variant(mods,VAR)["path"],cl)
    print("CLUSTER ABLATION PASS COMPLETE",file=sys.stderr)

if __name__=="__main__":
    main()
