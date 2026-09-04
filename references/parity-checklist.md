# Engram ↔ Nuwa process-parity checklist

**Frozen:** 2026-09-03 (America/Chicago)  
**Re-scored:** 2026-09-04 against **engram-v2** (not pre-v2 lean / frozen v1)  
**Baseline pack:** `this repository / ` vs `upstream Nuwa checkout / `  
**Scorer rule:** re-score by reading the Engram pack (SKILL.md + references + scripts). No vibes. An item is PASS only if an agent following Engram alone would execute the same *procedure*, not merely nod at the idea. Side-file OK if SKILL points in-flow and an agent would open it.

## Score vocabulary

| Score | Meaning |
|---|---|
| **PASS** | Present at comparable specificity to Nuwa |
| **PARTIAL** | Mentioned, thinner, wrong default, or only in a side file when Nuwa has it in-flow |
| **FAIL** | Missing as an operable procedure |
| **INTENTIONAL** | Deliberate cut; must stay documented; does not count against the ≥95% target |

## Scores

| Metric | Stage 0 freeze | Claimed Stage 6 (pre-v2 lean) | **2026-09-04 engram-v2 re-score (after fixes)** |
|---|---|---|---|
| Core items (excl. INTENTIONAL + Additive) | 69 | 69 | **69** |
| PASS | 44 | 69 (claimed) | **69** |
| PARTIAL | 11 | 0 (claimed) | **0** |
| FAIL | 14 | 0 | **0** |
| Weighted `(PASS + 0.5×PARTIAL) / 69` | ~72% | ~100% (claimed) | **100%** |
| Strict `PASS / 69` | ~64% | ~100% (claimed) | **100%** |

Pre-fix re-score on lean v2 alone: **2 PARTIAL** (C61 Agent B thinner than Nuwa; C71 version-self-check easy to miss — not in required-reading table) → weighted **~98.6%** / strict **~97.1%**. Both closed in this pass.

Additive Engram layers (memory, stakes Stage 8, immersion/CTT, peer curiosity) are **out of scope** for this checklist. They do not raise or lower Nuwa parity.

---

## INTENTIONAL cuts (locked)

Do not “fix” these into Nuwa behavior.

| ID | Cut | Why |
|---|---|---|
| I1 | No Z-Library / LibGen / pirate book download | Legal / safety |
| I2 | Write path `~/.tink/skills/engrams/<slug>/` not `.claude/skills/*-perspective` | User skill layout |
| I3 | Fork attribution (Engram) not 花叔 / Nuwa creator block | Honest fork credit |
| I4 | Engram need not be a git clone | Version check ports Nuwa's non-git skip; current install is not a clone |

---

## Checklist items

Status + Evidence = **fresh 2026-09-04 engram-v2** citations (file:section).

### Phase 0 / 0A

| ID | Item | Status | Evidence / gap | Closes in |
|---|---|---|---|---|
| C01 | Entry split: named person vs vague need | PASS | SKILL.md Phase 0 + `### Phase 0B` pointer to vague-need.md | — |
| C02 | Clarify: identity | PASS | SKILL.md Phase 0 §1 "Who is the person" | — |
| C03 | Clarify: full vs focused portrait | PASS | SKILL.md Phase 0 §2 | — |
| C04 | Clarify: use case | PASS | SKILL.md Phase 0 §3 thinking advisor / immersion / both | — |
| C05 | New vs update + scan existing skills | PASS | SKILL.md Phase 0 §4 scans engrams + personas-skillset | — |
| C06 | Ask for local corpus before search | PASS | SKILL.md Phase 0 §5 Resource drop | — |
| C07 | Tier table fast / standard / deep with source caps | PASS | SKILL.md Phase 0 tier table; fast cap ~5 | — |
| C08 | Defaults when user says just-do-it (non-blocking) | PASS | SKILL.md Defaults + "Proceed on Phase 0 clarifying questions that have defaults" | — |
| C09 | Cost magnitude disclosed before run | PASS | SKILL.md "Before spawning agents, confirm the tier"; name long multi-agent job; no invented dollar figure | Stage 1 |

### Phase 0B

| ID | Item | Status | Evidence / gap | Closes in |
|---|---|---|---|---|
| C10 | Demand-dimension table (10 categories) | PASS | `references/vague-need.md` Step 1 ten-row table; SKILL Phase 0B "read … follow that procedure" | Stage 3 |
| C11 | Max 2 follow-ups then recommend | PASS | vague-need.md "At most two follow-ups" | — |
| C12 | Candidate card: lens / fit / limit; max 3 | PASS | vague-need.md Step 3 card template (Lens / Why / Limit); max 3 | Stage 3 |
| C13 | Prefer existing local skills before new distill | PASS | vague-need.md Source A first; existing skills first rule | — |
| C14 | Person vs topic skill choice at intake | PASS | vague-need.md Step 2; points at special-scenarios topic table | Stage 3 |

### Phase 0.5

| ID | Item | Status | Evidence / gap | Closes in |
|---|---|---|---|---|
| C15 | Create directory before research | PASS | SKILL.md Phase 0.5 + schema.md | — |
| C16 | Tree: research 01–06 + sources/{books,transcripts,articles} | PASS | `references/schema.md` tree | — |
| C17 | Self-contained: research inside skill dir | PASS | SKILL.md 0.5 "folder must be self-contained" | — |
| C18 | China-subject source strategy switch at 0.5 | PASS | SKILL.md 0.5 checklist → special-scenarios.md China vs West | Stage 5 |
| C19 | Copy user corpus into sources/ + mark local-corpus mode | PASS | SKILL.md 0.5 checklist: copy + `mode: local-first / pure-local / pure-web` | Stage 1 |

### Phase 1 — acquisition

| ID | Item | Status | Evidence / gap | Closes in |
|---|---|---|---|---|
| C20 | Three modes: pure-web / local-first / pure-local | PASS | SKILL.md Phase 1 Acquisition mode table | Stage 1 |
| C21 | Local-first four-step (classify → gaps → search gaps → label origin) | PASS | SKILL.md "Local-first procedure" numbered 1–4 | Stage 1 |
| C22 | File-type → ledger coverage table | PASS | SKILL.md "File type → ledger" table | Stage 1 |
| C23 | Six agents; filenames 01–06 match Nuwa | PASS | SKILL.md agent table same filenames | — |
| C24 | Per-agent hunt + extract match Nuwa | PASS | SKILL.md Hunt / Extract columns | — |
| C25 | Hard rules: file, confidence, said-vs-about, keep contradictions | PASS | SKILL.md "Hard rules for every agent" | — |
| C26 | Agent prompt template | PASS | SKILL.md "Agent prompt (copy, fill the name)" | — |
| C27 | Subtitle download + SRT clean scripts | PASS | `scripts/download_subtitles.sh` + `srt_to_transcript.py`; SKILL Tools (pack-local path noted 2026-09-04) | — |
| C28 | merge_research.py + quality_check.py | PASS | Both under `scripts/`; referenced at 1.5 and Phase 4 | — |
| C29 | Scan named info-gathering skills | PASS | `references/info-gathering-skills.md` five Nuwa names by job; SKILL "Named info-gathering skills" | Stage 5 |
| C30 | Podcast transcript sites hint | PASS | SKILL.md Tools: podcastnotes.org + show's own site | Stage 1 |
| C31 | Source priority (user → own long form → …) | PASS | SKILL.md "Source priority (Nuwa)" | — |
| C32 | Blacklist Zhihu / WeChat / Baidu | PASS | SKILL.md Blacklist one-liner + special-scenarios.md Blacklist section | — |
| C33 | Chinese authoritative outlet allowlist | PASS | special-scenarios.md Chinese outlet allowlist (36氪…机器之心) + Bilibili/Xiaoyuzhou | Stage 5 |
| C34 | Book via Z-Lib/LibGen | INTENTIONAL | I1; SKILL Defaults + Tools refuse | — |
| C35 | Failure / degrade table | PASS | SKILL.md "Failure table (Nuwa, kept)" seven rows | — |
| C36 | Prefer labeled 60 over fake 90 | PASS | SKILL.md "Prefer a labeled 60 to a fabricated 90" | — |

### Phase 1.5 / 2 / 2.5

| ID | Item | Status | Evidence / gap | Closes in |
|---|---|---|---|---|
| C37 | 1.5 checkpoint + merge_research table | PASS | SKILL.md Phase 1.5; run merge_research.py | — |
| C38 | 1.5 default **pause** for user OK | PASS | SKILL.md "**Stop.** Ask…"; Defaults `waiver: run-through` | Stage 2 |
| C39 | Must read extraction-framework.md | PASS | SKILL.md Phase 2 first line; required-reading table | — |
| C40 | 15–30 candidates → triple verify → 3–7 by exclusivity | PASS | SKILL.md Phase 2 §1 + extraction-framework.md §1 | — |
| C41 | Heuristics 5–10 with cases | PASS | SKILL.md Phase 2 §2 | — |
| C42 | Expression DNA (fingerprint / poles) | PASS | SKILL.md Phase 2 §3 → framework §2 | — |
| C43 | Values, anti-patterns, tensions | PASS | SKILL.md Phase 2 §4 | — |
| C44 | Intellectual lineage | PASS | SKILL.md Phase 2 §5 | — |
| C45 | Honest boundary | PASS | SKILL.md Phase 2 §6 | — |
| C46 | 2.5 synthesis summary checkpoint | PASS | SKILL.md Phase 2.5 show list | — |
| C47 | 2.5 default **pause** for user OK | PASS | SKILL.md Phase 2.5 "**Stop.**"; waiver same as 1.5 | Stage 2 |

### Phase 3

| ID | Item | Status | Evidence / gap | Closes in |
|---|---|---|---|---|
| C48 | Fill skill-template.md every section | PASS | SKILL.md Phase 3 + fill table; template spine | — |
| C49 | Frontmatter ~300 / loader ~1024 warning | PASS | SKILL.md fill table + skill-template.md Frontmatter cap | Stage 4 |
| C50 | Agentic Protocol classify / research / answer | PASS | skill-template.md Answer workflow Steps 1–3; SKILL Agentic Protocol generation | — |
| C51 | Step-2 worked examples (Munger/Feynman/Taleb/MrBeast) | PASS | `references/agentic-protocol.md` calibration table; SKILL points there | Stage 4 |
| C52 | Walk framework quality checklist after build | PASS | SKILL.md Phase 3 "Walk the quality self-check"; framework §6 | — |
| C53 | Creator attribution = Nuwa/花叔 block | INTENTIONAL | I3; fill table "Engram fork line" | — |

### Phase 4 / 5

| ID | Item | Status | Evidence / gap | Closes in |
|---|---|---|---|---|
| C54 | Independent answerer (no web) | PASS | SKILL.md Phase 4 §2; fidelity-scorecard.md Procedure | — |
| C55 | Nuwa six-row pass table | PASS | SKILL.md Phase 4 pass table | — |
| C56 | Iterate 2→4 at most twice | PASS | SKILL.md Phase 4 §5 | — |
| C57 | Show validation before done | PASS | SKILL.md Phase 4 §6 | — |
| C58 | Fidelity scorecard 30/20/20/15/15 dual-agent | PASS | `references/fidelity-scorecard.md` five dims + procedure | — |
| C59 | Phase 5 dual-agent refine | PASS | SKILL.md Phase 5 | — |
| C60 | Agent A: 8-dimension structure + 3 dry-runs | PASS | SKILL.md Phase 5 A: eight named dims + Dry-run 3 | Stage 6 |
| C61 | Agent B: trigger + role-play operability | PASS | SKILL.md Phase 5 B: triggers; routing / frequency / failure prevention; missing facts; 2–3 patches (expanded 2026-09-04) | — |
| C62 | Apply non-conflicting edits + show summary | PASS | SKILL.md Phase 5 closing lines | — |

### Update / taste / anti / special / meta

| ID | Item | Status | Evidence / gap | Closes in |
|---|---|---|---|---|
| C63 | Update: agents 2+5+6 incremental | PASS | SKILL.md Updates | — |
| C64 | Taste: long-form > quotes; controversy > consensus; change > fixed | PASS | SKILL.md Taste rules three tie-breakers | Stage 6 |
| C65 | Anti-pattern 10-row table | PASS | SKILL.md Anti-patterns rows 1–10 (= Nuwa) + 11–17 Engram extras | Stage 6 |
| C66 | Living vs historical handling | PASS | special-scenarios.md Living vs historical; SKILL Special scenarios pointer | Stage 5 |
| C67 | Topic-skill phase-variant table | PASS | special-scenarios.md Topic skill table 0A–4 | Stage 5 |
| C68 | Distill-yourself procedure | PASS | special-scenarios.md Distill yourself; SKILL Phase 0 pointer | Stage 5 |
| C69 | China vs West source playbook | PASS | special-scenarios.md dual playbook + bilingual mix; 0.5 checklist | Stage 5 |
| C70 | Obscure person (<10 sources) procedure | PASS | special-scenarios.md four-step; 0.5 checklist fires it | Stage 5 |
| C71 | Silent version self-check | PASS | `references/version-self-check.md`; SKILL section + required-reading "before run" (added 2026-09-04); I4 non-git skip | Stage 6 |
| C72 | Output path = Nuwa `.claude/...` | INTENTIONAL | I2 | — |

Note: IDs C01–C72 include INTENTIONAL rows. **Core denominator = 69** = all non-INTENTIONAL items excluding Additive.

### Additive (not in parity %)

| ID | Item | Status |
|---|---|---|
| A1 | Memory store + four-test admission + intimate ledger + CTT vetoes | PASS (beyond Nuwa) |
| A2 | Stage 8 stakes (skin / why / productive urgency) | PASS (beyond Nuwa) |
| A3 | Peer curiosity / PEERS.md | PASS (beyond Nuwa) |
| A4 | Optional immersion track | PASS (beyond Nuwa) |

---

## FAIL queue — remaining

None (non-intentional). I1–I4 remain documented cuts.

## PARTIAL queue — remaining

None (C61, C71 closed 2026-09-04).

---

## Script / template notes (not checklist IDs)

| Area | Finding |
|---|---|
| `download_subtitles.sh` | Engram: en → zh → auto. Nuwa: zh → en → auto. **Intentional** English-runtime order; same job. |
| `merge_research.py` | English markers + optional 07-intimate. Behavioral parity for 01–06. |
| `quality_check.py` | English section regexes + additive memory check. Six Nuwa checks preserved. |
| `srt_to_transcript.py` | Functional parity (strip / dedupe / paragraph). |
| skill-template spine | Engram = Nuwa sections + Agentic Protocol in-template + additive (peers, stakes, evidence classes). Structural parity held. |
| Scripts location | Nuwa copies scripts into each skill dir; Engram keeps them in the factory pack (documented in SKILL Tools 2026-09-04). |

## Candidate C73+ (reviewed; not added)

| Candidate | Verdict |
|---|---|
| Inline Phase 4.1/4.2/4.3 named tests | Covered by fidelity-scorecard procedure (3 known + 1 edge + 1 style). No new ID. |
| Copy scripts into every output engram | Packaging difference, not distill procedure. Documented intentional. |
| Community index ≥B / WeChat / promo | Out of process parity (marketing). |
| 0B example dialogue script | Engram has paper calibration in vague-need.md; operable. |

---

## How to re-score

1. Read this file and `../SKILL.md` plus `references/*` and `scripts/*`.  
2. For each ID, set Status using the vocabulary above.  
3. Recompute:  
   - `core = items where Status ∉ {INTENTIONAL}` and ID not Additive  
   - `weighted = (PASS + 0.5×PARTIAL) / |core|`  
   - `strict = PASS / |core|`  
4. Append Changelog line: date, weighted%, strict%, FAIL count, stage that just closed.  
5. Gate for Stage N passes only if that stage’s “Closes in” IDs are all PASS (or INTENTIONAL).

Do not delete FAIL rows when fixed — change Status to PASS and note the stage in Changelog.

---

## Changelog

| Date | Event | Weighted | Strict | FAIL |
|---|---|---|---|---|
| 2026-09-03 | Stage 0 freeze (post line-break correction) | ~72% | ~64% | 14 |
| 2026-09-03 | Stage 1 G1 — corpus modes, local-first, file map, podcast hint, tier pre-confirm | ~80% | ~72% | 9 |
| 2026-09-03 | Stage 2 G2 — 1.5/2.5 pause unless run-through waiver | ~81% | ~75% | 9 |
| 2026-09-03 | Stage 3 G3 — Phase 0B table, cards, person vs topic | ~84% | ~80% | 8 |
| 2026-09-03 | Stage 4 G4 — frontmatter cap, Munger/Feynman/Taleb/MrBeast tracks | ~87% | ~83% | 6 |
| 2026-09-03 | Stage 5 G5 — special scenarios, China allowlist, named skills | ~96% | ~94% | 2 |
| 2026-09-03 | Stage 6 G6 — taste, anti-pattern table, Agent A 8 dims, version check | ~100% | ~100% | 0 |
| 2026-09-04 | **engram-v2 due diligence re-score** (lean side-files verified; C61/C71 PARTIAL→PASS; Stage 6 claim was for pre-v2 lean — re-verified against v2) | **100%** | **100%** | **0** |
| 2026-09-04 | Adversarial hostile audit → 4 PARTIAL (C09/C28/C57/C62); P0 fixes applied → **100%/100% FAIL0** | 100% | 100% | 0 |
| 2026-09-04 | Publish prep 2.5.0 — audit receipts → `docs/audit/`; LICENSE/README/VERSION | 100% | 100% | 0 |
