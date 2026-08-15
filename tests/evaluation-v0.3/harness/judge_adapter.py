#!/usr/bin/env python3
"""
Layer-2/3 judge adapter (v0.3.1).

Provides the judge interface plus two MOCK judges used to exercise the
calibration RUNNER (not a real judge's performance):

  - MockJudge("ideal")   : returns the analyst-in-the-loop reference verdicts
                           (encodes the rubric applied correctly). Running the
                           calibrator against it tests the RUNNER PLUMBING and
                           shows the target the rubric is meant to hit.
  - MockJudge("flawed")  : deliberately misses E13 and shows feminist-alignment
                           bias, to prove the calibrator CATCHES a bad judge.

  - ActingModelJudge     : the real semantic judge. In this environment there is
                           no reproducible, version-pinned programmatic endpoint
                           to call it deterministically, so it raises
                           AdapterPending. NOT faked.

Stdlib only. Verdict tables live in ../fixtures/calibration/mock-verdicts-*.json
"""
import json, os, time

HERE = os.path.dirname(os.path.abspath(__file__))
EVAL_ROOT = os.path.dirname(HERE)
CAL_FIX = os.path.join(EVAL_ROOT, "fixtures", "calibration")


class AdapterPending(Exception):
    """Raised when no reproducible judge endpoint is wired."""


class JudgeResult:
    def __init__(self, item_id, flagged_ecodes=None, prop_verdicts=None,
                 answer_scores=None, na_props=None, extra=None):
        self.item_id = item_id
        self.flagged_ecodes = set(flagged_ecodes or [])
        self.prop_verdicts = prop_verdicts or {}     # {P02: "PASS"|"PARTIAL"|"FAIL"|"N-A"}
        self.answer_scores = answer_scores or {}     # {"A": 2.0, "B": 0.7, "C": 1.8}
        self.na_props = set(na_props or [])
        self.extra = extra or {}                     # raw row (B_flagged, C_keyprop, ...)


class MockJudge:
    """Replays a canned verdict table. Deterministic + repeatable by design."""
    def __init__(self, variant="ideal"):
        self.variant = variant
        path = os.path.join(CAL_FIX, f"mock-verdicts-{variant}.json")
        with open(path, "r", encoding="utf-8") as f:
            self.table = json.load(f)
        self.config = {
            "judge": f"mock-{variant}",
            "prompt_version": "property-judge.md@v0.3.1",
            "temperature": 0.0,
            "deterministic": True,
            "timestamp": None,          # set per run for provenance
            "reproducible": True,
        }

    def judge(self, item_id):
        row = self.table.get(item_id)
        if row is None:
            raise KeyError(f"no mock verdict for {item_id}")
        return JudgeResult(item_id,
                           flagged_ecodes=row.get("flagged_ecodes"),
                           prop_verdicts=row.get("prop_verdicts"),
                           answer_scores=row.get("answer_scores"),
                           na_props=row.get("na_props"),
                           extra=row)

    def run_provenance(self):
        c = dict(self.config); c["timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        return c


class ActingModelJudge:
    """
    Real semantic judge. No reproducible programmatic endpoint is available in
    this environment (cannot pin a model + prompt + temperature and re-run
    identically), so this is intentionally NOT executable. Do not fake it.
    """
    def __init__(self):
        self.config = {"judge": "acting-model", "reproducible": False}

    def judge(self, item_id, *_):
        raise AdapterPending(
            "ActingModelJudge has no reproducible programmatic endpoint here; "
            "wire a pinned judge model per harness/adapter.md before use.")


def get_judge(name):
    if name in ("ideal", "flawed"):
        return MockJudge(name)
    if name == "acting-model":
        return ActingModelJudge()
    raise ValueError(f"unknown judge '{name}'")
