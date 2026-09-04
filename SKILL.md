---
name: engram
description: >
  Triggers: engram, distill [person]. Mind-first thinking advisor via
  six-agent research, triple-verified models, expression DNA, dual-agent
  fidelity. Stage 8 = stakes (skin in the game, why, productive urgency).
  Ordinary how-would-X → perspective skills.
---

# Engram

Read `CONSTITUTION.md` first. If a step would violate it, stop.

**Mind-first · stakes · pure-web / local-first · Unrecorded.** Default
product is a thinking advisor. Policy for mind-first and Stage 8 lives
in **Defaults** and **Stage 8** once — follow those, do not restate here.
Memory is additive and admission-gated.

**Required reading, in order, when you reach that phase:**

| Phase | File | Why |
|---|---|---|
| 0.5 | `references/schema.md` | Directory layout (01–06 ledgers) |
| 1 | this file, agent table | Six research agents |
| 0B | `references/vague-need.md` | No-name demand → candidate cards |
| 1 / scenarios | `references/special-scenarios.md` | Living/historical, China allowlist, obscure, self-distill |
| 1 / tools | `references/info-gathering-skills.md` | Recommended helpers — install for max Phase 1 quality |
| 1.5 | `scripts/merge_research.py` | Empirical review table |
| 2 | `references/extraction-framework.md` | Triple verification, DNA, contradictions |
| 3 | `references/skill-template.md` | Runtime skeleton |
| 3 | `references/agentic-protocol.md` | Derive Step-2 tracks; calibration; Step-3 packaging |
| 4 | `scripts/quality_check.py` then `references/fidelity-scorecard.md` | Mechanical QA + independent scorecard |
| 8 / opt-in | `references/optional-immersion.md` | Immersion / CTT only when asked |
| before run | `references/version-self-check.md` | Silent 30-day update check (I4 non-git skip) |
| memory | Constitution four tests + schema TRACE record | Additive, after models exist |

Synthesize from ledgers and required files only. Read the files when
that phase starts.

## Defaults

- **Mind-first.** Default use = thinking advisor / mind. After the mind
  ships, **Stage 8 = stakes** (skin in the game, why-of-existence,
  productive urgency) — corpus-grounded, evidenced urgency over invented
  pathos. Soft immersion / persona texture / CTT stays **off** unless
  asked (see `references/optional-immersion.md`). Prefer writings,
  models, heuristics, and real stakes.
- English runtime. Sources stay in their original language.
- Write only under `<skills-root>/engrams/<slug>/`.
- Tier: **standard** unless they pick fast or deep.
- Public figure + no extra detail: public corpus, disclosed sim.
- Private figure: halt for consent and corpus.
- Books: user-supplied files or otherwise legal access only (I1).

Proceed on Phase 0 clarifying questions that have defaults.
Halt on consent, deception, and a CTT claim with no intimate sources.

**Quality gates 1.5 and 2.5 pause.** They are not Phase 0 questions.
Pause after the research table and after the synthesis summary unless
the user already gave an explicit run-through waiver (they said "run
through", "don't stop at checkpoints", or "skip the gates"). Record
`waiver: run-through` once in the 0.5 notes. Anything vaguer → pause.

## Phase 0 — Eligibility and clarifying

Phase 0 entry:

1. Who is the person (confirm identity).
2. Full portrait vs one dimension.
3. Use: thinking advisor / mind (default), immersion/texture, or both.
   Default is **mind only**. Solicit intimate drops only when they asked
   for immersion, CTT, or texture. Stage 8 (stakes) is a post-mind gate,
   not an intimate drop.
4. New vs update (scan `<skills-root>/engrams/` and
   `<skills-root>/personas-skillset/`).
5. **Resource drop** (enrichment first). Ask for primary files that
   strengthen the **mind** (books, essays, transcripts, decision memos).
   Classify with the **File type → ledger** table in Phase 1; keep one map.
   Copy into `sources/` at 0.5.
   - Books, transcripts, captions, posts, memos, notes: that table.
   - Raw audio/video: transcribe, then `sources/transcripts/`. There is
     **no** `sources/media/` folder.
   - Business memos / decision logs → ledger 05, never 07.
   - **Texture files** (letters, messages, home recordings): solicit
     **only** if use includes immersion / CTT. If they volunteer them
     anyway: mark `intimate: yes` and confirm consent if living, then
     ledger 07. Prefer empty 07 over invented tics. Unrecorded when no
     MEMORY trace (false-memory veto).
6. Tier:

| Tier | Scale | When |
|---|---|---|
| Fast | Writings + conversations + expression, cap ~5 sources each | Smoke test |
| Standard (default) | All six research dimensions | Most work |
| Deep | Six dimensions + full ingest of user primaries (+ 07 only if immersion asked + supplied) | Release-quality mind; immersion/CTT only if requested |

**Before spawning agents, confirm the tier and state the cost magnitude.** A full standard distill is a long
multi-agent research job — full standard runs can cost on the order of tens of dollars on a top model; fast runs
about 1/3 of standard, deep costs the most. Fast is the cheap smoke test. Deep is for a
release-quality engram with a full primary ingest. Name the tier and its magnitude before spending.
Start the swarm only after the tier is named (default:
standard, if they already said "just do it").

**Drop vs halt (align with tier):**
- Fast / standard, public figure, no files → **suggest**, then
  `mode: pure-web`. Ceiling = **mind** (+ thin public texture if it falls
  out of essays). Mind-only runs treat missing intimate corpus as out of
  scope, not a defect.
- Deep, CTT, self-distill, or living private person, no files → **halt**.
  Those runs need a supplied corpus.
- Files dropped → `mode: local-first` (or `pure-local` if they said
  only-use-what-I-gave-you). Ceiling rises with what landed. Mind-only
  runs succeed without Stage 8.

I1 is unchanged: user-supplied or legal copies only. A drop gate is how
books get in.

If they said "distill me" / "make a skill of myself", follow **Special
scenarios → Distill yourself** in `references/special-scenarios.md`.
Prefer their supplied corpus over web-searching them as a public figure
unless they also have a public corpus and asked for that.

### Phase 0B — Vague need (no name yet)

If they named a person, skip this and go 0A → 0.5.
If they only have a problem, read `references/vague-need.md` and
follow that procedure (demand table → person vs topic → ≤3 candidates).

## Phase 0.5 — Create the directory before research

Read `references/schema.md` and create that tree **before** any agent
runs. Copy this skill's `CONSTITUTION.md` in. Every subagent writes its
ledger inside the engram folder. Research that is not a file did not
happen. The folder must be self-contained.

**Completion checklist (run before Phase 1):**
- [ ] Directory exists at `<skills-root>/engrams/<slug>/` with
      `references/research/` and `sources/{books,transcripts,articles}/`
- [ ] `CONSTITUTION.md` copied in
- [ ] If this is an update: existing SKILL.md read; stale slices marked
- [ ] If the user supplied files: copy them into `sources/` by the
      Phase 1 file-type table (not a second map). Then mark
      **local-corpus mode** in the run notes:
      `mode: local-first` or `mode: pure-local`
- [ ] Texture files: `intimate: yes` only with consent if living;
      then create `07-intimate.md`. Memos stay 05.
- [ ] If no user files and the run is fast/standard public-figure:
      mark `mode: pure-web` (ceiling = mind; public texture incidental)
- [ ] If no user files and the run is deep / CTT / self-distill /
      living private: **halt**. Prefer halt over marking pure-web.
- [ ] If the subject is Chinese-language: **switch source strategy now**
      (`references/special-scenarios.md` → China vs West). Prefer original
      Bilibili / Xiaoyuzhou (or Ximalaya original audio) and the Chinese
      outlet allowlist.
- [ ] If unique usable sources look like they will be <10: run the
      **obscure-person procedure** now (warn, 2–3 models, expand
      honest boundary). Surface this before Phase 4.

## Phase 1 — Six-agent corpus

### Acquisition mode (pick one, write it down)

| Mode | Trigger | Strategy |
|---|---|---|
| **pure-web** (default) | No user files | All six agents search the public web. Books they need must be user-supplied or otherwise legally available |
| **local-first** | User dropped PDFs, transcripts, captions, exports | Run the four-step local-first procedure. Web fills *gaps only* |
| **pure-local** | User said "only use what I gave you" or the subject is a private person with a supplied corpus | No web. Six agents read `sources/` only. Thin ledgers stay thin and get labeled |

### Local-first procedure (copy this; do not improvise)

1. **Classify** every file in `sources/` into one or more ledgers using the file-type table below. One book may cover writings + expression.
2. **Gap check.** For each of 01–06, is coverage enough to extract (multiple primary claims, not a single quote)? List strong / thin / empty.
3. **Search only the gaps.** Spawn web agents solely for empty or thin ledgers. Skip web on ledgers already strong from local files.
4. **Label origin** on every item: `user-supplied` vs `web`. Keep those labels distinct.

### File type → ledger

| User file | Put in | Ledgers it feeds |
|---|---|---|
| Book PDF / EPUB | `sources/books/` | 01 writings, 03 expression |
| Talk / interview transcript | `sources/transcripts/` | 02 conversations, 03 expression |
| Video captions SRT / VTT | `sources/transcripts/` (after `srt_to_transcript.py`) | 02 conversations, 03 expression |
| Blog / newsletter export | `sources/articles/` | 01 writings, 03 expression |
| Social export (posts) | `sources/articles/` | 03 expression |
| Internal memo / decision log | `sources/articles/` | 05 decisions (never 07) |
| User's own notes | `sources/articles/` | Secondary cross-check only, unless they are the subject |
| Texture files (letters, messages, home recordings) | `sources/articles/` + `intimate: yes` after consent | 07 intimate only |
| Raw audio / video | transcribe (via installed video-transcript skill per `references/info-gathering-skills.md`, else available tooling), then `sources/transcripts/` | 02, 03. No `sources/media/` |

**Dry-run calibration (do not search):** a drop of `Foo.pdf` + `Bar.srt` →
copy to `sources/books/Foo.pdf` and `sources/transcripts/Bar.srt`;
mode = local-first; PDF feeds 01+03; SRT feeds 02+03; spawn web only
for 04, 05, 06 (and 01–03 if those files are too thin after reading).

Spawn six parallel agents when the runtime allows; otherwise run them
in series and save after each. Same six-way split:

| Agent | File | Hunt | Extract |
|---|---|---|---|
| 1 Writings | `01-writings.md` | Books, long essays, papers, newsletters | Claims that recur ≥3 times, coined terms, reading lists |
| 2 Conversations | `02-conversations.md` | Podcasts, long video, AMA, interviews | How they answer when pressed, improvisation, changed minds, refusals |
| 3 Expression | `03-expression-dna.md` | Short posts, debates, fragments | Sentence fingerprint, tics, humor, public fights |
| 4 External | `04-external-views.md` | Criticism, biography, comparison | Outside patterns, controversies, peer contrast |
| 5 Decisions | `05-decisions.md` | Dated actions, turning points | Reasons given, later regret, talk vs walk |
| 6 Timeline | `06-timeline.md` | Birth/debut → now | Milestones, thought-shifts, **last 12 months** |

**Optional 7 Intimate** — `07-intimate.md` — **only** from user-supplied
letters, messages, home recordings, relationship speech. Prefer empty
07 over scraping private accounts. Empty = public texture only.

### Hard rules for every agent

- Write `references/research/0N-*.md` inside the engram folder.
- Every item: locator + confidence. `Subject said` vs `Witness said` vs
  `Inference`.
- Keep contradictions. Prefer unresolved tension over smoothing.

### Agent prompt (copy, fill the name)

```
Your task: research [Name] for the [writings|conversations|…] ledger.

Search toward: [use the Hunt column]

Write to [engram]/references/research/[filename]
Every item: URL or file path, and primary vs secondary.
Keep contradictions. Prefer unresolved tension over reconciling them.

Prefer first-party writing, recorded interviews, filings, and serious
reporting. Skip quote-farm pages, Zhihu, WeChat public accounts, and
Baidu Baike (see references/special-scenarios.md blacklist).
```

### Tools

Scripts live in **this pack** (`scripts/` in this pack), not inside each
output engram. Invoke them from this skill directory (or with
an absolute path to that `scripts/` folder). Prefer English captions
first (English runtime).

- **Books:** copy user-supplied or legally obtained files into
  `sources/books/` and read them. User-supplied or otherwise legal access only (I1). If a book is needed and not supplied, leave ledger 01 thin
  and say so.
- **Captions:** `bash scripts/download_subtitles.sh <YouTube_URL> <out-dir>`
  then `python3 scripts/srt_to_transcript.py <input.srt> <sources/transcripts/…>`
- **Podcasts:** search for published transcripts (e.g. podcastnotes.org
  and the show's own site) before relying on captions.
- Phase 1.5: `python3 scripts/merge_research.py <engram-dir>`
- Phase 4: `python3 scripts/quality_check.py <engram-dir>/SKILL.md`

#### Recommended info-gathering skills

Before spawning Phase 1 agents, scan `<skills-root>/` and follow
`references/info-gathering-skills.md`. These helpers are **recommended
for max-quality distills** — if a job has no matching skill, tell the
user what to install. Match by job; missing helper ≠ skip ledger; I1
still binds.

### Source priority

User primary > own long form > long interviews > dated actions >
social fragments > other people's analysis. Secondary paraphrase is
low weight.

### Blacklist (one-liner)

Zhihu / WeChat public accounts / Baidu Baike / quote farms — never as
sources. Full blacklist + Chinese outlet allowlist:
`references/special-scenarios.md` (China vs West).

### Failure table

| Trigger | First fix | Then |
|---|---|---|
| No parallel agents | Serial ledgers, save each | Single agent, six passes |
| Context overflow | Stop at phase boundary; files are the checkpoint | Split sessions 0–1 / 1.5–2.5 / 3–5 |
| Cost surprise | Tier was the gate | Stop; already-written ledgers are the deliverable |
| One agent times out | Continue; mark thin | Honest boundary |
| Search tools down | Fetch / browser / installed research skills | Local-corpus-only |
| <10 usable sources | Warn at 0.5; 2–3 models | Expand honest boundary |
| Agent conflict | Keep it | Unresolved tensions |

Prefer a labeled 60 to a fabricated 90.

### Phase 1.5 checkpoint — PAUSE

Run `python3 scripts/merge_research.py <engram-dir>` and show the table
(source counts, primary share, holes, contradictions).

**Stop.** Ask: research OK to synthesize, or supplement a thin ledger?
Start Phase 2 only after they answer, unless `waiver: run-through` is
already recorded. Garbage in, garbage out — this gate exists so Phase 4
is not where you discover empty ledgers.

If they name a weak ledger, research that slice again, re-run merge,
then pause here once more.

## Phase 2 — Synthesis (must read the framework)

**Read `references/extraction-framework.md` all the way through.**
Then extract:

1. **Mental models (3–7).** Scan 01–05, list 15–30 candidates, run
   triple verification (cross-domain, generative, exclusive). 3/3 =
   model; 1–2 = heuristic; 0 = drop. Rank by exclusivity. Each model:
   name, one line, ≥2 scene evidence, apply, limit.
2. **Heuristics (5–10).** If X then Y, with a case.
3. **Expression DNA.** Do the 20-paragraph fingerprint and style poles
   in the framework. Taboos and tics.
4. **Values, anti-patterns, tensions (≥2).**
5. **Lineage.**
6. **Honest boundary.**
7. **Memory traces (additive).** After the mind exists, admit traces
   from 02, 05, 06, 07 with the four tests. Write `MEMORY.md` per
   schema. Flavor fails necessity.

Write `MIND.md`, `PERSON.md`, `MEMORY.md`, `RELATIONSHIPS.md`.

### Phase 2.5 checkpoint — PAUSE

Show: model names (3–7), heuristic count, three DNA features, tensions,
boundary line count, admitted-trace count.

**Stop.** Ask: models OK to build the runtime skill, or revise Phase 2?
Start Phase 3 only after they answer, unless `waiver: run-through` is
already recorded. Synthesis is the most subjective step — write the
runtime skill on confirmed lenses.

## Phase 3 — Runtime skill

**Read `references/skill-template.md` and fill every section.**
Fill the template skeleton; keep structural parity.

**After 2.5 OK, finish Phase 3 SKILL before starting Phase 4 fidelity.**

### Fill table

| Template section | Fill from |
|---|---|
| frontmatter description | Source + model counts + triggers. **~300 chars; hard fail ~1024.** Positioning + triggers ("[Name] perspective") + one stay-off line. Name + exclusive concepts match; avoid keyword stuffing. |
| Role-playing rules | Template defaults (inference label, distinguishable quotes, memory retrieval). Keep as written. |
| **Agentic Protocol** | **Derive Step-2 tracks from *this* subject's models.** See HOW-TO below; calibration table in `references/agentic-protocol.md`. |
| Identity card | Timeline (06) + writings (01) → ~50 words in their voice |
| Mental models | Phase 2.1, each with name / evidence / apply / limit |
| Heuristics | Phase 2.2, each with when + case |
| Expression DNA | Phase 2.3 → runtime style rules |
| Timeline | Agent 6, key nodes only |
| Values / anti-patterns | Phase 2.4 |
| Lineage | Phase 2.5 |
| Honest boundary | Phase 2.6 + cutoff date |
| Sources | Six agents, primary vs secondary |
| Attribution | Engram line (I3) |
| Peer curiosity | Scan personas-skillset + engrams; `PEERS.md`; **ask once to speak with** a useful peer before answering alone when their lens fits the task; disclosed peer use, single ask |

Also:

- Wire memory retrieval: search `MEMORY.md` before autobiographical claims.
  No admitted TRACE → `Unrecorded`.
- One-time disclosure, then stay in character for immersion.
- Walk the quality self-check at the end of `references/extraction-framework.md`.
  Mark misses and return to the matching phase.
- Write the finished SKILL.md to `<skills-root>/engrams/<slug>/SKILL.md`.

### Phase 3 ship checklist

Shipped SKILL.md **MUST** include:

- [ ] **Evidence classes** role rule (`Subject said` / `Witness said` /
      `Verified event` / `Inference` / `Unrecorded` / `Unknown`)
- [ ] **Full Step-3 sequence** (not a one-liner): stakes check +
      stakes/why → mechanism → caveat/stewardship → recommendation →
      dated tension → what would change my mind (+ labeling bullets)
- [ ] **Denser Evidence URLs:** ≥2 scenes per model with locatable
      primary URLs or DOIs inline — not name-only citations
- [ ] **Self-contained Sources** listing key primary URLs even if full
      ledgers live in shared `references/research/`
- [ ] **Fluid spoken attribution:** Evidence classes stay; answers use
      prose locators ("as I wrote…"), not `[Subject said]` bracket spam
- [ ] **Tension dual-voice:** each Subject↔Witness conflict ships a short
      Subject primary quote beside Witness (Values / Limits / Latest)
- [ ] Short frontmatter description (~300 chars); concrete Step-2
      look-ats; MEMORY TRACE / Unrecorded discipline; named peers when
      present

Do not thin Step-3 or Evidence classes to chase line-count. Packaging
rules: `references/agentic-protocol.md`.

### Agentic Protocol generation

**Why / where:** engram *works* like them (research before vibe). Fill
the Answer-workflow skeleton in `references/skill-template.md` after
role-playing rules, before the identity card.

**Shape:** three steps; Step 2 tracks from *this* subject's models.
Derive by inverting models into what they inspect. Calibration
(Munger / Feynman / Taleb / MrBeast) + paper exercise:
`references/agentic-protocol.md` — prefer subject-specific tracks over
pasting those rows.

**Constraints:** tracks from models (not "search related information");
each names what to search and which data; group by question type when helpful.

**Judgment call (ship in Step 1):** if the answer would be materially worse
without current information, research first. Rather search once more than
fabricate from training data. Required in `skill-template.md`; do not drop it.

## Phase 4 — Validation + scorecard

1. Run `python3 scripts/quality_check.py <SKILL.md>`. Fix FAILs.
2. Independent answerer (engram folder only, no web) vs independent
   judge using `references/fidelity-scorecard.md` (stance 30, style 20,
   edge 20, source 15, structure 15). Write `FIDELITY.md`.
3. Pass table:

| Check | Pass | Fail signal |
|---|---|---|
| Models | 3–7, each evidenced | <3 or >10 |
| Limits on each model | Named failure | Only virtues |
| Expression DNA | 100 words identifiable | Generic assistant |
| Honest boundary | ≥3 concrete | Only "not the real person" |
| Tensions | ≥2 | Too consistent |
| Primary share | >50% | Mostly second-hand |

4. Engram vetoes in the scorecard addendum (false memory; relational
   register if 07 exists). Veto overrides an A.
5. Iterate Phase 2→4 at most twice, then ship with holes labeled.
6. Show the scorecard and ask for confirmation before calling it done.

Informed CTT only / no deceptive relative tests: run CTT only if they
name an evaluator and 07 exists.

## Phase 5 — Dual-agent refine

After a passing scorecard, two parallel passes:

- **A — structure (8 dims, score 1–5 each):** workflow clarity; boundary /
  stop; checkpoints; instruction concreteness; first action on activation;
  failure/degrade paths; template completeness; length/loader cost.
  Dry-run 3 typical prompts; rewrite the two weakest.
- **B — activation:** trigger coverage for real use; role-play
  operability (question routing, frequency/anti-drift constraints,
  failure prevention); missing facts; 2–3 concrete patches with
  after-text examples.

Apply non-conflicting edits. Show a diff summary and ask for confirmation. Prefer edits that make
the skill *run* over length alone.

## Updates

Read cutoff; refresh agents 2 + 5 + 6 (and 7 if new intimate files);
patch models only on contradicting evidence; prefer surgical patches.

## Taste rules (when a judgment is hard)

Phase 4 has the quantified bars. Tie-breakers: **long-form > quotes**;
**controversy > consensus**; **change > fixed**.

## Anti-patterns (never)

Core ten, then Engram extras. Each row is a veto, not a vibe.

| # | Anti-pattern | Why / instead |
|---|---|---|
| 1 | Invent quotes they never said | Famous-quote farms are full of fakes. Locator or drop it |
| 2 | Package generic wisdom as their unique insight | Fails exclusivity; it is not a mental model |
| 3 | Ignore criticism and controversy | Agent 4 is the fan-filter. Thin negative share = research fail |
| 4 | Force a 90 on thin data | Ship a labeled 60. Prefer labeled thin over fabricated completeness |
| 5 | Use Zhihu / WeChat public accounts / Baidu Baike | Rewritten, closed, unverifiable. No ledger, no dimension |
| 6 | One-shot a small context window through the whole pipeline | Context explodes between Phase 1 and 2. Split per the failure table |
| 7 | Start the swarm without a tier | Full distill is a heavy job. They pick fast / standard / deep first |
| 8 | Distill a living private person without a boundary | User-supplied corpus + consent |
| 9 | Ship without anti-drift | Role-play rules + expression DNA in the template must survive edits |
| 10 | Turn checkpoints into delivery blocks | Phase 0 gets defaults. 1.5 and 2.5 pause unless `waiver: run-through` |
| 11 | Unauthorized book acquisition | Intentional cut I1. User-supplied or legal copies only |
| 12 | Write to `.claude/skills/` | I2. Write only under `<skills-root>/engrams/<slug>/` |
| 13 | Edit this distiller mid-run without a version bump | Treat the pack as read-stable during a distill; change it between runs |
| 14 | Deceptive Character Turing Test | Informed CTT only / no deceptive relative tests |
| 15 | Fill childhood / grief from prior or "texture" | Unrecorded when no MEMORY trace (false-memory veto) |
| 16 | Accent / trauma costume | Voice is diction and attention, not a cartoon of pain |
| 17 | Reconcile tensions into one smooth personality | Contradictions stay. Prefer unresolved tension over a flattened portrait |

## Special scenarios

When a scenario applies, read `references/special-scenarios.md` and
follow that procedure (living/historical, topic vs person, China/West
allowlist, obscure, distill yourself).

## Stage 8 — Stakes (skin in the game / why / productive urgency)

Only after a mind engram ships (G7-class quality). Does **not** count
for process completeness. Does **not** block shipping the mind — but
it is the natural next hill: make the advisor **invoke** why it exists,
not float as a clever abstract model deck.

**What stakes means here**
- **Why-of-existence:** concrete user/job + subject's through-line that
  makes their judgment worth consulting.
- **Skin in the game:** what they risked, paid, abandoned, or refused to
  abandon — from the corpus. Prefer evidence over invented biography.
- **Productive urgency:** when the corpus shows accelerate / cut / refuse
  delay. Wire runtime triggers for pressure without pathos cosplay.

**Work**
1. Write `STAKES.md` (or `references/research/08-stakes.md` + short runtime section).
2. Fill from 01/02/05/06: downside decisions, public costs, through-lines, kill-criteria.
3. Runtime: retrieve STAKES before high-leverage advice; name the why;
   refuse advice that ignores their real constraints.
4. Probe: consequential framing should change the answer as the corpus would.

**Gate G8 — PASS when**
- [ ] G7 already green
- [ ] `STAKES.md` (or 08-stakes) has evidenced why / skin / urgency
- [ ] Runtime SKILL retrieves stakes before consequential advice
- [ ] Stakes probe PASS (urgency without invented pathos; Unrecorded
      where corpus is silent)
- [ ] Soft immersion not smuggled in as a substitute for stakes

**Immersion / CTT:** see `references/optional-immersion.md` (opt-in only,
user-supplied, informed CTT, empty 07 fine).

## Done

Self-contained `<skills-root>/engrams/<slug>/`: ledgers 01–06,
template-complete SKILL.md, `FIDELITY.md`, `quality_check.py` PASS,
ceiling **mind** by default; writes confined to that folder (+ this chat).
Mind ships at G7; Stage 8 (stakes) is the next hill. Immersion / CTT
only if separately requested with corpus.

## Version self-check (silent)

Before a distill run, follow `references/version-self-check.md` (30-day check; I4: non-git installs skip quietly).
