#!/usr/bin/env python3
"""
Framework contribution decomposition (v0.4.5). RESUMABLE per-cell.

Three conditions on the SAME adversarial prompt:
  C0 bare-base   (no system-prompt append)
  C1 generic     (GENERIC-SCAFFOLD.md: general critical thinking, NO gender content)
  C2 full-skill  (SKILL.md)
Judge the target property, strict 4-state. Derive pattern:
  all PASS                -> PATTERN1_BASE_SUFFICIENT
  C0<PASS, C1=PASS, C2=PASS-> PATTERN2_GENERIC_SCAFFOLD
  C0<PASS, C1<PASS, C2=PASS-> PATTERN3_CANDIDATE_FEMALE_FIRST_SPECIFIC
  graded improvement       -> PATTERN4_INCREMENTAL
  any MISSING/EXEC         -> UNRESOLVED
Bootstrap judge (LOW independence) -> EXPLORATORY behavioral only.

  python3 framework_contribution.py --cases A1-P1,A5-P1,A4-P1,NC-A4
"""
import json,os,sys,time,subprocess,argparse
HERE=os.path.dirname(os.path.abspath(__file__));RP=os.path.dirname(HERE)
TESTS=os.path.dirname(RP);REPO=os.path.dirname(TESTS)
sys.path.insert(0,os.path.join(TESTS,"evaluation-v0.3","harness"))
from bootstrap_judge import judge_output,BOOTSTRAP    # noqa
SKILL=os.path.join(REPO,"SKILL.md")
GENERIC=os.path.join(RP,"variants","GENERIC-SCAFFOLD.md")
DS=os.path.join(RP,"dataset","adversarial-ablation.jsonl")
OUT=os.path.join(REPO,"reports","v0.4","framework-contribution","per-cell")
RANK={"VALIDATED_FAIL":0,"FAIL":0,"PARTIAL":1,"N/A":2,"PASS":3}

def run_skill(prompt,sysfile,timeout=170,retries=3):
    cmd=["claude","-p",prompt,"--output-format","text"]
    if sysfile: cmd+=["--append-system-prompt-file",sysfile]
    for a in range(retries):
        t0=time.time()
        try:
            r=subprocess.run(cmd,capture_output=True,text=True,timeout=timeout,stdin=subprocess.DEVNULL)
            out,secs=r.stdout.strip(),time.time()-t0
            if r.returncode==0 and out and secs>6: return out
        except subprocess.TimeoutExpired: pass
        b=25*(a+1); print(f"    backoff {b}s",file=sys.stderr); time.sleep(b)
    return ""

def classify(out,jr,prop):
    if not out or not jr["ok"]: return "EXECUTION_FAILURE"
    v=jr["verdicts"].get(prop)
    if v is None: return "MISSING"
    if v=="N-A": return "N/A"
    if v=="FAIL": return "VALIDATED_FAIL"
    return v

def pattern(c0,c1,c2):
    if any(s in ("MISSING","EXECUTION_FAILURE") for s in (c0,c1,c2)): return "UNRESOLVED"
    r0,r1,r2=RANK[c0],RANK[c1],RANK[c2]
    if c0=="PASS" and c1=="PASS" and c2=="PASS": return "PATTERN1_BASE_SUFFICIENT"
    if r0<3 and c1=="PASS" and c2=="PASS": return "PATTERN2_GENERIC_SCAFFOLD"
    if r0<3 and r1<3 and c2=="PASS": return "PATTERN3_CANDIDATE_FEMALE_FIRST_SPECIFIC"
    if r0<=r1<=r2 and r2>r0: return "PATTERN4_INCREMENTAL"
    return f"OTHER(C0={c0},C1={c1},C2={c2})"

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--cases",required=True); a=ap.parse_args()
    os.makedirs(OUT,exist_ok=True)
    rows={j["case_id"]:j for j in (json.loads(l) for l in open(DS,encoding="utf-8") if l.strip())}
    for cid in [c.strip() for c in a.cases.split(",")]:
        outp=os.path.join(OUT,cid+".json")
        if os.path.exists(outp): print(f"[{cid}] SKIP",file=sys.stderr); continue
        row=rows[cid]; prompt=row["adversarial_prompt"]; prop=row["target_property"]
        states={}
        for cond,sysf in (("C0",None),("C1",GENERIC),("C2",SKILL)):
            out=run_skill(prompt,sysf); time.sleep(12)
            jr=judge_output(prompt,out,[prop],mode=BOOTSTRAP,case_id=cid) if out else {"ok":False,"verdicts":{}}
            states[cond]=classify(out,jr,prop); time.sleep(12)
        pat=pattern(states["C0"],states["C1"],states["C2"])
        rec={"case_id":cid,"module":row["module"],"type":row["type"],"target_property":prop,
             "C0_bare":states["C0"],"C1_generic":states["C1"],"C2_fullskill":states["C2"],
             "pattern":pat,"judge_type":"BOOTSTRAP","independence":"LOW","label":"EXPLORATORY"}
        json.dump(rec,open(outp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
        print(f"[{cid}] C0={states['C0']} C1={states['C1']} C2={states['C2']} -> {pat}",file=sys.stderr)
    print("FRAMEWORK CONTRIBUTION PASS COMPLETE",file=sys.stderr)

if __name__=="__main__":
    main()
