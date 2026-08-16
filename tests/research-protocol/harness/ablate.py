#!/usr/bin/env python3
"""
Ablation variant generator (v0.4). Produces a copy of SKILL.md with exactly ONE
top-level (## ) module section removed, for single-variable ablation studies.

DOES NOT modify the real SKILL.md — variants are written to an output dir and
fed to the skill runner via --append-system-prompt-file. One module removed per
variant; nothing else changed.

  python3 ablate.py --module A1 --out /tmp/ablations
  python3 ablate.py --list
  python3 ablate.py --all --out /tmp/ablations     # generate every A1..A7
"""
import argparse, os, re

# ablation id -> the ## heading prefix to remove (matched at line start)
MODULES = {
    "A1": "## Null Result Principle",
    "A2": "## Baseline Interrogation",
    "A3": "## Responsibility Principle",
    "A4": "## Intersectionality Invocation",
    "A5": "## Comparison discipline",
    "A6": "## Parallel Analysis",
    "A7": "## Class / Position Power Principle",
}

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
SKILL = os.path.join(REPO, "SKILL.md")

def remove_section(text, heading_prefix):
    lines = text.splitlines(keepends=True)
    out, i, removed, n_removed = [], 0, False, 0
    while i < len(lines):
        if not removed and lines[i].startswith(heading_prefix):
            # skip until the next '## ' heading (or EOF)
            i += 1
            while i < len(lines) and not lines[i].startswith("## "):
                i += 1
            removed = True
            n_removed += 1
            continue
        out.append(lines[i]); i += 1
    return "".join(out), n_removed

def make_variant(module_id, outdir):
    heading = MODULES[module_id]
    text = open(SKILL, encoding="utf-8").read()
    variant, n = remove_section(text, heading)
    if n != 1:
        raise SystemExit(f"expected to remove exactly 1 section for {module_id}, removed {n}")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, f"SKILL.ablate-{module_id}.md")
    # provenance banner (comment; does not change reasoning content of remaining modules)
    banner = (f"<!-- ABLATION VARIANT {module_id}: removed section '{heading}'. "
              f"single-variable; all other modules unchanged. NOT the canonical SKILL.md. -->\n")
    open(path, "w", encoding="utf-8").write(banner + variant)
    orig_len = len(text); new_len = len(variant)
    return {"module": module_id, "removed_heading": heading, "path": path,
            "orig_chars": orig_len, "variant_chars": new_len,
            "removed_chars": orig_len - new_len}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--module"); ap.add_argument("--out", default="/tmp/ablations")
    ap.add_argument("--all", action="store_true"); ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.list:
        for k, v in MODULES.items(): print(f"{k}: {v}")
        return
    ids = list(MODULES) if a.all else [a.module]
    for mid in ids:
        info = make_variant(mid, a.out)
        print(info)

if __name__ == "__main__":
    main()
