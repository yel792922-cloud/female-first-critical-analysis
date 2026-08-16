#!/usr/bin/env python3
"""
OOD / boundary sweep runner (v0.4.1). RESUMABLE + paced + backoff.

Runs the CURRENT skill (SKILL.md) on OOD / boundary cases, judges the mapped
properties, and records a deterministic over-genderization scan. Per-case
immutable files; skip completed; retry failed. judge_type = BOOTSTRAP.

  python3 ood_sweep.py --dataset generalization --limit 8
  python3 ood_sweep.py --dataset boundary
"""
import json, os, re, sys, time, subprocess, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
RP = os.path.dirname(HERE)
TESTS = os.path.dirname(RP)
REPO = os.path.dirname(TESTS)
sys.path.insert(0, os.path.join(TESTS, "evaluation-v0.3", "harness"))
from bootstrap_judge import judge_output, BOOTSTRAP   # noqa

SKILL = os.path.join(REPO, "SKILL.md")
PROP_MAP = {"evidence":"P01","null-result":"P02","agency":"P04","power":"P05",
            "structure":"P05","double-standard":"P05","responsibility":"P06",
            "intersectionality":"P07","class-position":"P07","comparison":"P08",
            "false-equivalence":"P08","causal":"P10","epistemic-fairness":"P11"}
GENDER_TERMS = r"性别|女性|男性|父权|男权|gender|女权|厌女|凝视"
GENDERED_CASE = r"性|女|男|gender|父权"   # marks a case that IS about gender

def run_skill(prompt, timeout=170, retries=3):
    cmd = ["claude","-p",prompt,"--append-system-prompt-file",SKILL,"--output-format","text"]
    for attempt in range(retries):
        t0=time.time()
        try:
            r=subprocess.run(cmd,capture_output=True,text=True,timeout=timeout,stdin=subprocess.DEVNULL)
            out,secs=r.stdout.strip(),time.time()-t0
            if r.returncode==0 and out and secs>8: return out
        except subprocess.TimeoutExpired: pass
        back=25*(attempt+1); print(f"    skill fast-fail backoff {back}s",file=sys.stderr); time.sleep(back)
    return ""

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--dataset",required=True,choices=["generalization","boundary"])
    ap.add_argument("--limit",type=int,default=999)
    a=ap.parse_args()
    ds=os.path.join(RP,"dataset",a.dataset+".jsonl")
    rows=[json.loads(l) for l in open(ds,encoding="utf-8") if l.strip()]
    outdir=os.path.join(REPO,"reports","v0.4","ood",a.dataset)
    os.makedirs(outdir,exist_ok=True)
    done=set(f[:-5] for f in os.listdir(outdir) if f.endswith(".json"))
    ran=0
    for row in rows:
        cid=row["case_id"]
        if cid in done: print(f"[{cid}] SKIP",file=sys.stderr); continue
        if ran>=a.limit: break
        prompt=row["prompt"]
        props=sorted(set(PROP_MAP[p] for p in row.get("expected_properties",[]) if p in PROP_MAP)) or ["P02","P05","P06","P10"]
        out=run_skill(prompt)
        if not out:
            print(f"[{cid}] skill failed -> retry next pass",file=sys.stderr); time.sleep(20); continue
        time.sleep(12)
        jr=judge_output(prompt,out,props,mode=BOOTSTRAP,case_id=cid)
        if not jr["ok"]:
            print(f"[{cid}] judge failed -> retry next pass",file=sys.stderr); time.sleep(20); continue
        case_is_gender=bool(re.search(GENDERED_CASE,prompt))
        g_terms=len(re.findall(GENDER_TERMS,out))
        overgender = (not case_is_gender) and g_terms>=3
        rec={"case_id":cid,"dataset":a.dataset,"category":row.get("category") or row.get("condition"),
             "prompt":prompt,"expected_properties":row.get("expected_properties"),
             "judged_props":props,"verdicts":jr["verdicts"],"flagged_ecodes":jr["flagged_ecodes"],
             "judge_type":"BOOTSTRAP","independence":"LOW",
             "case_is_gender":case_is_gender,"gender_term_count":g_terms,
             "over_genderization_flag":overgender,
             "output":out,"provenance":jr["provenance"]}
        json.dump(rec,open(os.path.join(outdir,cid+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
        print(f"[{cid}] verdicts={jr['verdicts']} overgender={overgender} gterms={g_terms}",file=sys.stderr)
        ran+=1; time.sleep(12)
    print(f"{a.dataset.upper()} SWEEP PASS COMPLETE",file=sys.stderr)

if __name__=="__main__":
    main()
