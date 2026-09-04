---
name: deep-research
description: >
  Structured web research with incremental saves so findings survive
  session truncation. Use when researching, looking something up,
  gathering sources, or needing depth on one topic — not for writing
  drafts. Upstream name: huashu-research.
---

> Upstream: `huashu-research`. Engram job folder: `deep-research`.
> When called from Engram Phase 1, write into the active engram directory
> (e.g. `sources/articles/` or a research note under that engram), not a
> random global `_knowledge_base/` unless the user asks otherwise.

# Deep research

Structured web research. Core goal: persist findings to disk in real time
so work is not lost when the session truncates.

## When to use

- Pre-writing research for an article or distill ledger
- Learning a new product, technology, or release
- Competitor or industry scan
- Any task that needs multiple web searches

## Procedure

### Step 1: Create the research file first

- Create the file **before** the first search
- Default path (standalone): `_knowledge_base/research-<topic>-<YYYYMMDD>.md`
- Engram Phase 1 path: `<engram-dir>/sources/articles/research-<topic>-<YYYYMMDD>.md`
  (or the ledger the caller named)
- Seed with: goal, key questions, expected output

```markdown
# [Topic] research notes

Date: YYYY-MM-DD
Goal: [one sentence]

## Key questions
1. [Q1]
2. [Q2]
3. [Q3]

## Findings

(fill incrementally)

## Sources

(append after every search)
```

### Step 2: Search and save incrementally

- After every WebSearch (or equivalent), append findings immediately
- Each finding includes source URL and date
- Prefer primary / official sources over secondary paraphrase

### Step 3: Stage summaries

- Every 3 searches, write a stage summary into the file
- Format: `### Stage summary (round N)` + current key findings

### Step 4: Final briefing

At the end, structure the file as a briefing:

```markdown
## Research conclusions

### Key facts
1. [Fact 1] (source: URL)
2. [Fact 2] (source: URL)

### Source table
| Source | URL | Published | Credibility |
|--------|-----|-----------|-------------|
| ... | ... | ... | high/med/low |

### Open questions
- [What still needs verification]

### Next steps for the caller
- [How Engram / writing should use this]
```

## Principles

- **File before search** — first result must already have a place to land
- **Incremental save** — never wait until the end
- **Research ≠ writing** — this skill gathers; it does not draft the article/skill
- **Label credibility** — primary (official) vs secondary (media/community)
- **Skip weak sources** — marketing fluff; unverifiable quote farms

## Outputs

- Research notes: path above
- Optional long-term keep: only if the user asks

**Upstream last update noted:** 2026-02-06
