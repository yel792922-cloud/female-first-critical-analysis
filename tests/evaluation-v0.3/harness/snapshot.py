#!/usr/bin/env python3
"""
Snapshot runner (v0.3.2, BOOTSTRAP mode).

Judges every (case_id, case, answer, properties) item in a manifest with the
bootstrap judge and writes a snapshot JSON carrying full provenance. A snapshot
represents ONE skill version's behavior, judged by the bootstrap (non-
independent) judge -- usable for regression, NOT for calibration.

  python3 snapshot.py --manifest M.json --label baseline --out S.json [--model X]
"""
import argparse, json, sys
from bootstrap_judge import judge_output, BOOTSTRAP

def run(manifest_path, label, model, skill_version):
    manifest = json.load(open(manifest_path, encoding="utf-8"))
    items = []
    for it in manifest["items"]:
        res = judge_output(it["case"], it["answer"], it["properties"],
                           mode=BOOTSTRAP, model=model,
                           skill_version=skill_version, case_id=it["case_id"])
        items.append({"case_id": it["case_id"], **{k: res[k] for k in
                     ("ok", "verdicts", "flagged_ecodes", "critical_flags", "provenance")}})
        print(f"[{it['case_id']}] ok={res['ok']} verdicts={res['verdicts']} "
              f"ecodes={res['flagged_ecodes']}", file=sys.stderr)
    return {"label": label, "manifest": manifest_path, "judge_type": "BOOTSTRAP",
            "skill_version": skill_version, "items": items}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default=None)
    ap.add_argument("--skill-version", default="current")
    a = ap.parse_args()
    snap = run(a.manifest, a.label, a.model, a.skill_version)
    json.dump(snap, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"wrote {a.out}", file=sys.stderr)

if __name__ == "__main__":
    main()
