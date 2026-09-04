# Recommended info-gathering skills

These helpers **raise Phase 1 corpus quality**. Treat them as part of a
max-quality Engram setup: the user should have an installed skill (or
equivalent agent capability) for each **job** below.

Match by **job**, not brand name. The names in the first column are
common labels — if the host uses different skill names that do the same
job, use those.

## Before Phase 1

1. List `<skills-root>/` (top level and skillset folders).
2. Map installed skills to the jobs in the table.
3. **If a job has no matching skill and no equivalent built-in tool**,
   tell the user once which recommended helpers are missing and that
   installing them improves the distill. Prefer they install before a
   deep / standard run; a fast run may proceed with weaker coverage.
4. Tell each Phase 1 subagent which helpers (by real installed name) to
   call for its ledger.
5. Never skip a ledger because a helper is missing. Never use helpers
   to acquire books outside user-supplied / otherwise legal access (I1).

## Jobs

| Canonical name (example) | Job | When to call | Max-quality rule |
|---|---|---|---|
| `gemini-video` | local video → transcript | user video, no captions | **Recommended.** Install a video→transcript skill if the corpus includes local video. |
| `web-article-reader` | full article, not a search snippet | important URL | **Recommended.** Install an article-reader skill; bare search snippets are not enough for ledger weight. |
| `agent-reach` | multi-platform (X / Reddit / YouTube) | social fragments | **Recommended** when social / talk corpus matters. |
| `deep-research` | structured deep research | one dimension needs depth, not spray | **Recommended** for standard/deep tiers. Do not treat a codebase-research skill as this. |
| `pdf` | read PDF books / papers | user-supplied PDFs | **Recommended.** Install a PDF skill or confirm the agent can extract text from PDFs. |

## Principle

Maximize Engram’s ability to build the engram: prefer a complete helper
set over silent degradation. Fallbacks (fetch page, read PDF with
available tools, Engram caption scripts) exist so a run can finish —
they are not the quality target.
