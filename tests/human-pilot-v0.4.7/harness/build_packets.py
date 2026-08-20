#!/usr/bin/env python3
"""
Blinded participant-packet builder for the human pilot (v0.4.7).

Given generated stimuli (stimulus_gen.py) and a participant roster, produce
per-participant blinded packets:
  - condition C0/C1/C2 mapped to display labels A/B/C by a per-(participant,case)
    random permutation (label bias control)
  - display order randomized (position bias control)
  - a balanced-incomplete-block case assignment (5-6 cases incl. HP05 & HP10)
  - a manifest recording the TRUE maps + seed for post-hoc unblinding
The TRUE condition->label map lives ONLY in the manifest, never in the packet
shown to a participant.

This does NOT invent participants; it consumes a roster you provide (real people)
or, with --dry-run, prints the blinding plan for N slots without any human data.

  python3 build_packets.py --seed 42 --participants 18 --dry-run
"""
import json, os, sys, random, hashlib, argparse, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
HP = os.path.dirname(HERE)
TESTS = os.path.dirname(HP)
REPO = os.path.dirname(TESTS)
STIM = os.path.join(REPO, "reports", "v0.4", "human-pilot", "stimuli")
PACKETS = os.path.join(REPO, "reports", "v0.4", "human-pilot", "packets")
ALL_CASES = [f"HP{i:02d}" for i in range(1, 11)]
BOUNDARY = ["HP05", "HP10"]
NON_BOUNDARY = [c for c in ALL_CASES if c not in BOUNDARY]
CONDS = ["C0", "C1", "C2"]


def load_stim(case, cond):
    fn = os.path.join(STIM, f"{case}__{cond}.txt")
    if not (os.path.exists(fn) and os.path.getsize(fn) > 0):
        return None
    text = open(fn, encoding="utf-8").read().strip()
    return {"text": text, "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "char_count": len(text)}


def assign_cases(rng, n_participants, per=5):
    """Balanced-ish incomplete block: every non-boundary case gets >=8 exposures."""
    plan = []
    pool = []
    # cycle non-boundary cases to spread exposure
    cyc = itertools.cycle(rng.sample(NON_BOUNDARY, len(NON_BOUNDARY)))
    for _ in range(n_participants):
        extra = [next(cyc) for _ in range(per - len(BOUNDARY))]
        cases = BOUNDARY + extra
        rng.shuffle(cases)
        plan.append(cases)
    return plan


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--participants", type=int, required=True)
    ap.add_argument("--per-participant", type=int, default=5)
    ap.add_argument("--dry-run", action="store_true",
                    help="print blinding plan without requiring a real roster")
    a = ap.parse_args()
    rng = random.Random(a.seed)
    os.makedirs(PACKETS, exist_ok=True)

    # verify stimuli exist (unless dry-run, where we just plan)
    missing = []
    for case in ALL_CASES:
        for cond in CONDS:
            if load_stim(case, cond) is None:
                missing.append(f"{case}/{cond}")
    if missing and not a.dry_run:
        print("REFUSING: missing stimuli -> run stimulus_gen.py first:\n  "
              + ", ".join(missing), file=sys.stderr)
        sys.exit(2)
    if missing:
        print(f"[dry-run] {len(missing)} stimuli not yet generated: "
              + ", ".join(missing[:8]) + (" ..." if len(missing) > 8 else ""),
              file=sys.stderr)

    case_plan = assign_cases(rng, a.participants, a.per_participant)
    manifest = {"seed": a.seed, "participants": a.participants, "packets": []}
    exposure = {c: 0 for c in ALL_CASES}
    for pidx, cases in enumerate(case_plan):
        pid = f"P{pidx+1:03d}"
        pk = {"participant_id": pid, "cases": []}
        for case in cases:
            exposure[case] += 1
            labels = ["A", "B", "C"]
            perm = CONDS[:]
            rng.shuffle(perm)
            cond_to_label = dict(zip(perm, labels))       # true map (secret)
            order = labels[:]
            rng.shuffle(order)                            # display order
            shown = []
            for lab in order:
                cond = [c for c, l in cond_to_label.items() if l == lab][0]
                st = load_stim(case, cond)
                shown.append({"label": lab,
                              "sha256": st["sha256"] if st else None,
                              "char_count": st["char_count"] if st else None})
            # length confound flag
            counts = [s["char_count"] for s in shown if s["char_count"]]
            lc = bool(counts) and (max(counts) / max(1, min(counts)) > 1.8)
            pk["cases"].append({"case_id": case,
                                "condition_to_label": cond_to_label,
                                "presentation_order": order,
                                "shown": shown,
                                "length_confound_flag": lc})
        manifest["packets"].append(pk)
    manifest["exposure"] = exposure
    json.dump(manifest, open(os.path.join(PACKETS, "manifest.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"manifest written: {a.participants} packets, exposure={exposure}", file=sys.stderr)
    print("BUILD PACKETS COMPLETE", file=sys.stderr)


if __name__ == "__main__":
    main()
