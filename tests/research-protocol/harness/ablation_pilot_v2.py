#!/usr/bin/env python3
"""
Ablation pilot v2 (v0.4.2). Full-vs-ablated on capability-challenging cases,
with STRICT 4-state classification. RESUMABLE + paced + backoff.

States (never conflated):
  N/A               property not applicable (judge returned N-A)
  MISSING           judge returned no verdict for the target property
  EXECUTION_FAILURE model/judge/runner call failed
  VALIDATED_FAIL    property actually FAIL
  (PASS / PARTIAL)  property held / partially held

Per case: run FULL skill + ABLATED variant (the case's module), judge BOTH on
the single target property, classify each, derive an effect level:
  LEVEL3_NECESSITY   full=PASS  ablated=VALIDATED_FAIL
  LEVEL2_ROBUSTNESS  full=PASS  ablated=PARTIAL
  LEVEL1_OVERLAP     full=PASS  ablated=PASS
  UNRESOLVED         any MISSING / EXECUTION_FAILURE
For negative controls: CONTROL_OK (full==ablated) else CONTROL_OVERTRIGGER.

judge_type = BOOTSTRAP, independence = LOW -> results are EXPLORATORY only.

  python3 ablation_pilot_v2.py --cases A1-P1,A2-P1,A5-P1,A6-P2,NC-A1,NC-A6
"""
import json, os, sys, time, subprocess, argparse

HERE=os.path.dirname(os.path.abspath(__file__)); RP=os.path.dirname(HERE)
TESTS=os.path.dirname(RP); REPO=os.path.dirname(TESTS)
sys.path.insert(0, os.path.join(TESTS,"evaluation-v0.3","harness"))
from bootstrap_judge import judge_output, BOOTSTRAP           # noqa
from ablate import make_variant                               # noqa

SKILL=os.path.join(REPO,"SKILL.md")
DS=os.path.join(RP,"dataset","ablation-diagnostic.jsonl")
VAR=os.path.join(RP,"variants")
OUT=os.path.join(REPO,"reports","v0.4","ablation-v2","per-case")

def run_skill(prompt, sysfile, timeout=170, retries=3):
    cmd=["claude","-p",prompt,"--append-system-prompt-file",sysfile,"--output-format","text"]
    for a in range(retries):
        t0=time.time()
        try:
            r=subprocess.run(cmd,capture_output=True,text=True,timeout=timeout,stdin=subprocess.DEVNULL)
            out,secs=r.stdout.strip(),time.time()-t0
            if r.returncode==0 and out and secs>8: return out
        except subprocess.TimeoutExpired: pass
        back=25*(a+1); print(f"    skill backoff {back}s",file=sys.stderr); time.sleep(back)
    return ""

def classify(run_ok, judge_ok, verdicts, prop):
    if not run_ok: return "EXECUTION_FAILURE"
    if not judge_ok: return "EXECUTION_FAILURE"
    v=verdicts.get(prop)
    if v is None: return "MISSING"
    if v=="N-A": return "N/A"
    if v=="FAIL": return "VALIDATED_FAIL"
    return v  # PASS / PARTIAL

def effect(typ, full, abl):
    if typ=="negative":
        if full in ("MISSING","EXECUTION_FAILURE") or abl in ("MISSING","EXECUTION_FAILURE"):
            return "UNRESOLVED"
        return "CONTROL_OK" if full==abl else "CONTROL_OVERTRIGGER"
    if full in ("MISSING","EXECUTION_FAILURE") or abl in ("MISSING","EXECUTION_FAILURE"):
        return "UNRESOLVED"
    if full=="PASS" and abl=="VALIDATED_FAIL": return "LEVEL3_NECESSITY"
    if full=="PASS" and abl=="PARTIAL": return "LEVEL2_ROBUSTNESS"
    if full=="PASS" and abl=="PASS": return "LEVEL1_OVERLAP"
    return f"OTHER(full={full},abl={abl})"

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--cases",required=True)
    a=ap.parse_args(); os.makedirs(OUT,exist_ok=True)
    rows={j["case_id"]:j for j in (json.loads(l) for l in open(DS,encoding="utf-8") if l.strip())}
    for cid in a.cases.split(","):
        cid=cid.strip()
        outp=os.path.join(OUT,cid+".json")
        if os.path.exists(outp): print(f"[{cid}] SKIP",file=sys.stderr); continue
        row=rows.get(cid)
        if not row: print(f"[{cid}] not in dataset",file=sys.stderr); continue
        mod, prop, prompt, typ = row["module"], row["target_property"], row["prompt"], row["type"]
        variant=make_variant(mod,VAR)["path"]
        # FULL
        f_out=run_skill(prompt,SKILL); time.sleep(12)
        fj=judge_output(prompt,f_out,[prop],mode=BOOTSTRAP,case_id=cid) if f_out else {"ok":False,"verdicts":{},"flagged_ecodes":[]}
        f_state=classify(bool(f_out),fj["ok"],fj["verdicts"],prop); time.sleep(12)
        # ABLATED
        a_out=run_skill(prompt,variant); time.sleep(12)
        aj=judge_output(prompt,a_out,[prop],mode=BOOTSTRAP,case_id=cid) if a_out else {"ok":False,"verdicts":{},"flagged_ecodes":[]}
        a_state=classify(bool(a_out),aj["ok"],aj["verdicts"],prop)
        eff=effect(typ,f_state,a_state)
        rec={"case_id":cid,"module":mod,"target_property":prop,"type":typ,
             "difficulty_note":row["difficulty_note"],
             "full_state":f_state,"ablated_state":a_state,"effect_level":eff,
             "full_verdicts":fj["verdicts"],"ablated_verdicts":aj["verdicts"],
             "full_ecodes":fj.get("flagged_ecodes",[]),"ablated_ecodes":aj.get("flagged_ecodes",[]),
             "judge_type":"BOOTSTRAP","independence":"LOW","label":"EXPLORATORY",
             "ablated_output_head":(a_out[:600] if a_out else "")}
        json.dump(rec,open(outp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
        print(f"[{cid}] full={f_state} ablated={a_state} -> {eff}",file=sys.stderr)
        time.sleep(12)
    print("ABLATION PILOT V2 PASS COMPLETE",file=sys.stderr)

if __name__=="__main__":
    main()
