#!/usr/bin/env python3
"""
Bootstrap judge (v0.3.2). Wraps the `claude -p` path as a BOOTSTRAP regression
judge with a HARD mode guard.

Two execution modes exist in this pipeline:
  - BOOTSTRAP: judge = claude -p, independence = LOW (same vendor/family as the
    skill author). ALLOWED for behavior/adapter/schema/prompt/version-comparison
    regression. FORBIDDEN for calibration gates, precision/recall claims, or
    pilot-readiness claims.
  - INDEPENDENT_CALIBRATION: requires an independent, version-pinned,
    reproducible judge. If unavailable -> BLOCKED (never falls back to bootstrap).

This module ONLY implements BOOTSTRAP. Requesting INDEPENDENT_CALIBRATION raises
IndependentJudgeUnavailable (there is no independent endpoint in this env).
"""
import subprocess, time, json, re, hashlib, os

BOOTSTRAP = "BOOTSTRAP"
INDEPENDENT_CALIBRATION = "INDEPENDENT_CALIBRATION"

CRITICAL_PROPS = ["P02", "P04", "P06", "P11", "P12"]
CRITICAL_ECODES = ["E01", "E05", "E11", "E12", "E13", "E14", "E17"]

JUDGE_SYSTEM = (
    "You are a BOOTSTRAP reasoning-property judge for a female-first critical-"
    "analysis skill. Score ONLY the listed properties for the ANSWER about the "
    "CASE. Score REASONING QUALITY, not political alignment: feminist framing "
    "earns no bonus, non-feminist framing no penalty; same evidence/inference "
    "bar for every stance. E-codes to consider when present: E01 forced-"
    "oppression (structural/patriarchy conclusion past the evidence), E05 "
    "victimhood->exemption, E11 strawman (rebuilding a view as one it disclaims), "
    "E12 model substitution, E13 aggregate->individual causal leap, E17 political-"
    "alignment->epistemic-privilege. Output ONLY a compact JSON object, no prose, "
    'no fences: {"verdicts":{"P02":"PASS|PARTIAL|FAIL|N-A"},"flagged_ecodes":[],'
    '"evidence":{"P02":"short reason"}}'
)


class IndependentJudgeUnavailable(Exception):
    pass


def _hash(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]


def _extract_json(text):
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        return None


def _git_commit():
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, timeout=10).stdout.strip() or "UNKNOWN"
    except Exception:
        return "UNKNOWN"


def judge_output(case_text, answer_text, properties, mode=BOOTSTRAP,
                 model=None, skill_version="UNKNOWN", case_id="UNKNOWN", timeout=120):
    if mode == INDEPENDENT_CALIBRATION:
        raise IndependentJudgeUnavailable(
            "No independent, version-pinned judge endpoint in this environment. "
            "Bootstrap must NOT fall back to satisfy INDEPENDENT_CALIBRATION.")
    if mode != BOOTSTRAP:
        raise ValueError(f"unknown mode {mode}")

    prompt = (f"CASE:\n{case_text}\n\nANSWER:\n{answer_text}\n\n"
              f"PROPERTIES TO SCORE: {', '.join(properties)}\nReturn ONLY the JSON object.")
    cmd = ["claude", "-p", prompt, "--output-format", "text",
           "--append-system-prompt", JUDGE_SYSTEM]
    if model:
        cmd += ["--model", model]
    t0 = time.time()
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        ok = r.returncode == 0
        parsed = _extract_json(r.stdout) if ok else None
    except subprocess.TimeoutExpired:
        ok, parsed, r = False, None, None

    prov = {
        "mode": BOOTSTRAP,
        "judge_type": "BOOTSTRAP",
        "adapter": "claude-cli-print",
        "independence_level": "LOW (same vendor/family; alias model)",
        "judge_model_alias": model or "DEFAULT",
        "model_version": "UNKNOWN (alias, not pinned)",
        "prompt_version": "bootstrap_judge.py@v0.3.2",
        "runtime": "UNKNOWN",
        "temperature": "UNKNOWN (not exposed by CLI)",
        "reproducible": False,
        "mock": False,
        "skill_version": skill_version,
        "git_commit": _git_commit(),
        "case_id": case_id,
        "fixture_hash": _hash(case_text + "||" + answer_text),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "secs": round(time.time() - t0, 1),
    }
    return {
        "ok": ok,
        "parsed": parsed,
        "verdicts": (parsed or {}).get("verdicts", {}),
        "flagged_ecodes": (parsed or {}).get("flagged_ecodes", []),
        "critical_flags": [e for e in (parsed or {}).get("flagged_ecodes", []) if e in CRITICAL_ECODES],
        "provenance": prov,
    }
