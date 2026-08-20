# Blind Randomization & Provenance (v0.4.7)

Goal: participants cannot infer which answer is the female-first Skill, the
control, or the "intended winner." Three biases are controlled: **label bias**,
**position bias**, **familiarity bias**.

## 1. Condition ↔ label decoupling

For each (participant × case), the three conditions **C0/C1/C2** are mapped to
display labels **A/B/C** by an independent uniform random permutation. The true
map is stored server-side in `condition_label_map` (survey-schema) and is
**never shown** to the participant or to the blind annotators.

- Across the pilot, each condition appears under each of A/B/C roughly equally
  (the builder balances the permutation multiset per case).
- The mapping is re-randomized **per case**, so a participant cannot learn "B is
  always the long one."

## 2. Position / order counterbalancing

- The **display order** of the labelled answers is randomized per case
  (`presentation_order`), independently of the condition→label map.
- Across participants, first/second/third positions are balanced per condition.

## 3. Case assignment (balanced incomplete block)

- Each participant sees **5–6 cases**, always including boundary cases **HP05**
  and **HP10**.
- The remaining cases are drawn by a balanced-incomplete-block scheme so each of
  HP01–HP04, HP06–HP09 is seen by **≥ 8 participants**.
- Case *order* within a session is randomized per participant.

## 4. Anti-familiarity measures

- No condition is ever labelled with a system name, version, or gender term.
- Formatting is normalized (same heading style, same markdown, same bullet
  conventions) so a participant cannot spot C2 by house style rather than
  content. Normalization touches presentation only, never analytical content.
- The neutral warm-up uses a non-gender topic so participants are not primed
  toward gender as the salient dimension.

## 5. Length parity

The packet builder computes each answer's character count. If, for a case, the
max/min length ratio across shown conditions exceeds a preset threshold, the case
is flagged `LENGTH_CONFOUND` for that packet and excluded from the
length-sensitive items (helpfulness, readability) in analysis. Content is never
trimmed to force parity.

## 6. Provenance ledger (per stimulus)

Every generated stimulus records: `case_id`, `condition`, `model`,
`temperature`, `system_prompt_file` (none / GENERIC-SCAFFOLD.md / SKILL.md),
`char_count`, `sha256`, `generated_at`, and the runner git commit. Reused
v0.4.6 captures carry their original provenance plus a `reused_from` pointer.
The builder refuses to assemble a packet if any stimulus hash is missing.

## 7. Reproducible seed

`build_packets.py` takes `--seed`; the seed, the resulting per-participant
condition→label maps, orders, and case assignments are written to
`packets/manifest.json` so the exact blinding is auditable after unblinding.

## 8. Unblinding

The condition→label map is revealed **only** at analysis time, after all
participant responses and all blind annotations are locked. Annotators code
against locked, still-blinded records.
