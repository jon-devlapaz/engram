# Nested Phase-1 helpers

These skills ship **inside Engram** under `helpers/`. One install carries them.
Open the helper’s `SKILL.md` when the job applies — do not depend on a host
skills-root scan.

| Job | Path | Notes |
|---|---|---|
| local video → transcript | `helpers/gemini-video/SKILL.md` | Needs `GEMINI_API_KEY`. YouTube captions still use Engram `scripts/download_subtitles.sh` when available. |
| full article → markdown | `helpers/web-article-reader/SKILL.md` | Prefer over search snippets for important URLs. |
| multi-platform gather | `helpers/agent-reach/SKILL.md` | May need upstream `agent-reach` CLI for full backends — see helper `SOURCE.md`. |
| structured deep research | `helpers/deep-research/SKILL.md` | Upstream name `huashu-research`. Persist findings into the engram dir, not a random `_knowledge_base/`. |
| PDF / doc → text | `helpers/pdf/SKILL.md` | Upstream `huashu-md-html` (MIT). **User-supplied / legal files only (I1).** |

## Before Phase 1

1. Confirm `helpers/*/SKILL.md` exist (they should, in this pack).
2. Tell each Phase 1 subagent which helper paths to use for its ledger.
3. Never skip a ledger if a helper fails — fall back to fetch / caption scripts / available PDF tools, and note the gap.
4. I1 still binds: no unauthorized book acquisition.

Provenance and licenses: `helpers/THIRD_PARTY.md` and each `helpers/*/SOURCE.md`.
