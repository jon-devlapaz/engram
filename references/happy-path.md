# Happy-path agentic bootstrap

Lean contract for **distill `<name>`** on Engram **2.7.9+**. The agent
owns scripts and the tree; the user consents only for (a) **host installs**
and (b) **checkpoints 1.5 / 2.5** with verbs **approve | revise | stop**.

See also `references/ax-ops.md` and `scripts/phase1_gate.py`.

## Contract

| Who | Owns |
|---|---|
| User | Says `distill <name>`; host-install consent; 1.5/2.5 approve\|revise\|stop |
| Agent | Create tree, doctor, phase1_gate, AX beats, Phase 1… spawn, labeled gaps |

Detect-only for host tools — **never** silent `brew` / `pipx` / package installs.

## Flow

1. **Create engram tree** from `references/schema.md` + `STATUS.md`
   (`phase: 0.5`) + `mkdir sources/url-cache` (and books/transcripts/articles).
2. Agent runs:
   ```bash
   python3 scripts/engram_doctor.py --engram <dir>
   python3 scripts/phase1_gate.py --engram <dir> --mkdir-cache
   ```
3. If `blocker_fails > 0`: **ONE consent** — install blockers / proceed with
   labeled gaps / stop. True blockers today: `python3`, missing helper/script
   files. Optional WARNs (ffmpeg, poppler, agent-reach, playwright, gemini,
   pdf deps, **yt-dlp**) do not block spawn.
4. Optional WARNs: default **proceed with labeled gaps** unless the user
   asked max-fidelity bootstrap. Example: yt-dlp missing → label YouTube
   caption/discover path as gap; use other helpers.
5. `python3 scripts/ax_gate.py --engram <dir>` at phase 0.5 must **not** FAIL
   on empty `sources/url-cache/` (WARN / empty-OK when phase is 0.5 or
   pre-research). Nonempty required only after Phase 1.5+ / post-gather.
6. Spawn Phase 1… Auto AX beats after 1.5 / 2.5 / 4 / G8. Human only at
   **1.5** and **2.5** (unless `waiver: run-through` recorded at 0.5).

## Consent shapes

```text
Host install — Engram needs: <tool>. OK to install / proceed labeled gaps / stop?
Checkpoint 1.5|2.5 — approve | revise | stop
```

Dismiss/skip ≠ approve. Bare "proceed" is not approve unless the phase is named.

## Gates: deterministic vs judgment

| Kind | Examples | Owner |
|---|---|---|
| Deterministic | `quality_check`, `merge_research`, `engram_doctor`, `phase1_gate`, `ax_gate`, `test_smoke` | Scripts |
| Judgment | fidelity-scorecard, Stage 8 stakes, synthesis quality | Agent |

Scripts assert structure; agents own taste. Smoke uses `examples/minimal-fixture/` only.
