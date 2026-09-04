---
name: web-article-reader
description: >
  Fetch a web article by URL into clean Markdown and save it locally.
  Use when the user (or Engram Phase 1) needs the full article, not a
  search snippet. Routes X/Twitter, WeChat, and generic pages. Prefer
  Jina Reader; fall back to Playwright scripts in this folder.
---

# Web article reader

## Workflow

When asked to read a URL (or Engram needs a full page for a ledger):

### Step 1: Choose save directory

- **Engram Phase 1:** save under `<engram-dir>/sources/articles/`
- **Standalone:** ask once for a save directory and reuse it
- Do **not** hardcode another user's Obsidian path

### Step 2: Route by URL

| URL match | Strategy |
|---|---|
| `x.com/*` or `twitter.com/*` | Run `scripts/scrape_tweet.py` |
| `mp.weixin.qq.com/*` | Run `scripts/fetch_wechat.py` |
| Everything else | Jina Reader first; Playwright fallback |

#### X / Twitter

1. Primary: fxtwitter API (no auth, fast) via `scripts/scrape_tweet.py`
2. Fallback: Playwright if the API fails

```bash
python3 <skill_path>/scripts/scrape_tweet.py <URL>
```

#### WeChat

Playwright mobile profile via:

```bash
python3 <skill_path>/scripts/fetch_wechat.py <URL>
```

#### Generic pages

1. **Prefer Jina Reader:** fetch `https://r.jina.ai/<URL>` and extract full
   article markdown (headings, body, structure)
2. **Fallback Playwright:** if Jina fails or returns thin content, use the
   Playwright path (same tooling as the WeChat script where applicable)

### Step 3: Language policy

- **Default (Engram):** keep the article in its **original language**.
  Engram ledgers may be English summaries later; do not force-translate
  the saved primary file.
- **Standalone optional:** only translate if the user explicitly asks.
- Preserve Markdown structure either way.

### Step 4: Save

- Write Markdown to the chosen directory
- Filename: sanitized article title + `.md`
- Include title, author (if known), source URL, and fetch date in frontmatter
  or a short header block

### Step 5: Report

Show: title, author (if any), save path, ~500-character preview, and whether
any optional translation was requested.

## Notes

- `<skill_path>` is this helper folder (the directory containing this `SKILL.md`)
- Playwright: `pip install playwright && playwright install chromium` when needed
- Jina Reader needs no install when called via URL prefix / WebFetch
- If every method fails, say so and ask the user to paste the content
