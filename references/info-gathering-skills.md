# Nested Phase-1 helpers — hard bind

These skills ship **inside Engram** under `helpers/`. One install carries
them. Phase 1 does **not** scan a host skills root. Invocation is:

1. Orchestrator sets `ENGRAM_PACK` = absolute path to this Engram pack.
2. Every Phase 1 subagent prompt includes the **Helper block** from
   `SKILL.md` (mandatory).
3. Subagents **read** `helpers/<job>/SKILL.md` then execute when a
   trigger hits — in-tree paths and per-ledger routing so it cannot be
   skipped.

## Job table

| Job | Path | Trigger | Save under engram |
|---|---|---|---|
| Full article | `helpers/web-article-reader/SKILL.md` | Important URL; need full text not a snippet | `sources/articles/` |
| Multi-platform | `helpers/agent-reach/SKILL.md` | X / Reddit / YouTube / social fragments | ledger + optional `sources/articles/` |
| Deep research | `helpers/deep-research/SKILL.md` | One ledger needs depth, not spray | `sources/articles/` + ledger |
| Local video → transcript | `helpers/gemini-video/SKILL.md` | User video, no captions; needs `GEMINI_API_KEY` | `sources/transcripts/` |
| PDF / doc → text | `helpers/pdf/SKILL.md` | User-supplied / legal PDF or doc (**I1**) | `sources/books/` or `sources/articles/` |

**YouTube with captions:** prefer Engram scripts before gemini-video:

```bash
bash "$ENGRAM_PACK/scripts/download_subtitles.sh" <YouTube_URL> <out-dir>
python3 "$ENGRAM_PACK/scripts/srt_to_transcript.py" <input.srt> <engram>/sources/transcripts/<name>.txt
```

## Per-agent routing

| Agent | Prefer |
|---|---|
| 1 Writings | pdf (user books), web-article-reader (essay URLs), deep-research if thin |
| 2 Conversations | subtitle scripts → gemini-video (local/no-caption) → agent-reach (discover) |
| 3 Expression | agent-reach, web-article-reader |
| 4 External | web-article-reader, deep-research |
| 5 Decisions | deep-research, web-article-reader |
| 6 Timeline | deep-research (esp. last 12 months), web-article-reader |

## Reliability rules

1. **No spawn without Helper block** in the agent prompt.
2. **Read helper SKILL.md** before first use in a run.
3. **Helper failure ≠ skip ledger** — fall back; label the gap.
4. **I1** — pdf/books only from user-supplied or otherwise legal access.
5. **Original language** for saved primary files (article-reader); Engram
   runtime stays English.
6. Phase 1.5: if a ledger is thin, re-run that agent **with the same
   Helper block** and the deep-research preference explicit.

## Preflight doctor

Before Phase 1 spawn (and after mid-run helper failure):

```bash
# Preferred gate (doctor + url-cache; exit 0 only when safe to spawn)
python3 "$ENGRAM_PACK/scripts/phase1_gate.py" --engram "<engram-dir>"
# optional: --mkdir-cache

# Doctor alone (scripting / wizards)
python3 "$ENGRAM_PACK/scripts/engram_doctor.py"
python3 "$ENGRAM_PACK/scripts/engram_doctor.py" --json
```

- **Gate:** `phase1_gate.py` runs doctor and requires
  `<engram>/sources/url-cache/` (create with `--mkdir-cache`). Exit 0
  only when safe to spawn Phase 1.
- Checks nested `helpers/*/SKILL.md`, pack scripts, and host CLIs.
- **Blockers:** `python3`, `yt-dlp`, missing helper/script files → exit 1.
  **Do not spawn Phase 1 while `blocker_fails > 0`.**
- **Optional warns:** ffmpeg, pdftotext, agent-reach CLI, playwright, gemini
  SDK/key, pdf Python deps, url-cache process note. Proceed only with
  labeled gaps in run notes.
- On WARN/FAIL: open `helpers/doctor/SKILL.md`, walk JSON `next_wizards`,
  re-doctor, then resume.
- Doctor **detects only** — do not install `agent-reach` (or other host
  tools) without the user. Jung Phase-1 lesson: helper SKILL present ≠
  CLI on PATH.

## Shared URL cache

1. Ensure `<engram>/sources/url-cache/` exists before spawn.
2. Before fetch: look for `sha256(url)[:16].md` (or stable slug); first
   line must be `url: <original>`.
3. Hit → reuse. Miss → fetch once, write cache, then save under
   `sources/articles/` or `sources/transcripts/` as needed.
4. Never re-fetch a cached URL from another agent in the same run.

## Spine-first

Spawn Timeline (Agent 6) — or one spine agent — **before** the other
five. Optional `references/research/00-spine.md` (≤40 lines) lists hub
URLs + cache paths. Agents 1–5 consume cache; they re-run deep-research
on a hub only if their ledger is uniquely thin after reading spine + cache.

## Helper log schema

One line per attempt in `PARITY-RUN.md`:

`|agent|helper|trigger|outcome|cache=hit|miss|n/a|notes|`

## I1 enrichment (optional)

If quote density matters, ask once for user-supplied legal primaries
before deep gather. Pure-web mind still ships without them. Never invent
book access.

Provenance: `helpers/THIRD_PARTY.md`, each `helpers/*/SOURCE.md`.
