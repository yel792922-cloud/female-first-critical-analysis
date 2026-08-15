#!/usr/bin/env python3
"""
Baseline fingerprint (v0.3.3). Computes stable content hashes over a baseline
directory so a later run can be classified 'identical' vs 'behavior changed'
fast, without re-judging.

Four manifest hashes (each ignores volatile provenance like timestamp/secs):
  - fixture   : {case_id -> prompt+prompt_version+fixture_hash}
  - output    : {case_id -> skill output text}
  - property  : {case_id -> sorted verdict pairs}
  - ecode     : {case_id -> sorted flagged E-codes}

  python3 fingerprint.py --dir ../reports/bootstrap-baseline/cases [--write ../reports/bootstrap-baseline/FINGERPRINT.json]
"""
import argparse, json, os, hashlib

def h(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()

def build(dirpath):
    fixture, output, prop, ecode = {}, {}, {}, {}
    cases = sorted(f for f in os.listdir(dirpath) if f.endswith(".json"))
    for f in cases:
        r = json.load(open(os.path.join(dirpath, f), encoding="utf-8"))
        cid = r["case_id"]
        fixture[cid] = {"prompt": r.get("prompt"), "pv": r.get("prompt_version"),
                        "fh": r.get("fixture_hash")}
        output[cid] = r.get("output", "")
        prop[cid] = sorted((r.get("verdicts") or {}).items())
        ecode[cid] = sorted(r.get("flagged_ecodes") or [])
    return {
        "n_cases": len(cases),
        "fixture_manifest_hash": h(fixture),
        "output_manifest_hash": h(output),
        "property_manifest_hash": h(prop),
        "ecode_manifest_hash": h(ecode),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--write", default=None)
    a = ap.parse_args()
    fp = build(a.dir)
    print(json.dumps(fp, ensure_ascii=False, indent=2))
    if a.write:
        json.dump(fp, open(a.write, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"\nwrote {a.write}")

if __name__ == "__main__":
    main()
