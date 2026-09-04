---
name: pdf
description: "Convert PDF/DOCX/EPUB/PPTX/XLSX/images/audio/URL to clean Markdown; also md→publication-grade HTML, DOCX, PDF (A4/A5/large-32mo), and EPUB3. Four curated templates; HTML and PDF support designer mode (AI reads content and recommends three differentiated visual directions). Implements md-as-source, multi-format consume. SKIP: tasks that need newly generated images, or compression/screenshot-only work."
---

> Engram Phase 1: use this helper for **user-supplied / legal files only (I1)**. When called from Engram, write outputs under `<engram-dir>/sources/books/` or `sources/articles/` as appropriate.
> Engram job alias: `pdf` (upstream: huashu-md-html — PDF/DOCX/EPUB/web → Markdown, plus md→html/docx/pdf/epub pipelines).

# pdf (huashu-md-html)

## Who you are

**You are not a format converter. You are the person who turns a manuscript into a publication.**

The same markdown can become a page that merely “works,” or something someone would want to keep.
The difference is not the tool—anyone can invoke pandoc—**it is whether you treat yourself as a conversion script,
or as a publishing house.**

The standard: the output should not feel “exported”; it should feel **made**.
You can reach that bar—current models can draw on the typographic tradition and taste of any publisher or book designer.
**The limit is usually not capability; it is whether you first decide to meet that standard.**

### You are not one person—you are a publishing team

| Role | What they own | If missing |
|---|---|---|
| **Editor** | Content structure, hierarchy, how titles should split | H1/H2 chaos; readers lose the path |
| **Book designer** | Layout, type, whitespace, that one 120% detail | “Readable” but nobody wants to keep it |
| **Typesetter** | Pagination, line breaks, orphans/widows, text–figure fit | A single orphan line; titles stranded at page bottom |
| **Production** | Trim size, margins, binding allowance, bleed | Printed PDF with the inner edge eaten by the binding |

Different media put different roles in charge—for the web the book designer leads;
for print PDF the typesetter and production lead. Decide who leads before you start.

### How long you may think

**As long as you need.** For layout, trying two directions before committing costs far less than finishing first and revising later.

---

> You no longer need to hand-edit every deliverable. Markdown is the source; html / docx / pdf / epub are products. This skill stitches the best path for each target into one pipeline.

## Six capabilities (decision tree)

| What the user says | Which capability | Which tool |
|------|------|------|
| “Convert this PDF/DOCX/PPTX/XLSX/EPUB/image/audio to md” / “import document” | **Cap 1: anything→md** | `scripts/any_to_md.py` (wraps markitdown) |
| “Turn this md into a web page / excellent html / publishable html” / “md to html” | **Cap 2: md→polished html** | `scripts/md_to_html.py` (wraps pandoc + 4 templates) |
| “Convert this local html back to md” / “blog URL to md” / “extract article body” | **Cap 3: html→md** | `scripts/html_to_md.py` (wraps html-to-markdown + trafilatura) |
| “Make publisher-ready Word from these md files” / “manuscript for editor/publisher” / “submission docx” / “print-book final” | **Cap 4: md→polished docx** | `scripts/md_to_docx.py` (wraps python-docx + professional layout) |
| “Print md to pdf” / “article to pdf” / “A4 pdf” / “single-chapter preview PDF” / “print-book shape” | **Cap 5: md→polished PDF** | `scripts/md_to_pdf.py` (pandoc + 4 templates + Playwright) |
| “Make an epub from md” / “ebook” / “Apple Books” / “Kindle” / “single-chapter ebook preview” | **Cap 6: md→polished EPUB** | `scripts/md_to_epub.py` (pandoc + ebooklib) |
| “Product page / tech-doc URL to md” / “bring metadata too” | **Cap 1: anything→md** (also accepts URLs) | `scripts/any_to_md.py` |

**Decision principles**:
- Cap-1 markdown can feed Cap 2/5/6 end-to-end (e.g. “PDF→md→polished reading html” or “PDF→md→re-typeset PDF”)
- Cap 3 is for reverse archival (e.g. “save a published html blog post back into project source”)
- **Cap 4 is the publishing endpoint**—when a human editor/publisher reviews, use docx; do not hand them html or md. Professional publishing defaults to docx
- **Cap 5/6 are stateless single-md conversions**—project-scale Orange Book pipelines (multi-fragment + versioning + R2 upload + WeChat Reading listing) belong to the huashu-book-pdf skill; do not try to recreate that full release pipeline here

### Further URL routing (findings from 2026-05 testing)

For URL input **both paths run**, but output quality differs sharply. Microsoft Learn certificate page (measured): Cap 1 (markitdown) 192 lines with full YAML frontmatter, certificate full name, all structured field values, heading hierarchy, links preserved; Cap 3 (trafilatura+html-to-markdown) 87 lines, lost certificate name/field values/heading hierarchy/links—flat body only.

| Page type | Use | Why |
|---------|--------|------|
| **Structured pages**: product detail, tech docs, API docs, certificate/course pages, e-commerce product pages | **Cap 1** (markitdown) | Keeps metadata, field values, links, heading hierarchy—“information-complete” |
| **Long-form pages**: blogs, news, essays, WeChat Official Account articles, column essays | **Cap 3** (trafilatura) | Auto-strips nav/sidebar/related/ads—“pure reading” |
| **Unsure** | **Run both and compare** | Pick whichever suits your downstream use |

Quick heuristic:

> **Is the URL content meant to be “read,” or “looked up”?**
> Read → Cap 3 (denoise)
> Look up → Cap 1 (preserve information)

## Core aesthetic floor (inherited from huashu-design)

Every html this skill produces must meet Huashu’s aesthetic floor. **Violate any row and redo—do not deliver.**

| Category | Must | Forbidden |
|------|------|------|
| Color | Restrained publisher palette (terracotta orange / Tufte ivory / ink blue / quiet gray) | Purple gradients, cyber neon, deep navy base (#0D1117), rainbow |
| Type | CJK serif (Source Han Serif / PingFang SC) + Latin serif/Inter; code in JetBrains Mono | Comic Sans, Roboto/Arial as large display, ultra-light weights that look frail |
| Icons | Real images (Wikimedia/Met/Unsplash/AI content images) | Emoji as formal icons, hand-drawn SVG people |
| Containers | Honest separation (hairlines, whitespace, type hierarchy) | Rounded cards + left-border accent cliché, stacked shadows |
| Ornament | One 120% signature detail (margin notes / serif italic pull-quote / handmade type detail) | Even force everywhere: emoji + tag + status dots |
| Rhythm | Breathing room between paragraphs, line-height 1.75–1.85 (CJK), max-width 680–820px | Edge-to-edge dense layout, line-height under 1.4, width >900px (eye fatigue) |

Full rules: `references/anti-ai-slop.md`.

## Ask before you start—do not guess while doing

On “convert / beautify / import” tasks, **do not jump straight to execution**.
Not because you need permission—because rework costs far more than one clarifying question. Ask first:

1. **Which capability?** Pick via the decision tree
2. **Source / destination?** File path / URL / string? Where should output go?
3. **Cap-2 only:** which template? (article default / report / reading / interactive)
4. **Special needs?** (images: keep relative paths or base64 embed? language: Chinese / English edition?)

Only start after answers are clear. Do not default-guess; wrong guesses cost the user more than one extra question.

## Cap 1: anything → md (`scripts/any_to_md.py`)

Wraps [microsoft/markitdown](https://github.com/microsoft/markitdown) v0.1.5+; one Python script covers 20+ formats.

### Invocation

```bash
# Basic: auto-detect by extension
python scripts/any_to_md.py input.pdf
python scripts/any_to_md.py input.docx -o output.md
python scripts/any_to_md.py "https://www.youtube.com/watch?v=xxx"

# Structured web / product / tech docs (keep metadata + heading hierarchy + links)
python scripts/any_to_md.py "https://learn.microsoft.com/en-us/credentials/certifications/modern-desktop/" -o cert.md

# LLM image description (needs OPENAI_API_KEY env var)
python scripts/any_to_md.py photo.jpg --llm-describe
```

### Supported formats

PDF, DOCX, PPTX, XLSX, XLS, HTML, CSV, JSON, XML, images (EXIF / optional LLM describe), audio (optional transcription), YouTube URL (auto captions), **ordinary web URLs** (with YAML frontmatter), EPUB, ZIP (recursive unpack), Outlook mail (.msg).

### Known pitfalls (also surfaced in script output)

- Scanned PDFs get no OCR; attach an LLM client or Azure Document Intelligence
- Complex tables (merged cells / nesting) lose semantics
- PPTX keeps text + notes only; animation and layout are dropped
- Output is **designed for LLM consumption**; human reading still needs a layout pass

Deps: `pip install 'markitdown[all]'` (auto-detected; install hint if missing).

Full cookbook: `references/markitdown-cookbook.md`.

## Cap 2: md → polished html (`scripts/md_to_html.py`)

Wraps [Pandoc](https://pandoc.org/) + 4 curated templates covering Huashu writing scenarios.

### Invocation

```bash
# Default: article template (Tufte-ish; essays/blogs)
python scripts/md_to_html.py article.md

# Pick a theme
python scripts/md_to_html.py report.md --theme report      # wide, table-dense; tech reports/whitepapers
python scripts/md_to_html.py article.md --theme reading    # Medium-minimal; WeChat Official Account handoff
python scripts/md_to_html.py book.md --theme interactive   # collapsible TOC + SVG; longform / Orange Book

# Output path
python scripts/md_to_html.py input.md -o out.html

# Image handling
python scripts/md_to_html.py input.md --inline-images      # base64 embed (self-contained single file)
python scripts/md_to_html.py input.md --copy-images        # copy into output dir (default keeps relative paths)
```

### Four templates at a glance

| Template | Philosophy | Best for |
|------|---------|---------|
| **article** | Tufte CSS–inspired; Pentagram-style information architecture | essays, blogs, deep reading, standalone articles |
| **report** | Publisher whitepaper; table-dense | tech reports, research, whitepapers, product docs |
| **reading** | Medium-minimal; single narrow column, large type | Official Account handoff, pure reading, light distribution |
| **interactive** | Long-doc navigation; collapse + TOC + sidebar | Orange Book chapters, technical books, long tutorials |

Each template is a **self-contained single CSS**; open the HTML and it works—no external CDN.

### Dependencies

- `brew install pandoc` (required binary)
- Script checks `which pandoc` on start and prints the install command if missing

Full cookbook: `references/md-to-html-themes.md`.

### Two modes · fallback vs visual designer

Cap 2 has two paths—

| Mode | Token cost | When |
|------|------|------|
| **Fallback** (4 theme skins) | No | Known theme, need speed, details secondary—`md_to_html.py --theme xxx` one command |
| **Designer mode** (AI custom) | Yes | AI reads the content, proposes 3 design directions, custom visual expression |

Fallback runs the pandoc binary, ~5s, no network/tokens—this is the **default**.
Designer mode is an **optional upgrade**: when the user says “make an excellent html for this md,” “show me a few styles,” or “do it in Anthropic style,” run the 4-step workflow (read → recommend → decide → implement).

Full method + style pool + review checklist: `references/visual-designer-mode.md`.
**Reference implementation**: `examples/readme.html`—a live sample from designer mode · direction C (Anthropic warm tech).

## Cap 3: html → md (`scripts/html_to_md.py`)

Wraps [html-to-markdown](https://github.com/Goldziher/html-to-markdown) (Rust core, 150–280 MB/s) + [trafilatura](https://github.com/adbar/trafilatura) (body extraction for URLs).

**Best for**: blogs, news, essays, Official Account long posts—any page where **the body is the product and everything else is noise**. Cap 3 drops nav/sidebar/related/ads and keeps the body.

**Not for**: product pages, tech docs, API docs, e-commerce—**structured pages**. Cap 3 drops field values/links/hierarchy. Use Cap 1 (markitdown) instead.

### Invocation

```bash
# Local HTML (html-to-markdown directly)
python scripts/html_to_md.py input.html

# Blog/news URL (trafilatura body extract; strips nav/ads/sidebar)
python scripts/html_to_md.py "https://example.com/article"

# URL but you want raw HTML, no body extract
python scripts/html_to_md.py "https://example.com/data" --no-extract

# Fine control
python scripts/html_to_md.py input.html --bullets="-" --heading-style=atx --strip="script,style,nav,footer"

# Output
python scripts/html_to_md.py input.html -o output.md
```

### Engine selection

| Input | Default engine | When to switch |
|---------|---------|---------|
| Local / already-clean HTML | `html-to-markdown` | Fast; auto-sanitizes |
| Blog/news URL | `trafilatura` extract → `html-to-markdown` convert | Auto-started; removes noise |
| Structured URL (product/docs/cert pages) | **Use Cap 1 (markitdown) instead** | trafilatura drops field values; markitdown keeps metadata and hierarchy |
| Fine control (heading/bullet style) | `markdownify` (opt-in, `--engine=markdownify`) | When the user explicitly asks |

Deps: `pip install html-to-markdown trafilatura markdownify`.

Full cookbook: `references/html-to-md-cookbook.md`.

## Cap 4: md → polished docx (`scripts/md_to_docx.py`)

Wraps [python-docx](https://github.com/python-openxml/python-docx) + publisher-grade layout presets, aimed at “human editor / publisher review / submission / print-book final.”

**Why Cap 4 instead of Cap 2 → docx**: pandoc’s built-in `md → docx` looks stiff (default Calibri, unstyled tables, flat quotes, no chapter-opener design). Professional print layout has its own language—small chapter label + large chapter title + English subtitle + orange rule, quote blocks colored by type, table header fill, code blocks with left color bar + light gray ground, header book title + footer page numbers. Cap 4 bakes those presets in; **one file or a whole book from one command**.

### Invocation

```bash
# Single md → docx (default: look for images beside the md)
python3 scripts/md_to_docx.py article.md
python3 scripts/md_to_docx.py article.md -o article.docx
python3 scripts/md_to_docx.py article.md --images-dir ./images

# Merge multiple md (plain mode; no cover/TOC)
python3 scripts/md_to_docx.py ch01.md ch02.md ch03.md -o combined.docx

# Full book mode (cover + TOC + headers/footers + chapter page breaks)
python3 scripts/md_to_docx.py ch*.md postscript.md appendix.md --book \
    --title "Illustrated Agent Skills" \
    --subtitle "Teach AI to remember how you work" \
    --author "Huashu" \
    --extra-info "2026 · Orange Book series" \
    --chapter-labels "Chapter 1,Chapter 2,Chapter 3,...,Afterword,Appendix" \
    --images-dir ./images \
    -o book.docx

# Page size
python3 scripts/md_to_docx.py article.md --page-size a4   # A4 report
python3 scripts/md_to_docx.py book.md --page-size book    # large 32mo (default; print-book trim)
```

### Built-in layout presets

| Element | Preset |
|------|------|
| Page size | Large 32mo (176×240 mm) or A4 |
| CJK font | Source Han Serif CN (fallback Songti SC / PingFang SC) |
| Latin font | Georgia (serif) |
| Code font | JetBrains Mono (fallback Menlo) |
| Chapter title (H1) | 24pt bold black + orange bottom rule + small chapter label above |
| Section title (H2) | 17pt bold black |
| Subsection (H3) | 13.5pt bold orange |
| Line spacing | 1.6 (comfortable for CJK) |
| Quotes | Auto color by emoji: 💡 amber / ✅ teal / ⚠️ rose / plain warm orange |
| Code blocks | Light gray ground (F5F5F0) + 16pt orange left bar |
| Tables | Header fill + light gray borders + center align |
| Figures | Centered + gray italic caption + max width 5.8 in |
| Header | Right-aligned small italic gray book title |
| Footer | Centered auto page numbers |

### Automatic image embedding

Supports both markdown image forms:

```markdown
# Inline: relative or absolute path
![caption](images/cover.png)

# Reference style (good for long books): define paths at end
![Fig 1-1 · data curve][fig-1-1]

[fig-1-1]: images/ch01-fig01.png "Data curve · Nuwa 37 days 18k stars"
```

Reference style also supports “path by ref name convention”—if the ref looks like `fig-1-1` but has no defined path, the tool looks under `--images-dir` for `ch01-fig01.png`. That convention keeps long books (many chapters, dozens of figures) from hand-maintaining a ref map.

### Dependencies

```bash
python3 -m pip install python-docx Pillow
```

Script auto-detects on start and prints a clear install command if missing.

Full cookbook: `references/md-to-docx-cookbook.md`.

## Cap 5: md → polished PDF (`scripts/md_to_pdf.py`)

Reuses Cap 2’s four html templates + Playwright/Chromium for publication-grade PDF. Two steps: md → html → pdf.

**Why Cap 5 instead of Cap 4 → pdf**: docx is for editing; pdf is for reading/print. Different layout languages. PDF via html keeps Cap 2’s four themes (article/report/reading/interactive)—richer options. DOCX goes straight OOXML with publisher page sizes (large 32mo/A4), no html hop.

### Invocation

```bash
# Default article theme + A4
python3 scripts/md_to_pdf.py article.md
python3 scripts/md_to_pdf.py article.md -o article.pdf

# Themes (same four as Cap 2)
python3 scripts/md_to_pdf.py article.md --theme article      # Tufte editorial (default)
python3 scripts/md_to_pdf.py report.md  --theme report       # wide table-dense whitepaper
python3 scripts/md_to_pdf.py post.md    --theme reading      # Medium minimal
python3 scripts/md_to_pdf.py book.md    --theme interactive  # collapsible TOC long tutorial

# Page size
python3 scripts/md_to_pdf.py article.md --page-size A4       # 210×297mm (default)
python3 scripts/md_to_pdf.py article.md --page-size A5       # 148×210mm
python3 scripts/md_to_pdf.py book.md    --page-size book     # 176×240mm large 32mo print book
python3 scripts/md_to_pdf.py article.md --page-size Letter   # 8.5×11in US

# Landscape + custom margins
python3 scripts/md_to_pdf.py wide.md --landscape --margin 18mm

# Keep intermediate html
python3 scripts/md_to_pdf.py article.md --keep-html
```

### Page sizes

| `--page-size` | Dimensions | When |
|---------------|------|--------|
| A4 | 210×297mm | Default; office/print/submission |
| A5 | 148×210mm | Handbooks, pocket |
| **book** | 176×240mm | China print large 32mo |
| Letter | 8.5×11in | US office |
| Legal | 8.5×14in | US legal |

### Dependencies

```bash
brew install pandoc                                   # already required
python3 -m pip install playwright                     # new
python3 -m playwright install chromium                # required once
```

Full cookbook: `references/md-to-pdf-cookbook.md`.

## Cap 6: md → polished EPUB (`scripts/md_to_epub.py`)

Wraps pandoc + [ebooklib](https://github.com/aerkalov/ebooklib) for standard EPUB3. Auto-embeds images, chapter splitting, cover/author/TOC metadata, publisher-taste built-in CSS.

**Why Cap 6 instead of raw pandoc `md → epub`**: pandoc epub cannot do “merge many md into a book + auto-embed local images + publisher CSS + full metadata” in one command. ebooklib gives finer EPUB3 control.

### Invocation

```bash
# Minimal: one md → one-chapter EPUB
python3 scripts/md_to_epub.py article.md --title "My Article" --author "Huashu"

# Many md → one book (one file per chapter)
python3 scripts/md_to_epub.py ch01.md ch02.md ch03.md \
    --title "Agent Skills Intro" --author "Huashu" \
    --cover ./assets/cover.jpg \
    -o agent-skills-intro.epub

# One md split on H1
python3 scripts/md_to_epub.py book.md --split-h1 \
    --title "Full Book Title" --author "Huashu" --cover cover.jpg

# Force chapter titles
python3 scripts/md_to_epub.py ch01.md ch02.md ch03.md \
    --chapter-titles "Chapter 1 Intro,Chapter 2 Practice,Chapter 3 Advanced" \
    --title "..." --author "Huashu"

# Full metadata
python3 scripts/md_to_epub.py book.md --split-h1 \
    --title "..." --author "Huashu" \
    --description "..." --pubdate 2026-05-11 --lang zh-CN
```

### Chapter splitting

| Input | Default behavior |
|------|---------|
| Single md | Whole book one chapter (first H1 as chapter title) |
| Multiple md | One file per chapter (CLI order) |
| Single md + `--split-h1` | Split into chapters on H1 |
| `--chapter-titles A,B,C` | Force-overwrite chapter titles |

### Default CSS

Built-in EPUB-optimized CSS (Source Han Serif + 1.8 line-height + terracotta orange accents + clear quote/code/table boundaries). **Intentionally avoids** CSS variables / clamp / grid—Kindle’s older engine and some domestic readers lack full support. `--custom-css` replaces the whole sheet.

### Automatic image embedding

Scans each chapter’s HTML for `<img src=...>`, reads local images into the EPUB `images/` subtree, and rewrites src. Default base is “directory of each md”; `--images-dir` overrides.

### Dependencies

```bash
brew install pandoc                          # already required
python3 -m pip install ebooklib Pillow       # new
```

Full cookbook: `references/md-to-epub-cookbook.md`.

### Boundary with huashu-book-pdf

| Scenario | Use |
|------|------|
| Single md → general-reader EPUB (Apple Books / Kindle / Duokan / Calibre) | **Cap 6** |
| Multiple md → simple collection EPUB | **Cap 6** |
| **WeChat Reading** listing (complex tables need PNG screenshot fallback) | **huashu-book-pdf** |
| Project-scale Orange Book full pipeline (versioning / R2 upload / huasheng.ai landing / WeChat Reading) | **huashu-book-pdf** |

## Typography floor (shared by all templates)

See `references/design-tokens.md`. Key parameters:

```
Body font (CJK)     PingFang SC, Source Han Serif, Noto Serif CJK
Body font (Latin)   Inter, IBM Plex Sans, et-book
Code font           JetBrains Mono, Fira Code
Line-height (CJK)   1.75 - 1.85
Line-height (Latin) 1.6
Font size (desktop) 17 - 18px
Font size (mobile)  16px
Max width (article) 680 - 720px
Max width (report)  760 - 820px
Paragraph gap       1em - 1.2em
Code block ground   #F6F8FA (light) / #1F2428 (dark)
Quotes              4px left color bar + light gray ground
Heading scale       h1 2em / h2 1.6em / h3 1.3em
```

**Ban list**: purple gradients, cyber neon, #0D1117 deep navy base, Comic Sans, emoji as formal icons.

## End-to-end workflows (typical scenarios)

```bash
# Scenario 1: PDF whitepaper → polished reading html
python scripts/any_to_md.py whitepaper.pdf -o whitepaper.md
python scripts/md_to_html.py whitepaper.md --theme report -o whitepaper.html

# Scenario 2: YouTube → blog article
python scripts/any_to_md.py "https://youtube.com/watch?v=xxx" -o video.md
# edit video.md...
python scripts/md_to_html.py video.md --theme article -o blog.html

# Scenario 3: Archive published blog → project source (Cap 3)
python scripts/html_to_md.py "https://example.com/blog/article" -o article.md

# Scenario 4: Fetch product/tech doc → full structured md (Cap 1)
python scripts/any_to_md.py "https://learn.microsoft.com/en-us/some-doc" -o doc.md

# Scenario 5: Orange Book chapter → multi-theme compare
python scripts/md_to_html.py chapter.md --theme article -o ch-article.html
python scripts/md_to_html.py chapter.md --theme interactive -o ch-interactive.html
# compare in browser; pick the better look

# Scenario 6: Unsure which URL path → run both and compare
python scripts/any_to_md.py "https://example.com/page" -o page-markitdown.md
python scripts/html_to_md.py "https://example.com/page" -o page-trafilatura.md
# see which fits your downstream use

# Scenario 7: Full Orange Book md → publisher review docx (Cap 4)
python scripts/md_to_docx.py md-v2/ch*.md md-v2/postscript.md md-v2/appendix.md --book \
    --title "Illustrated Agent Skills" \
    --subtitle "Teach AI to remember how you work" \
    --author "Huashu" \
    --images-dir ./images-v2 \
    -o Illustrated-Agent-Skills_publisher-review.docx
# 158 pages · 9 chapters + afterword + appendix + 57 figures · send straight to publisher editor

# Scenario 8: PDF paper/report → submission docx (Cap 1 → Cap 4)
python scripts/any_to_md.py paper.pdf -o paper.md
# edit paper.md to fix formatting...
python scripts/md_to_docx.py paper.md --page-size a4 -o paper.docx

# Scenario 9: md article → A4 PDF for friend/client (Cap 5)
python scripts/md_to_pdf.py article.md --theme article --page-size A4 -o share.pdf

# Scenario 10: single chapter → large-32mo print-book shape preview PDF (Cap 5)
python scripts/md_to_pdf.py chapter-3.md --theme article --page-size book \
    --margin-top 24mm --margin-bottom 24mm -o preview.pdf

# Scenario 11: multi-chapter md → general-reader EPUB (Cap 6)
python scripts/md_to_epub.py ch01.md ch02.md ch03.md \
    --title "..." --author "Huashu" --cover cover.jpg -o book.epub

# Scenario 12: PDF doc → md → re-typeset PDF (Cap 1 → Cap 5)
python scripts/any_to_md.py old.pdf -o old.md
# edit old.md content...
python scripts/md_to_pdf.py old.md --theme report --page-size A4 -o new.pdf

# Scenario 13: YouTube captions → md → EPUB for on-the-go reading (Cap 1 → Cap 6)
python scripts/any_to_md.py "https://youtube.com/watch?v=xxx" -o talk.md
# edit talk.md; clean timestamps...
python scripts/md_to_epub.py talk.md --title "..." --author "Huashu" -o talk.epub
```

## Error handling

| Scenario | Handling |
|------|------|
| markitdown missing | Script detects and prompts `pip install 'markitdown[all]'`; no silent fail |
| pandoc missing | Script detects and prompts `brew install pandoc` with official download URL |
| Input file missing | Fail immediately; do not pretend to continue |
| URL request failed (Cap 1 YouTube / Cap 3 URL) | Degrade with hint: check network/VPN/CDN |
| Empty conversion output | Warn: may be scanned PDF or image-heavy doc; suggest `--llm-describe` |
| Output html renders oddly | Check pandoc version (recommend ≥3.0) and template file integrity |
| python-docx missing | Script detects and prompts `python3 -m pip install python-docx Pillow` |
| Images missing in docx | Check `--images-dir` path, or whether ref `fig-N-X` maps to `chNN-figNN.png` naming |
| playwright (python) missing | Script detects and prompts `python3 -m pip install playwright && python3 -m playwright install chromium` |
| Chromium not downloaded yet | Run `python3 -m playwright install chromium`; on failure check https_proxy |
| md_to_pdf large images incomplete | Raise `--wait 5000` or longer |
| md_to_pdf CJK glyphs as boxes | System fonts missing—four theme CSS files already include PingFang SC / Source Han Serif fallback |
| md_to_epub "Document is empty" | Chapter wrap used xml prolog or xmlns—this script already uses plain html5 wrappers to avoid that |
| md_to_epub WeChat Reading tables lost | WeChat Reading engine is weak—use huashu-book-pdf’s screenshot-to-PNG path |
| md_to_epub cover not shown | Confirm jpg/png, valid path, file <2MB |

## References routing

| Task | Read |
|------|-----|
| markitdown best practices by file type | `references/markitdown-cookbook.md` |
| html→md tool combos for three scenarios | `references/html-to-md-cookbook.md` |
| Design philosophy + CSS for 4 html templates | `references/md-to-html-themes.md` |
| Visual art designer mode (fallback vs custom · when to escalate to AI) | `references/visual-designer-mode.md` |
| md→docx full cookbook (book mode / single file / submission) | `references/md-to-docx-cookbook.md` |
| md→pdf full cookbook (4 themes, page sizes, collaboration with book-pdf) | `references/md-to-pdf-cookbook.md` |
| md→epub full cookbook (chapter split, image embed, CSS compatibility) | `references/md-to-epub-cookbook.md` |
| Typography floor (fonts / line-height / width) | `references/design-tokens.md` |
| Anti-AI-slop floor (from huashu-design) | `references/anti-ai-slop.md` |

## Core reminders

- **Six capabilities have hard boundaries**: Cap 1 input side, Cap 2 html, Cap 3 reverse archive, Cap 4 docx publishing endpoint, Cap 5 pdf reading endpoint, Cap 6 epub ebook endpoint. Wrong decisions waste time.
- **Markdown is the source**—wherever it came from and wherever it goes, md is the pipeline center. html / docx / pdf / epub are products.
- **html must anti-slop**: purple gradients, emoji icons, SVG people—never. Aesthetic floor: `references/anti-ai-slop.md`.
- **URL dual path**: structured pages → Cap 1 (keep metadata+hierarchy+links); blog-like → Cap 3 (strip nav, body only). Heuristic—content to “read” → 3; to “look up” → 1.
- **docx is for editing, pdf for reading, epub for readers**: wrong product hurts downstream.
- **Cap 5/6 are stateless single-md conversions**: project Orange Book (multi-fragment / versioning / R2 / WeChat Reading) → huashu-book-pdf; do not recreate that release pipeline here.
- **Ask before doing**: which template, embed images?, LLM image describe?, single file vs book mode—clear it once; do not guess mid-flight.
- **External deps**: markitdown (pip), pandoc (brew), html-to-markdown (pip), python-docx (pip), playwright (pip + chromium), ebooklib (pip). Scripts self-check on start and prompt clearly when missing.
- **Python env trap**: on macOS `pip` and `python3` may point at different Python versions (seen in practice: `pip` → 3.11, `python3` → 3.14). Always install with `python3 -m pip install ...`, never bare `pip install`.

## Version self-check (silent)

For the AI agent: before each use of this skill, do an offline check—read `.last-update-check` in this skill directory (the directory containing SKILL.md). Contents: one line, date YYYY-MM-DD. If the file exists and is fewer than 30 days old, skip this section and work; say nothing about updates to the user.

Only when expired or missing:

1. This directory is not a git clone (no `.git` or no origin) → write today’s date and skip
2. Compare versions: `git -C <this-dir> rev-parse HEAD` vs `git -C <this-dir> ls-remote origin HEAD`
3. Regardless of result, write today’s date into `.last-update-check`
4. Same → say nothing; behind → finish the user’s current task first, then append one line: “This skill has a newer version; you can update with `git -C <this-dir> pull --ff-only`.” Whether to update is the user’s call—do not update proactively

---

Upstream huashu-md-html (MIT), alchaincyf.
