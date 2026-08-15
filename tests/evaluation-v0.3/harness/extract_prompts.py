#!/usr/bin/env python3
"""
Extract one prompt per benchmark case_id from the case markdown files into a
machine manifest for bootstrap baseline runs. Best-effort: pulls the [Case] or
[Prompt] bullet; falls back to the heading title.
"""
import json, os, re, glob

HERE = os.path.dirname(os.path.abspath(__file__))
EVAL = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(EVAL))
RWB = os.path.join(REPO, "tests", "real-world-benchmark")
ES = os.path.join(REPO, "tests", "epistemic-system-stress")

INV = json.load(open(os.path.join(EVAL, "fixtures", "regression", "inventory.json"), encoding="utf-8"))

FILES = glob.glob(os.path.join(RWB, "cases-*.md")) + [os.path.join(ES, "cases.md")]

def parse_file(path):
    """Return {case_id: {title, prompt}} from a case markdown file."""
    out = {}
    text = open(path, encoding="utf-8").read()
    # headings: ## or ### <ID> · title   (ID like RWB-16, DF-01, AC-A, MS-01, ES-01)
    blocks = re.split(r"^#{2,3}\s+", text, flags=re.MULTILINE)
    for b in blocks:
        m = re.match(r"([A-Z]{2,3}-[0-9A-Za-z]+)\s*[·:]?\s*(.*)", b)
        if not m:
            continue
        cid, title = m.group(1), m.group(2).splitlines()[0].strip()
        # find [Case] or [Prompt] bullet, join wrapped lines until next '- **['
        cm = re.search(r"\*\*\[(?:Case|Prompt)\]\*\*\s*(.+?)(?=\n-\s+\*\*\[|\Z)", b, re.DOTALL)
        prompt = None
        if cm:
            prompt = re.sub(r"\s*\n\s*", "", cm.group(1)).strip().strip('"“”')
        out[cid] = {"title": title, "prompt": prompt}
    return out

def main():
    parsed = {}
    for f in FILES:
        parsed.update(parse_file(f))
    items = []
    missing = []
    for fam, meta in INV["families"].items():
        for cid in meta["case_ids"]:
            rec = parsed.get(cid)
            if rec and rec.get("prompt"):
                prompt = rec["prompt"]
            elif rec:
                prompt = f"请就以下性别议题案例做分析：{rec['title']}"
                missing.append(cid + "(title-fallback)")
            else:
                prompt = None
                missing.append(cid + "(NOT FOUND)")
            items.append({"case_id": cid, "family": fam, "prompt": prompt})
    manifest = {"items": items, "count": len(items),
                "missing_or_fallback": missing}
    out = os.path.join(EVAL, "fixtures", "regression", "full-manifest.json")
    json.dump(manifest, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"wrote {out}: {len(items)} items; {len(missing)} fallback/missing")
    for m in missing:
        print("  -", m)

if __name__ == "__main__":
    main()
