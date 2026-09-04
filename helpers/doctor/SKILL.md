---
name: engram-doctor
description: >
  Troubleshooting wizard for Engram preflight and mid-run helper failures.
  Run when engram_doctor.py reports WARN/FAIL, or when a Phase 1 helper
  (yt-dlp, agent-reach, gemini-video, pdf, playwright, poppler) breaks
  mid-distill. Step 0 always re-runs the doctor.
---

# Engram doctor — troubleshooting wizards

Use this skill when `scripts/engram_doctor.py` reports **WARN** or **FAIL**,
or when a helper fails mid-run (missing CLI, import error, empty captions,
API key unset).

**Do not install agent-reach (or other host tools) without the user.** The
doctor only *detects*; wizards tell the user what to install.

## Step 0 — Always re-run the doctor

```bash
python3 "$ENGRAM_PACK/scripts/engram_doctor.py"
python3 "$ENGRAM_PACK/scripts/engram_doctor.py" --json
```

- Exit **0** = no blocker fails (warns OK).
- Exit **1** = blocker fail(s) — fix before spawning Phase 1 agents that need them.
- Exit **2** = doctor crashed — report stderr; do not invent a green light.
- JSON field `next_wizards` is the ordered, deduped wizard list to walk.

Then open the matching wizard below.

## Mid-run failure protocol

1. **Log** the failure in the engram run notes / helper usage log (helper,
   trigger, error, timestamp). Do not silent-degrade.
2. **Pause** if the failure is a blocker for that agent's primary path
   (e.g. no `yt-dlp` for YouTube captions). Thin ledgers are allowed only
   when labeled; missing tools are not an excuse to skip the ledger.
3. **Wizard** — run Step 0, then the wizard from `next_wizards` (or the
   one that matches the error).
4. **Re-doctor** — confirm the check flipped to pass (or an accepted warn).
5. **Resume** the agent with the same Helper block.

## Wizards

### reinstall-pack

**When:** any `helper-*/SKILL.md` or required `scripts/*` check is **fail**.

**Do:**
1. Confirm `ENGRAM_PACK` points at this tree (folder that contains
   `SKILL.md`, `helpers/`, `scripts/`).
2. Re-clone or restore the Engram pack from the known git remote; do not
   hand-invent missing helper folders.
3. Re-run the doctor.

### install-python

**When:** `cli-python3` fail (blocker).

**Do:** Install Python 3 and ensure `python3` is on PATH (`brew install
python`, pyenv, or the OS package). Re-doctor.

### install-ytdlp

**When:** `cli-yt-dlp` fail (blocker).

**Do:**
```bash
brew install yt-dlp
# or: pipx install yt-dlp
which yt-dlp
```
Never spawn caption/discover agents that assume yt-dlp without this check.
Re-doctor.

### install-ffmpeg

**When:** `cli-ffmpeg` warn.

**Do:** `brew install ffmpeg` (or OS equivalent). Optional for many runs;
required for some media convert paths. Re-doctor.

### install-poppler

**When:** `cli-pdftotext` warn.

**Do:** `brew install poppler` so `pdftotext` is on PATH. Re-doctor.

### install-agent-reach

**When:** `cli-agent-reach` warn.

**Why it matters:** Carl Jung Phase-1 hard-bind postmortem — agents opened
`helpers/agent-reach/SKILL.md` but the `agent-reach` CLI / mcporter backends
were absent on PATH; multi-platform discover degraded to zero-config Jina
and yt-dlp search only.

**Upstream:** https://github.com/Panniantong/Agent-Reach

**Do (with user approval only):**
1. Show the user the doctor warn and the Jung lesson (CLI absent ≠ skill absent).
2. Let the user install from upstream (follow that repo's README — typically
   pipx/uv of the package that provides the `agent-reach` CLI).
3. `agent-reach doctor --json` (upstream health) then Engram doctor again.
4. Engram doctor **detects only** — never install agent-reach silently.

### install-playwright

**When:** `playwright` warn.

**Do:**
```bash
pip install playwright
playwright install chromium
```
Needed for WeChat / some web-article-reader fallbacks. Re-doctor.

### install-gemini-video

**When:** `gemini` warn (SDK and/or API key).

**Do:**
```bash
pip install -r "$ENGRAM_PACK/helpers/gemini-video/requirements.txt"
# Ensure GEMINI_API_KEY or GOOGLE_API_KEY is set in the environment.
```
**Never paste API keys into ledgers, run notes, commits, or chat logs.**
Point the user at env / secret store only. Re-doctor (doctor reports whether
a key env is set — not the value).

### install-pdf-deps

**When:** `pdf-python-deps` warn, or pdf helper import errors mid-run.

**Do:**
```bash
pip install -r "$ENGRAM_PACK/helpers/pdf/requirements.txt"
# Optional system: brew install poppler pandoc
```
I1 still binds: user-supplied / legal files only. Re-doctor.

### enable-url-cache

**When:** `url-cache-process` warn (info severity — always offered as process hygiene).

**Do:** Prefer **fetch-once** into the engram's `sources/url-cache/`:
1. Create `sources/url-cache/` under the engram folder if missing.
2. Before re-fetching a URL, check for an existing cache file keyed by URL
   or slug.
3. On first fetch (Jina, article-reader, WebFetch), save the raw/markdown
   body under `sources/url-cache/` and reference that path from the ledger.
4. Mid-run: if a URL was already cached, reuse it — do not hammer the origin.

This is a process wizard, not a host package install.

## Anti-patterns (do not)

- **Spawn with missing yt-dlp** after a blocker fail — fix or halt that path.
- **Silent degrade** — always log helper failure; label ledger gaps.
- **Paste API keys** into ledgers, SKILL drafts, commits, or scorecards.
- **Pirate tools / pirate book sites** — Engram I1; refuse.
- **Install agent-reach (or any host tool) without the user** — detect + advise only.
- **Skip re-doctor** after a wizard — prove the check flipped.

## Related

- Preflight script: `scripts/engram_doctor.py`
- Helper index: `helpers/README.md`
- Phase-1 bind: `references/info-gathering-skills.md`
