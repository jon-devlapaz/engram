# Named info-gathering skills

Before spawning Phase 1 agents, list `~/.tink/skills/` (top level and
skillset folders). Match by **job**, not nostalgia for Claude paths.
Tell each subagent the names that actually exist. A missing row means
that helper is unavailable — still complete the ledger; still refuse
infringing books.

| Nuwa name | Job | When to call | Local rule |
|---|---|---|---|
| `gemini-video` | local video → transcript | user video, no captions | use if a video-transcript skill is installed |
| `web-article-reader` | full article, not a search snippet | important URL | use if an article-reader skill is installed; else fetch the page |
| `agent-reach` | multi-platform (X / Reddit / YouTube) | social fragments | use if a multi-platform gatherer is installed |
| `huashu-research` | structured deep research | one dimension needs depth, not spray | use if a *web-corpus* research skill is installed; do not treat a codebase-`research` skill as this |
| `pdf` | read PDF books / papers | user-supplied PDFs | use if a pdf skill is installed; else read the file with available PDF tools |

As of the Stage 5 port, none of those five Nuwa names live under
`~/.tink/skills/`. Re-scan each run; if one appears, prefer it over
raw WebSearch for that job.
