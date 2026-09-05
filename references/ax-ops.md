# AX ops — Status, beats, checkpoints, machine-down

Lean operator contract for Engram hill-climb **3.0.0+**. Process friction
fixes — not fidelity. See also `scripts/ax_gate.py` and
`references/happy-path.md`.

## STATUS.md (single truth)

Top-of-engram file. **Overwrite in place** each milestone (do not append
a history of Status blocks here — history lives in `PARITY-RUN.md`).

Minimum schema (keys or headings; case-insensitive):

```markdown
# STATUS — <Subject>

- phase: <e.g. G8 complete | Phase 1.5 awaiting approve | …>
- fidelity: <score/grade or n/a>
- stakes: <G8 PASS | pending | n/a>
- gate: <pack version that last gated, e.g. 3.0.0>
- I1: <public-legal | local-first | …>
- updated: <YYYY-MM-DD America/Chicago>
```

Optional: one-line `next:` and `blockers:`. Point `PARITY-RUN.md` at
`STATUS.md` with a short pointer at the top; do not delete run history.

## Auto AX beat (after 1.5 / 2.5 / 4 / G8)

After each of those milestones, append **exactly 5 lines** to
`PARITY-RUN.md` and surface the same block to the user in chat:

```text
AX beat — <milestone> — <YYYY-MM-DD>
phase: <from STATUS>
fidelity: <from STATUS or n/a>
decision: approve | revise | stop | (auto after gate)
note: <≤1 line friction or next>
```

Do not skip the beat because the user said "proceed" casually — still
emit it once the phase actually advanced.

## Checkpoint verbs (1.5 and 2.5)

Widget / options must be **exactly**:

- `approve` — advance to the next phase
- `revise` — stay; name the thin ledger or synthesis patch
- `stop` — halt the distill

Hard rules:

- Dismiss / skip / ignore **≠** approve.
- Do **not** treat bare "proceed" / "continue" / "go ahead" as approve
  unless the user names the phase ("approve Phase 1.5", "approve 2.5").
- `waiver: run-through` (recorded at 0.5) is the only pre-authorization
  to skip the pause.

## Machine-down card

When the **host machine/session is not connected** (Shell unavailable /
session tooling down):

```text
Machine-down — Engram needs your host machine/session connected.
1. Reconnect the host machine / session, then confirm Shell works again.
2. Message the user in chat with this card if Shell is unavailable.
3. Re-run the last gate (phase1_gate / ax_gate / quality_check).
4. Resume from STATUS.md phase — do not re-spawn Phase 1 blindly.
```

First fix: reconnect host session. Then resume from Status. See SKILL
failure table row **Machine-down**.

## sources/INDEX.md + CAPTCHA stubs

- Keep `sources/INDEX.md` classifying files as **primary** / **secondary**
  / **stub** (and optional biblio).
- CAPTCHA / Robot Challenge / Cloudflare interstitial fetches must **not**
  live under `sources/articles/`. Move to `sources/stubs/` or delete.
- Prefer fetch-once into `sources/url-cache/` (`sha256(url)[:16].md`).
- At phase 0.5 an empty `url-cache/` dir is OK (ax_gate WARN). Nonempty
  is required after Phase 1.5+ / post-gather.

## Gate commands

```bash
python3 scripts/engram_doctor.py --engram <dir>   # url-cache PASS when nonempty
python3 scripts/phase1_gate.py --engram <dir>
python3 scripts/ax_gate.py                        # pack checks A–E
python3 scripts/ax_gate.py --engram <dir>         # + engram F–J
python3 scripts/merge_research.py --engram <dir>
python3 scripts/quality_check.py --engram <dir>
```
