#!/usr/bin/env python3
"""
Evaluation v0.3 offline harness.

Runs the DETERMINISTIC layer (Layer 1) for real. The property judge (Layer 2)
and pairwise (Layer 3) require an LLM judge behind an execution adapter and
return ADAPTER_PENDING here — see harness/adapter.md. Skill invocation is also
adapter-pending; outputs are supplied as captured fixtures.

Stdlib only (no pip installs). Usage:

  python3 run_eval.py --case F.case.json --output F.output.json --gold G.json
  python3 run_eval.py --demo            # runs every fixtures/*.case.json pair
  python3 run_eval.py --demo --markdown # emit a markdown report

Exit code is 0 even on FAIL verdicts (this is a report tool, not a gate); a
nonzero code means the harness itself errored.
"""
import argparse, json, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
EVAL_ROOT = os.path.dirname(HERE)                 # tests/evaluation-v0.3
REPO_ROOT = os.path.dirname(os.path.dirname(EVAL_ROOT))  # repo root
REFERENCES_DIR = os.path.join(REPO_ROOT, "references")
FIXTURES = os.path.join(EVAL_ROOT, "fixtures")

# Conservative shortcut pre-flag patterns -> candidate E-codes. These are
# HEURISTIC SIGNALS routed to the judge, never verdicts (see deterministic.md).
PREFLAG_PATTERNS = [
    (r"显然(就)?是(父权|男权)", "E01", "strong structural claim marker — verify evidence"),
    (r"因为(父权|男权)制?(导致|造成)", "E01", "single-cause patriarchy attribution"),
    (r"她自己选的?[，,].{0,8}(所以).{0,6}(自由|没问题)", "E03", "choice->freedom shortcut"),
    (r"(被|受)(父权|男权).{0,4}洗脑", "E04", "brainwashed / structure->no-agency"),
    (r"都是女性[，,].{0,10}(不算|谈不上)(剥削|压迫)", "E06", "shared-gender flattening"),
    (r"男(的|性)也.{0,10}所以(不(用|必)|无需)(谈|讨论)", "E08", "whataboutism topic-closer"),
    (r"受害者[，,].{0,10}(不(用|需)|无需)(承担|负).{0,4}责任", "E05", "victimhood->exemption"),
]

MODULE_ENUM = {"female-first","evidence","null-result","baseline-interrogation",
               "agency","power-structure","responsibility","intersectionality",
               "class-position","comparison","parallel-analysis"}

def load(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def length_bucket(n):
    if n < 600: return "short"
    if n > 1800: return "long"
    return "medium"

def depth_expect_bucket(depth):
    return {"concise": {"short","medium"}, "default": {"short","medium","long"},
            "deep": {"medium","long"}}.get(depth, {"short","medium","long"})

def deterministic_layer(case, output, gold):
    checks, preflags = [], []
    def chk(name, ok, detail=""):
        checks.append({"name": name, "status": "PASS" if ok else "FAIL", "detail": detail})
        return ok

    hard_ok = True
    hard_ok &= chk("case_id_match", output.get("case_id") == case.get("case_id"),
                   f'{output.get("case_id")} vs {case.get("case_id")}')
    hard_ok &= chk("answer_text_nonempty", bool(output.get("answer_text","").strip()))
    hard_ok &= chk("skill_version_set", bool(output.get("skill_version")))
    hard_ok &= chk("module_trace_present", isinstance(output.get("module_trace"), list))

    # dangling references
    dangling = []
    for r in output.get("references_cited", []) or []:
        base = os.path.basename(r)
        if not os.path.exists(os.path.join(REFERENCES_DIR, base)):
            dangling.append(r)
    hard_ok &= chk("no_dangling_references", not dangling, ("dangling: "+", ".join(dangling)) if dangling else "")

    # self-audit required only in argument-reconstruction mode
    if case.get("mode") == "argument-reconstruction":
        hard_ok &= chk("self_audit_present", bool(output.get("self_audit")), "required in argument-reconstruction mode")
    else:
        checks.append({"name": "self_audit_present", "status": "N-A", "detail": "not required in standard mode"})

    trace = set(output.get("module_trace", []) or [])
    exp = (gold or {}).get("expected_modules", {}) if gold else {}
    # necessary modules present (mechanical part of P14)
    for m in exp.get("necessary", []):
        ok = m in trace
        hard_ok &= chk(f"necessary_module:{m}", ok, "" if ok else "missing necessary module -> candidate under-activation")
    # inactive modules respected (mechanical part of P13); presence -> preflag E16
    for m in exp.get("inactive", []):
        ok = m not in trace
        chk(f"inactive_module_absent:{m}", ok, "" if ok else "irrelevant module active")
        if not ok:
            preflags.append({"e_code": "E16", "span": m, "note": "module active though gold marks it inactive"})

    # depth/length bucket (mechanical part of P15)
    n = output.get("output_length_chars", len(output.get("answer_text","")))
    lb = length_bucket(n)
    depth = output.get("requested_depth") or case.get("requested_depth") or "default"
    depth_ok = lb in depth_expect_bucket(depth)
    chk(f"depth_length_consistent({depth}->{lb})", depth_ok,
        "" if depth_ok else "length bucket inconsistent with requested depth -> candidate E15/E20")
    if not depth_ok:
        preflags.append({"e_code": "E15/E20", "span": f"{depth}->{lb}", "note": "depth/length mismatch"})

    # shortcut pre-flags (heuristic; routed to judge)
    text = output.get("answer_text","")
    for pat, ecode, note in PREFLAG_PATTERNS:
        m = re.search(pat, text)
        if m:
            preflags.append({"e_code": ecode, "span": m.group(0), "note": note + " (PRE-FLAG ONLY, not a verdict)"})

    return {"passed": hard_ok, "checks": checks, "shortcut_preflags": preflags}

def property_judge_stub(case, output, gold):
    """ADAPTER_PENDING. Applicability comes from gold; N-A is never a deficiency."""
    na = set((gold or {}).get("not_applicable", []))
    applicable = set((gold or {}).get("required_properties", [])) | set((gold or {}).get("optional_properties", []))
    props = {}
    allp = ["P0"+str(i) for i in range(1,10)] + ["P1"+str(i) for i in range(0,6)]
    for p in allp:
        if p in na:
            props[p] = {"status": "N-A"}
        elif p in applicable:
            props[p] = {"status": "ADAPTER_PENDING", "evidence": "requires wired judge model (adapter.md)"}
    return props

def evaluate(case, output, gold):
    det = deterministic_layer(case, output, gold)
    pj = property_judge_stub(case, output, gold)
    verdict = "ADAPTER_PENDING" if det["passed"] else "FAIL"
    critical = []
    # deterministic-only critical: dangling ref or a must_not_fail necessary module missing structurally
    return {
        "case_id": case.get("case_id"),
        "skill_version": output.get("skill_version"),
        "layers": {"deterministic": det, "property_judge": pj,
                   "pairwise": {"result": "ADAPTER_PENDING"}},
        "critical_failures": critical,
        "verdict": verdict,
    }

def render_md(ev):
    d = ev["layers"]["deterministic"]
    lines = [f"### {ev['case_id']}  ({ev['skill_version']})",
             f"- deterministic layer: **{'PASS' if d['passed'] else 'FAIL'}**"]
    for c in d["checks"]:
        mark = {"PASS": "PASS", "FAIL": "FAIL", "N-A": "N-A"}.get(c["status"], "?")
        lines.append(f"  - [{mark}] {c['name']} {('— '+c['detail']) if c['detail'] else ''}")
    if d["shortcut_preflags"]:
        lines.append("- shortcut pre-flags (routed to Layer 2, NOT verdicts):")
        for pf in d["shortcut_preflags"]:
            lines.append(f"  - `{pf['e_code']}` «{pf['span']}» — {pf['note']}")
    pend = [p for p,v in ev["layers"]["property_judge"].items() if v["status"]=="ADAPTER_PENDING"]
    na = [p for p,v in ev["layers"]["property_judge"].items() if v["status"]=="N-A"]
    lines.append(f"- property judge: {len(pend)} ADAPTER_PENDING, {len(na)} N-A → {sorted(na) if na else 'none'}")
    lines.append(f"- pairwise: ADAPTER_PENDING")
    lines.append(f"- **verdict: {ev['verdict']}**\n")
    return "\n".join(lines)

def run_pair(case_p, out_p, gold_p, md):
    case, output = load(case_p), load(out_p)
    gold = load(gold_p) if gold_p and os.path.exists(gold_p) else None
    ev = evaluate(case, output, gold)
    print(render_md(ev) if md else json.dumps(ev, ensure_ascii=False, indent=2))

def demo(md):
    cases = sorted(glob.glob(os.path.join(FIXTURES, "*.case.json")))
    if not cases:
        print("no fixtures found", file=sys.stderr); return
    for cp in cases:
        cid = os.path.basename(cp).replace(".case.json","")
        gold = os.path.join(EVAL_ROOT, "calibration", "gold", cid.split("__")[0] + ".json")
        for op in sorted(glob.glob(os.path.join(FIXTURES, cid + ".*.output.json"))):
            if md: print(f"\n<!-- {os.path.basename(op)} -->")
            run_pair(cp, op, gold, md)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case"); ap.add_argument("--output"); ap.add_argument("--gold")
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--markdown", action="store_true")
    a = ap.parse_args()
    if a.demo:
        demo(a.markdown)
    elif a.case and a.output:
        run_pair(a.case, a.output, a.gold, a.markdown)
    else:
        ap.print_help(); sys.exit(2)

if __name__ == "__main__":
    main()
