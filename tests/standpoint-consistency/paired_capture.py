#!/usr/bin/env python3
"""
Paired standpoint capture (v0.4.6). RESUMABLE + paced + backoff.

Captures OUTPUTS (not judge verdicts) for qualitative structured comparison of
standpoint / cross-case consistency. The bootstrap judge is too unreliable on the
subtle standpoint metrics (systematic MISSING on P04/P06/P07), so this round does
a transparent analyst comparison of the raw outputs. All BOOTSTRAP / LOW
INDEPENDENCE (same-family). Conditions: C0 bare, C2 full skill.

  python3 paired_capture.py --pairs A1,A5,B5 --conditions C0,C2 --genders F,M
  python3 paired_capture.py --pairs NC1,NC2 --conditions C2 --genders F,M
"""
import json,os,sys,time,subprocess,argparse
HERE=os.path.dirname(os.path.abspath(__file__))
REPO=os.path.dirname(os.path.dirname(HERE))
SKILL=os.path.join(REPO,"SKILL.md")
DS=os.path.join(HERE,"pairs.jsonl")
OUT=os.path.join(REPO,"reports","v0.4","standpoint","captures")

def run(prompt,cond,timeout=170,retries=3):
    cmd=["claude","-p",prompt,"--output-format","text"]
    if cond=="C2": cmd+=["--append-system-prompt-file",SKILL]
    for a in range(retries):
        t0=time.time()
        try:
            r=subprocess.run(cmd,capture_output=True,text=True,timeout=timeout,stdin=subprocess.DEVNULL)
            out,secs=r.stdout.strip(),time.time()-t0
            if r.returncode==0 and out and secs>6: return out
        except subprocess.TimeoutExpired: pass
        b=25*(a+1); print(f"    backoff {b}s",file=sys.stderr); time.sleep(b)
    return ""

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--pairs",required=True)
    ap.add_argument("--conditions",default="C0,C2")
    ap.add_argument("--genders",default="F,M")
    a=ap.parse_args(); os.makedirs(OUT,exist_ok=True)
    rows={j["pair_id"]:j for j in (json.loads(l) for l in open(DS,encoding="utf-8") if l.strip())}
    conds=a.conditions.split(","); genders=a.genders.split(",")
    for pid in [p.strip() for p in a.pairs.split(",")]:
        row=rows[pid]
        variants=[]
        if row["kind"]=="pair":
            if "F" in genders: variants.append(("F",row["female_prompt"]))
            if "M" in genders: variants.append(("M",row["male_prompt"]))
        else:
            variants.append(("S",row["prompt"]))
        for g,prompt in variants:
            for cond in conds:
                fn=os.path.join(OUT,f"{pid}__{g}__{cond}.txt")
                if os.path.exists(fn) and os.path.getsize(fn)>0:
                    print(f"[{pid}/{g}/{cond}] SKIP",file=sys.stderr); continue
                out=run(prompt,cond)
                open(fn,"w",encoding="utf-8").write(out)
                print(f"[{pid}/{g}/{cond}] {len(out)} chars",file=sys.stderr); time.sleep(12)
    print("PAIRED CAPTURE PASS COMPLETE",file=sys.stderr)

if __name__=="__main__":
    main()
