# Parity adversarial audit — Engram v2 vs huashu-nuwa

**Auditor ID:** HOSTILE-2026-09-04 · **Date:** 2026-09-04 (America/Chicago)
**Mode:** audit-only. No files edited except this new report. Nuwa, frozen v1 untouched.
**Ground truth:** `~/.tink/skills/huashu-nuwa/` (`SKILL.md` 682 lines + 3 references + 4 scripts)
**Factory under test:** `~/.tink/skills/engram-v2/` (`SKILL.md` 536 lines + references + scripts)
**Prior claim (contested, read last):** `docs/audit/PARITY-DUE-DILIGENCE-2026-09-04.md` (100%/100%/0) + `references/parity-checklist.md`
**Method:** Nuwa read first, own process map written before opening Engram receipts; checklist Status treated as defendant exhibit. Empirical probes in `/tmp/parity-probe` (Chinese-marker fixture) and cross-run of both `quality_check.py` on Nuwa's own `examples/feynman-perspective/SKILL.md`.

## 1. Executive verdict

**Engram v2 is at 97.1% weighted / 94.2% strict with zero FAILs but four real PARTIALs — it is not 100%, and "ship-ready at 100%" must be refused until four one-line fixes land.**

## 2. Scores

| Metric | Prior claimed | This audit |
|---|---|---|
| Core items (excl. INTENTIONAL + Additive) | 69 | 69 |
| PASS | 69 | **65** |
| PARTIAL | 0 | **4 (C09, C28, C57, C62)** |
| FAIL | 0 | **0** |
| Weighted `(PASS + 0.5×PARTIAL)/69` | 100% | **67/69 = 97.1%** |
| Strict `PASS/69` | 100% | **65/69 = 94.2%** |

**Pre-bias correction:** I entered assuming the checklist was green and my first full pass agreed at 69/69. The nitpick probes broke four of them: the cost-magnitude refusal (C09), the Chinese-marker blindness in `merge_research.py` (C28, empirical), and the two missing confirmation verbs at Phase 4/5 closure (C57, C62). None survived re-attack. The prior 100% is therefore **falsified as stated** — close, but not 100%.

**Ship-ready gate** (weighted ≥95% **and** FAIL=0 **and** no PARTIAL on pause gates, swarm, triple-verify, template fill, dual-agent fidelity, Phase 5 A/B): weighted passes, FAIL=0 passes, but C57 (validation closure) and C62 (refine closure) are PARTIAL on dual-agent fidelity / Phase 5 procedure. **Ship-ready language refused.** The fixes are trivial (see §11); re-score after.

## 3. Process map (from Nuwa — reconstructed before opening Engram)

Nuwa is a nine-gate distill pipeline with two entries:

- **0 (split):** named person → 0A; vague need → 0B.
- **0A (clarify, non-blocking):** identity, focus, use, new-vs-update (scan `.claude/skills/`), local-corpus ask, **tier + cost-magnitude disclosure** (fast 3-dim×5-src / standard 6-dim default / deep + full ingest; top-model full run costs tens of dollars, real case). Defaults carry; `just do it` → full portrait + advisor + web + standard.
- **0B (diagnose):** ≤2 follow-up rounds → 10-row demand table → person-vs-topic call → scan local skills first → ≤3 candidate cards (lens / why-fit / limit, existing first, differentiated) → pick → 0A → 0.5.
- **0.5 (scaffold first):** create `.claude/skills/<name>-perspective/` with `SKILL.md`, `scripts/`, `references/research/01–06.md`, `sources/{books,transcripts,articles}`; self-containment rule (never external `07-调研与分析`); China-strategy switch; update-mode read; corpus copy + mode mark.
- **1 (swarm):** pure-web (default) / local-first (classify → gap-check → search gaps only → label origin) / pure-local; file-type→ledger table; six agents (writings, conversations, expression, external, decisions, timeline+last-12mo) with per-agent hunt/extract, hard rules (file, credibility, said/about/inferred, keep contradictions), prompt template with blacklist; tools (Z-Lib/LibGen books, subtitle dl+clean scripts, podcast transcripts, merge script, quality script); named helper-skill scan; source priority; blacklist (Zhihu/WeChat/Baidu) + Chinese outlet allowlist; 7-row failure/degrade table; "labeled 60 over fake 90".
- **1.5 (gate):** `merge_research.py` table → **pause for user OK**.
- **2 (synthesis):** must read extraction-framework (triple verify: cross-domain ≥2 / generative / exclusive; 15–30 candidates → 3–7 models by exclusivity; 5–10 heuristics; 20-paragraph DNA fingerprint + style poles + taboos; values/anti-patterns/tensions; lineage; honest boundary).
- **2.5 (gate):** summary → **pause for user OK**.
- **3 (build):** read skill-template; fill table incl. ~300/~1024 frontmatter cap, role-play defaults, **Agentic Protocol** (classify / model-derived Step-2 tracks with Munger/Feynman/Taleb/MrBeast calibration / answer), identity, models, heuristics, DNA, timeline, values, lineage, boundary, sources, 花叔 attribution; quality self-check; write file.
- **4 (validate):** subagent trials — 3 known-stance + 1 edge (hedged-inference expectation) + 1 voice (100 words); 6-row pass table (3–7 models, limits, DNA identifiability, ≥3 boundary, ≥2 tensions, >50% primary); ≤2 iterations; **confirmation checkpoint**.
- **5 (refine):** dual agents — A: 8-dim structure + 3 dry-runs → weakest 2 with after-text; B: triggers + role-play operability (routing, frequency, failure prevention) + missing facts → 2–3 after-text patches; apply non-conflicting; **confirmation checkpoint**; "activate-and-run" standard.
- **Transverse:** update path (agents 2+5+6 incremental); taste tie-breakers (long>quotes, controversy>consensus, change>fixed); 10-row anti-pattern table; specials (living/historical, topic variants, China/West, obscure <10, self-distill); silent 30-day version self-check with non-git skip.

## 4. Prosecution table (C01–C72; receipts = file:line)

### Phase 0 / 0A

| ID | Item | Status | Nuwa receipt | Engram receipt | Nitpick |
|---|---|---|---|---|---|
| C01 | Entry split named vs vague | PASS | SKILL.md:32-40 table | SKILL.md:68-70 + 126-130 | In-flow pointer to vague-need.md at decision point. |
| C02 | Clarify identity | PASS | SKILL.md:47 | SKILL.md:72 §1 | Same procedure. |
| C03 | Full vs focused | PASS | SKILL.md:48 | SKILL.md:73 §2 | Same. |
| C04 | Use case | PASS | SKILL.md:49 | SKILL.md:74-77 §3 (mind default; immersion opt-in is additive, not a use-case drop) | No procedure lost. |
| C05 | New vs update + scan | PASS | SKILL.md:50 scan `.claude/skills/` | SKILL.md:78-79 scan `engrams/` + `personas-skillset/` | Path change is I2; procedure (scan-then-decide) identical. |
| C06 | Local-corpus ask first | PASS | SKILL.md:51 | SKILL.md:80-93 §5 Resource drop | Engram more operable (file map now, not later). |
| C07 | Tier table fast/std/deep + caps | PASS | SKILL.md:54-58 | SKILL.md:95-99 (fast cap ~5; standard default; deep full ingest) | Source caps match. **But** cost column dropped → see C09. |
| C08 | Non-blocking defaults | PASS | SKILL.md:60,62 | SKILL.md:59,66 Defaults "Proceed on Phase 0…" | Same polarity. |
| C09 | **Cost magnitude before run** | **PARTIAL** | SKILL.md:52 ("tens of dollars, real case, must state"), :324, anti-7 :619 | SKILL.md:101-105 ("Name the tier; leave cost unmeasured") | **Downgrade.** Nuwa demands a magnitude with a real anchor; Engram explicitly refuses measurement ("long multi-agent job" only) and drops the tier table's cost column. "No invented dollars" is no defense — quoting Nuwa's disclosed anchor invents nothing. Thin where Nuwa is specific. |

### Phase 0B

| ID | Item | Status | Nuwa receipt | Engram receipt | Nitpick |
|---|---|---|---|---|---|
| C10 | 10-row demand table | PASS | SKILL.md:77-88 | vague-need.md:10-21 (10 rows, same semantics) | Renames OK. |
| C11 | Max 2 follow-ups | PASS | SKILL.md:90-93,109 | vague-need.md:5-6,23-24 ("at most two; one round then recommend") | Engram stricter (1 round norm, 2 cap). Ceiling preserved; not a parity loss. |
| C12 | Candidate cards ≤3 (lens/fit/limit) | PASS | SKILL.md:126-141 | vague-need.md:45-56 (Lens/Why/Limit, max 3, differ, existing-first) | Row-equivalent. |
| C13 | Existing skills first | PASS | SKILL.md:120-121,137 | vague-need.md:37-40 Source A first | Same, paths per I2. |
| C14 | Person vs topic at intake | PASS | SKILL.md:115-118 | vague-need.md:26-33 → special-scenarios.md:31-40 | Bound at intake, not post-hoc. |

### Phase 0.5

| ID | Item | Status | Nuwa receipt | Engram receipt | Nitpick |
|---|---|---|---|---|---|
| C15 | Directory before research | PASS | SKILL.md:149-151 "immediately, before research" | SKILL.md:132-137 + schema.md | Same gate position. |
| C16 | Tree 01–06 + sources/3 | PASS | SKILL.md:153-169 | schema.md:6-28 (same filenames; +07 only-if-intimate additive) | Filenames interchangeable. |
| C17 | Self-contained | PASS | SKILL.md:179 (never external dir) | SKILL.md:137 | Engram omits naming the historical `07-调研与分析` path — immaterial, rule preserved. |
| C18 | China switch at 0.5 | PASS | SKILL.md:171-173 checklist | SKILL.md:154-157 checklist → special-scenarios.md:44-81 | Bound at 0.5 checklist, fires before agents. |
| C19 | Corpus copy + mode mark | PASS | SKILL.md:175 | SKILL.md:144-147 (`local-first/pure-local/pure-web` in run notes) | Same, plus dry-run calibration. |

### Phase 1

| ID | Item | Status | Nuwa receipt | Engram receipt | Nitpick |
|---|---|---|---|---|---|
| C20 | Three modes | PASS | SKILL.md:189-193 | SKILL.md:164-170 table | Same triggers/strategies; I1 carved out of pure-web explicitly. |
| C21 | Local-first 4-step | PASS | SKILL.md:195-200 | SKILL.md:172-177 (classify/gap/search-gaps/label, numbered) | Verbatim procedure. |
| C22 | File-type→ledger table | PASS | SKILL.md:202-212 | SKILL.md:179-191 (+texture/raw-AV rows additive) | All 7 Nuwa rows present with same ledger mapping. |
| C23 | Six agents, filenames | PASS | SKILL.md:224-231 | SKILL.md:201-208 same six + filenames | Match. Optional-7 additive only. |
| C24 | Hunt + extract per agent | PASS | SKILL.md:224-231 | SKILL.md:201-208 Hunt/Extract columns | Same content. |
| C25 | Hard rules | PASS | SKILL.md:233-237 (file, credibility, said/about/inferred, contradictions) | SKILL.md:214-219 (file, locator+confidence, Subject/Witness/Inference, tensions) | "Credibility" compressed into confidence+priority; operable, no step lost. Weakest PASS — see §7. |
| C26 | Agent prompt template | PASS | SKILL.md:241-262 (task, directions, write-to, URL+credibility, 1st/2nd-hand, contradictions, blacklist) | SKILL.md:221-235 (task, Hunt, write-to, URL-or-path, primary/secondary, contradictions, blacklist) | Drops "credibility per item" line and tool-call lines, but Tools § covers tools at operator level exactly as Nuwa does (Nuwa's template also omits subtitle/merge invocations). Survives — see §7. |
| C27 | Subtitle scripts | PASS | SKILL.md:266-272; scripts/download_subtitles.sh, srt_to_transcript.py | SKILL.md:250-251; scripts/ both present, invoked with pack path | Same job; en-first order intentional (English runtime); Nuwa's dead `-newer marker` branch actually fixed. Subagent binding note in §7, no downgrade. |
| C28 | **merge + quality scripts** | **PARTIAL** | scripts/merge_research.py (CN markers, box table); quality_check.py (6 checks, exit 1 unless 6/6) | scripts/ both present; SKILL.md:254-255,290,414 | **Downgrade on merge leg (empirical §5):** Chinese fixture → Nuwa counts 30/60 primary markers + 5 contradictions; Engram reports "unlabeled" + 0 contradictions. Engram regexes dropped all CN alternations (`一手/本人/原文/原始/二手/转述/矛盾/争议…`). Material because Engram explicitly supports China-subject distills whose ledgers contain exactly these markers. Quality leg passes (English-runtime intentional; memory 7th check additive, vacuous-pass when no MEMORY.md). |
| C29 | Helper-skill scan | PASS | SKILL.md:284-294 (5 names by job, tell subagents) | info-gathering-skills.md (5 Nuwa names, job-matched) + SKILL.md:257-260 | Names what/where; "missing ≠ skip ledger" preserves Nuwa intent. Honestly notes none installed locally. |
| C30 | Podcast hint | PASS | SKILL.md:274 | SKILL.md:252-253 (podcastnotes.org + show site) | More specific. |
| C31 | Source priority | PASS | SKILL.md:296-306 (7-row table with what-each-reveals + weights) | SKILL.md:262-266 one-line ordering | Compressed (drops "reveals" column) but ordering identical and local-primary-top preserved. Weak PASS — see §7. |
| C32 | Blacklist | PASS | SKILL.md:308-312 | SKILL.md:268-272 one-liner + special-scenarios.md:48-53 | One-liner omits 知道, side file has Baike/知道 + quote farms. Bound pointer present. |
| C33 | Chinese allowlist | PASS | SKILL.md:314 (8 outlets + B站/小宇宙/喜马拉雅) | special-scenarios.md:55-63 (same 8 + same platforms + reupload exclusion) | Complete; reupload-account rule is faithful hardening. |
| C34 | Z-Lib/LibGen books | INTENTIONAL | SKILL.md:265 (I1) | SKILL.md:56-57,168,245-249 refuse; anti-11 :479 | Cut present, not reintroduced (grep: only refusal mentions). |
| C35 | Failure table | PASS | SKILL.md:316-328 (7 rows) | SKILL.md:274-284 (7 rows, same triggers/fixes/fallbacks incl. 500k-token + 3-session splits) | Row-equivalent. |
| C36 | Labeled-60 rule | PASS | SKILL.md:330 | SKILL.md:286 | Verbatim. |

### Phase 1.5 / 2 / 2.5

| ID | Item | Status | Nuwa receipt | Engram receipt | Nitpick |
|---|---|---|---|---|---|
| C37 | 1.5 table via merge script | PASS | SKILL.md:332-355 | SKILL.md:288-299 + scripts/merge_research.py | Table renders; URL counts + findings + thin-ledger warnings verified live. CN-marker blindness noted under C28, not double-counted. |
| C38 | 1.5 default pause | PASS | SKILL.md:334,352 | SKILL.md:62-66 Defaults + 293-296 "Stop. Ask…" + waiver | Pause-by-default polarity kept; waiver needs explicit run-through phrase. Vague "just do X" correctly does NOT waive (waiver recorded only for stated phrases). |
| C39 | Must read extraction-fw | PASS | SKILL.md:361 | SKILL.md:303 + required-reading :30 | "All the way through… do not improvise" — strong binding. |
| C40 | 15–30 → triple → 3–7 | PASS | SKILL.md:363-375 + extraction-framework.md:5-33 | SKILL.md:306-309 + extraction-framework.md:7-37 (same 3 tests, same 3/3→model / 1–2→heuristic / 0→drop, same Naval/Munger examples) | Faithful port incl. exclusivity ranking. |
| C41 | Heuristics 5–10 + cases | PASS | SKILL.md:376-378 | SKILL.md:310 | Same "If X then Y + case". |
| C42 | DNA fingerprint/poles | PASS | SKILL.md:380-390 + extraction-framework.md:37-70 (6 metrics, 7 poles, taboos) | SKILL.md:311-312 → framework :39-71 (same 6 metrics, same 7 poles, same taboo/tic rule) | Row-equivalent incl. 20-paragraph sample. |
| C43 | Values/anti/tensions | PASS | SKILL.md:391-395 | SKILL.md:313 | Same, ≥2 tensions. |
| C44 | Lineage | PASS | SKILL.md:397-399 | SKILL.md:314 | Same. |
| C45 | Honest boundary | PASS | SKILL.md:401-408 (4 required limits) | SKILL.md:315 | Same 4 (unpredictability, no-substitute-creativity, public-vs-real gap, cutoff). |
| C46 | 2.5 summary checkpoint | PASS | SKILL.md:411-422 | SKILL.md:322-325 (models, heuristic count, 3 DNA, tensions, boundary, traces) | Same fields. |
| C47 | 2.5 default pause | PASS | SKILL.md:424 | SKILL.md:327-330 "Stop… unless waiver" | Same polarity as C38. |

### Phase 3

| ID | Item | Status | Nuwa receipt | Engram receipt | Nitpick |
|---|---|---|---|---|---|
| C48 | Fill every template section | PASS | SKILL.md:435-439 | SKILL.md:334-335 "fill every section" + fill table :339-356 + template spine (§5: all Nuwa sections present) | Spine verified section-by-section. |
| C49 | Frontmatter ~300/1024 | PASS | SKILL.md:443 | SKILL.md:343 + skill-template.md:9-11 | Same numbers + same anti-stuffing rationale. |
| C50 | Protocol classify/research/answer | PASS | SKILL.md:457-497 (3 steps, derived Step-2, output format, judgment principle :482) | skill-template.md:81-134 (3 steps, derived tracks, private-digest format) + SKILL.md:397-410 | One dropped sentence: Nuwa's "if missing info would degrade quality, research; rather search once more than fabricate" (:482) has no verbatim counterpart. Covered in spirit by "Use real tools. Do not skip" + Step-1 routing, but the tie-breaker sentence is gone. Weak PASS — see §7. |
| C51 | Step-2 calibration examples | PASS | SKILL.md:499-508 (Munger/Feynman/Taleb/MrBeast table) | agentic-protocol.md:21-26 (same 4 rows, same derivations) + SKILL.md:403-407 pointer | Same derivations; "do not paste calibration rows" correctly prevents template contamination. |
| C52 | Framework self-check after build | PASS | SKILL.md:515-516 | SKILL.md:362-364 + extraction-framework.md:104-129 | Same checklist position (post-build). |
| C53 | 花叔 attribution block | INTENTIONAL | SKILL.md:455 (I3) | SKILL.md:355 fork line; template :238-239 | Cut present, honest fork credit. |

### Phase 4 / 5

| ID | Item | Status | Nuwa receipt | Engram receipt | Nitpick |
|---|---|---|---|---|---|
| C54 | Independent answerer, no web | PASS | SKILL.md:525-529 | SKILL.md:414-417 + fidelity-scorecard.md:32-41 (answerer: engram dir only, no web; judge separate) | Dual-agent iron rule quoted with SkillLens 46.4% rationale. |
| C55 | Six-row pass table | PASS | SKILL.md:543-552 | SKILL.md:418-427 (same 6 rows, same bars: 3–7, limits, 100-word DNA, ≥3 boundary, ≥2 tensions, >50%) | Identical gates. |
| C56 | ≤2 iterations | PASS | SKILL.md:555 | SKILL.md:431 | Same cap + ship-labeled fallback. |
| C57 | **Show validation before done** | **PARTIAL** | SKILL.md:557 "展示验证结果给用户确认后才算完成" (confirmation checkpoint) | SKILL.md:432 "Show the scorecard before calling it done" | **Downgrade.** Showing ≠ confirming. Nuwa makes user confirmation constitutive of done; Engram requires only display. Under N3 (optional where Nuwa mandates), PARTIAL. One-verb fix. |
| C58 | Scorecard 30/20/20/15/15 dual-agent | PASS | fidelity-scorecard.md:7-16,26-50 | fidelity-scorecard.md:13-21 + procedure :32-41 + anti-cheat :68-73 (same weights, same 10/6/0, same 3+1+1 items, same FIDELITY.md shape, same >10-gap double-judge) | Weights/rules identical; vetoes additive, non-scoring. N6 held. |
| C59 | Dual-agent refine | PASS | SKILL.md:561-563 | SKILL.md:437-439 | Same trigger (after passing scorecard), parallel. |
| C60 | Agent A 8-dim + 3 dry-runs | PASS | SKILL.md:567-570 ("8维度…工作流清晰度、边界条件、检查点设计、指令具体性等" + 3 prompts + weakest-2 with after-text) | SKILL.md:441-444 (8 named dims + 3 dry-runs + weakest-2 rewrite) | Nuwa names 4 + 等; Engram's extra 4 (first action, failure/degrade, template completeness, loader cost) are unverifiable expansion — but operable, direction-correct, and the scored behaviors (3 runs, weakest-2, after-text) match. PASS with noted caveat, see §7. |
| C61 | Agent B triggers + role-play | PASS | SKILL.md:572-576 (triggers, routing/frequency/failure-prevention, missing facts, 2–3 after-text patches) | SKILL.md:445-448 (same 4 elements) | Post-fix text verified present. |
| C62 | **Apply + show summary** | **PARTIAL** | SKILL.md:578 ("应用不冲突的改进，展示变更摘要请用户确认") + :580 run-standard | SKILL.md:450-451 ("Apply non-conflicting edits. Show a diff summary" + run-standard) | **Downgrade.** Same missing confirmation verb as C57. The run-standard line is kept; the 请用户确认 gate is not. |

### Update / taste / anti / special / meta

| ID | Item | Status | Nuwa receipt | Engram receipt | Nitpick |
|---|---|---|---|---|---|
| C63 | Update 2+5+6 incremental | PASS | SKILL.md:586-595 (cutoff date, 2+5+6, 3 compare cases, latest+date, no rewrite) | SKILL.md:453-456 (cutoff, 2+5+6 [+7 additive], contradict-only patching, surgical) | All 5 Nuwa steps present. |
| C64 | Taste tie-breakers | PASS | SKILL.md:601-607 | SKILL.md:458-461 (same 3: long>quotes, controversy>consensus, change>fixed) | Verbatim. |
| C65 | 10-row anti-pattern table | PASS | SKILL.md:609-622 (10 rows) | SKILL.md:463-478 rows 1–10 same + 11–17 Engram extras | Row-by-row match incl. #7 cost-gate (which Engram's own row 7 restates while C09 weakens — internal tension noted, not double-counted). |
| C66 | Living vs historical | PASS | SKILL.md:628-630 | special-scenarios.md:6-24 (living 4 steps incl. 12-mo + cutoff; historical 4 steps incl. 2-family cross-validation + periodization) | Engram strictly more operable. |
| C67 | Topic-skill variants | PASS | SKILL.md:632-646 (8-row phase table) | special-scenarios.md:31-40 (same 8 phases: boundary, dir, 3–5 people/1–2 agents each, consensus+splits, neutral voice, school splits, template swap, canonical-case validation) | Full row parity. |
| C68 | Distill-yourself | PASS | SKILL.md:658-664 (4 steps) | special-scenarios.md:98-114 (5 steps: halt-till-corpus, 4 corpus classes, sources-only agents, self-serving warning in boundary, 07+veto) | All 4 Nuwa steps + hardening. |
| C69 | China vs West playbook | PASS | SKILL.md:647-649 | special-scenarios.md:44-81 (blacklist, 8-outlet allowlist, CN path, Western path, bilingual-mix rule) | Complete; bilingual rule additive-correct. |
| C70 | Obscure <10 procedure | PASS | SKILL.md:651-656 (warn at 0.5, 2–3 models, expand boundary, supply primaries) | special-scenarios.md:83-96 (same 4, fired by 0.5 checklist SKILL.md:158-160) | Same trigger point and caps. |
| C71 | Silent version self-check | PASS | SKILL.md:673-684 (30-day file, non-git skip, rev-parse vs ls-remote, behind→finish-task-then-one-line) | version-self-check.md:1-16 (same 4 steps, I4 named) + SKILL.md:36 required-reading "before run" + :534-536 section | All behaviors ported; discoverability via table row + closing section. Weakest-link candidate (footer placement) but the required-reading table is phase-bound ("before run"), satisfying N10's letter. See §7. |
| C72 | Output path `.claude/…` | INTENTIONAL | SKILL.md:154,519 (I2) | SKILL.md:52,140,365 `engrams/<slug>/`; anti-12 :480 | I2 throughout; no `.claude/skills` write path exists in Engram (grep confirms). |

No C73+ rows added — see §8 for the hunt that justifies "none".

## 5. Deep-diff findings

**D1 Anti-patterns (N1):** 10/10 rows match in order and semantics (fake quotes/locator-or-drop; exclusivity gate; Agent-4 fan-filter; labeled-60; Zhihu/WeChat/Baidu ban; small-window split; tier-before-swarm; private-person consent; anti-drift retention; defaults-not-blocks). Engram rows 11–17 are additive vetoes (I1/I2 piracy/path, read-only Nuwa, informed-CTT-only, false-memory, costume, tension-flattening) — unscored, no interference.

**D2 Phase 0B (N1/N2):** 10 demand dimensions match; max-2 cap kept (Engram norm is stricter: 1 round, cap 2); card fields match (lens/why/limit + installed-vs-new marker); max-3 + existing-first + differentiation match. The worked dialogue (Nuwa :95-109) is replaced by a different paper calibration (vague-need.md:64-68); rhythm rule ("one round then recommend") is preserved as procedure, so no downgrade — but the calibration example teaches a different domain than Nuwa's decision-speed case.

**D3 Tier table (N1/N2):** scale/caps match (fast 3-dim×~5, standard 6-dim default, deep + full ingest). **Missing cell:** Nuwa's 成本量级 column (1/3×, medium, highest) has no counterpart — feeds C09 PARTIAL. Cost disclosure is prose-only ("long multi-agent job") with no anchor.

**D4 Failure table (N1):** 7/7 rows match trigger→fix→fallback, including the 500k-token overflow splits (0–1/1.5–2.5/3–5 sessions) and the cost-stop rule (ledgers-are-deliverable). Strongest PASS in the pack.

**D5 Phase 5 Agent A (N1):** 3 dry-runs + weakest-2-with-after-text match. The "8 dims" are half-Nuwa (4 named + 等): Engram's 4 invented dims (first action on activation, failure/degrade paths, template completeness, loader cost) are plausible and direction-aligned with Nuwa's run-standard, but receipt-free. Held as PASS because every *scored behavior* matches; the invented dims only add review surface, they don't change procedure.

**D6 Phase 5 Agent B:** post-fix text names all four Nuwa elements (trigger coverage; routing/frequency/failure-prevention; missing facts; 2–3 after-text patches). PASS — this fix is real, verified in current SKILL.md:445-448.

**D7 Agentic Protocol (N7):** 3-step shape, model-derived Step-2, private-digest output format, Munger/Feynman/Taleb/MrBeast calibration derivations all match. One dropped sentence: Nuwa's tie-breaker "if missing info would degrade quality, research — rather search once more than fabricate" (:482). Engram's "Use real tools. Do not skip" + Step-1 router covers the common case but not the marginal call. Weak PASS, fix-list P2.

**D8 Scripts (N4):** `srt_to_transcript.py` — functional parity (strip/dedupe/paragraph logic identical; only CLI strings anglicized). `download_subtitles.sh` — same 3-attempt job; en-first order intentional; Engram *fixes* Nuwa's dead first branch (`-newer /tmp/.ytdlp_marker` could never fire) to `-mmin -1`. `merge_research.py` — **PARTIAL leg** (see C28; empirical probe below). `quality_check.py` — same CLI/exit contract (nonzero unless all pass); English-only section regexes are consistent with the English-runtime fork, but cross-running Engram's checker on Nuwa's own `examples/feynman-perspective/SKILL.md` yields 3/7 with three pure language-detection FAILs (no mental-model/DNA/boundary sections detected) where Nuwa's own checker scores 4/6 on real content gates. No live failure on Engram's own English output, but the "six checks preserved" claim needs the bilingual-heading caveat (fix-list P1).

**D9 Template spine (N5):** every Nuwa `skill-template.md` section exists in Engram's (frontmatter, role-play, identity, models, heuristics, DNA, timeline+latest, values/anti-patterns, lineage, honest boundary, sources primary/secondary/key-quotes). Structural note in Engram's favor: Nuwa's own template *file* omits the Agentic Protocol section its SKILL fill-table requires; Engram's template adds the Answer-workflow section, resolving Nuwa's internal inconsistency. Additive sections (peers, stakes, evidence classes, memory retrieval) don't displace any Nuwa section. PASS.

**D10 Scorecard (N6):** 30/20/20/15/15, 10/6/0 known-stance scoring, blind-style, edge-honesty, >50% primary, structural completeness (3–7/≥3/≥2/anti-patterns/anti-drift), 3+1+1 item set, no-web answerer, separate judge, FIDELITY.md shape, >10-gap double-judge — all identical. Vetoes additive, non-scoring. Clean PASS.

**D11 China/blacklist (N9):** blacklist operable (Zhihu/WeChat/Baike+Zhidao/quote-farms, "no ledger, no dimension"); allowlist complete (same 8 named newsrooms + original-Bilibili/Xiaoyuzhou/Ximalaya + first-party Weibo/books, reupload exclusion). PASS — which is exactly why the C28 merge-marker gap stings: the factory *recruits* Chinese corpora its own review script cannot count.

**D12 Pause gates (N3):** 1.5/2.5 pause-by-default with explicit-phrase waiver — polarity preserved, waiver correctly narrow ("run through / don't stop at checkpoints / skip the gates"; vague assent still pauses). **But** Phase 4 and Phase 5 closures dropped the confirmation verb (C57/C62 PARTIAL). The factory pauses where Nuwa pauses mid-pipe and merely *displays* where Nuwa demands confirmation at the end.

**D13 Update path:** all 5 Nuwa steps (cutoff read, 2+5+6 only, reinforce/supplement/contradict triage, latest+date patch, no rewrite) present; +7-intimate conditional is additive-correct.

**D14 Version self-check:** silent cadence, 30-day file, non-git skip (I4 named), rev-parse-vs-ls-remote, finish-task-first-then-one-line — all ported; required-reading "before run" row gives phase binding. PASS per N10's letter, though a footer section is the weakest pointer in the pack (see §7).

## 6. Cold-agent simulations (Engram files only; N12)

**S1 Named person, standard, pure-web (0A→0.5→1→1.5⏸→2→2.5⏸→3→4→5).** Opens SKILL.md: required-reading table routes 0.5→schema, 1→agent table, 1.5→merge script, 2→framework, 3→template+protocol, 4→quality+scorecard. Tier named (standard default after "just do it"), mode pure-web marked, six ledgers written, merge table shown, two pauses hit. **Friction:** at tier-confirm the agent can name no cost anchor (C09) — it says "long multi-agent job" where Nuwa would cite the tens-of-dollars anchor; at Phase 4/5 closure it shows-but-does-not-confirm (C57/C62). Path completes, gates softer than Nuwa at three points.

**S2 Vague need → 0B → candidate → distill.** "I keep picking wrong products" → vague-need.md Step 1 (Startup & business row), one split question, ≤3 cards with limits, existing-scan first, pick → 0A → 0.5. Completes operably without Nuwa knowledge. The paper calibration covers exactly this case. PASS path.

**S3 Local PDFs/transcripts dropped → local-first/pure-local.** Phase 0 §5 + file-type table classifies (PDF→01+03, SRT→02+03 after clean script), gap-check lists 04/05/06 thin, web fills gaps only, origins labeled. "Only use what I gave you" → pure-local, thin ledgers labeled not padded. Matches Nuwa's 4-step + labeling. PASS path.

**S4 China-subject distill.** 0.5 checklist fires China playbook; agents bound to allowlist; blacklist excludes Zhihu/WeChat/Baidu slices. Ledgers fill with Chinese markers — then **`merge_research.py` reports "primary markers: unlabeled" and 0 contradictions on content Nuwa's script scores 30/60 + 5** (probe §5/C28). The 1.5 gate still renders counts and findings, but the primary-share signal the gate exists to review is blind. **Governing ID C28 PARTIAL — the one simulation that exposes a live behavioral gap.**

**S5 Obscure person (<10 sources).** 0.5 warn + 2–3 model cap + expanded boundary + supply-primaries pivot all fire before Phase 4 (SKILL.md:158-160 + special-scenarios.md:83-96). No fabrication pressure: labeled-60 rule + thin-evidence labels. PASS path.

**S6 (bonus) Self-distill + update-existing.** "Distill me" → halt-till-corpus + self-serving warning (special-scenarios.md:98-114); update → cutoff read + 2+5+6 surgical patch. Both operable without Nuwa. PASS paths.

## 7. Contamination stress — 10 weakest PASSes re-attacked

1. **C09 (cost)** — BROKE → PARTIAL. "Leave cost unmeasured" is a refusal, not a paraphrase, of "must state magnitude with real anchor."
2. **C28 (scripts)** — BROKE on merge leg → PARTIAL (empirical). Quality leg survives (English-runtime + vacuous-pass memory check).
3. **C31 (priority)** — SURVIVES, barely. The 7-row "reveals/weight" table compresses to an ordering, but no decision changes: local-primary-first, secondary-last holds for every ledger call. Not downgraded; one clause ("reveals what") would harden it.
4. **C38/C47 (waiver)** — SURVIVE. Attack: "Nuwa has no waiver, so waiver breaks parity." Rejected: default polarity is pause in both; waiver is an explicit-opt-out additive that cannot trigger accidentally. No behavior lost on the default path.
5. **C50 (protocol tie-breaker)** — SURVIVES as PASS. The dropped marginal-call sentence is real but covered by "Do not skip" + router for all standard cases; fix-list P2, not scored.
6. **C57/C62 (closures)** — BROKE both → PARTIAL. "Show" does not entail "confirm"; Nuwa's checkpoint is constitutive of done.
7. **C60 (Agent A dims)** — SURVIVES. 4 invented dims are receipt-free but behavior-neutral (review surface only; scored outputs match). Not charity: if the extra dims ever drove different rewrites, this reopens.
8. **C71 (version discoverability)** — SURVIVES. Footer placement is the weakest pointer, but the required-reading table binds it "before run" and the section header names the silent cadence. N10's bar ("phase binding with force") is met at minimum strength.
9. **C26 (agent prompt)** — SURVIVES. Attack: "omits credibility + tool lines." Rejected: Nuwa's own template omits tool invocations too (they live at operator level in both); confidence + priority rules cover credibility operably.
10. **C27/C37 (caption + 1.5 table)** — SURVIVE. Pack-local script path is documented at the exact invocation lines; table output verified live (URLs, findings, thin-ledger warnings all render).

**"Would a skeptical staff engineer sign 100%?" No.** They would sign 97% with four annotated gaps and a two-line fix list. The top line stays unfixed at 100%.

## 8. C73+ omissions

Hunt method: `rg` over Nuwa SKILL.md for procedure verbs (必须/绝不/永远/每次/落盘/存文件/之前完成), all CHECKPOINT/表格/脚本 invocations, and every Phase/Step heading; each hit mapped against C01–C72. Result: **no new process-parity IDs.** Near-misses reviewed and rejected: Phase 4.1/4.2/4.3 *names* (Sanity/Edge/Voice) — behaviors encoded in scorecard item set + pass table; per-engram script *copy* — packaging, documented intentional (factory-pack path noted at SKILL.md:239-243); community-index ≥B / WeChat / promo — out of scope per prompt; 0B dialogue script — rhythm rule preserved as procedure; `07-调研与分析` external-dir ban — covered by self-containment rule; gemini-video-for-local-video — covered jointly by file-type table + info-gathering job row (weakest binding in the pack after C71; fix-list P3, unscored).

## 9. Intentional cuts (I1–I4 confirmed, none reintroduced)

- **I1** piracy refusal: SKILL.md:56-57,168,245-249 + anti-11; grep shows only refusal mentions, no fetch path. Present as cut.
- **I2** write path: `~/.tink/skills/engrams/<slug>/` at :52,140,365,528 + anti-12; no `.claude/skills` write path anywhere. Present.
- **I3** fork attribution: SKILL.md:355 + template :238-239 Engram line; no 花叔 block. Present.
- **I4** non-git skip: version-self-check.md:8-10 + required-reading :36. Present.

## 10. Additive Engram (unscored, correctly separated)

Memory/TRACE four-test admission, 07-intimate + informed-CTT/false-memory vetoes, Stage 8 stakes, peer curiosity/PEERS.md, optional immersion. None claimed toward parity; none displaces a Nuwa step (verified: intimate ledger is conditional-only, stakes is post-ship, vetoes are non-scoring). The scorecard veto and memory quality-check are additive-correct.

## 11. Fix list (priority; do NOT apply unless asked — audit-only)

- **P0-1 (C57):** SKILL.md:432 → "Show the scorecard and ask for confirmation before calling it done." (one verb; restores Nuwa :557 gate).
- **P0-2 (C62):** SKILL.md:450 → "Apply non-conflicting edits. Show a diff summary and ask for confirmation." (restores Nuwa :578 gate).
- **P0-3 (C09):** Phase 0 tier-confirm → add one anchored line: "Full standard distill is a long multi-agent job — Nuwa's disclosed anchor is tens of dollars on a top model (real user case); fast ≈1/3 of standard." Quotes Nuwa's disclosure; invents nothing.
- **P0-4 (C28):** `merge_research.py` `count_sources` + `find_contradictions` → restore bilingual alternations (`一手|本人|原文|原始|直接引用|primary|…`, `矛盾|相反|争议|张力|contradiction|tension|…`). ~2 regex lines; re-run probe to verify 30/60 + 5 on the fixture.
- **P1 (D8 note):** `quality_check.py` heading/section regexes → add CN alternations (心智模型/表达DNA/诚实边界/张力/矛盾) so the checker validates Nuwa-format files too.
- **P2 (D7 note):** Step-1 classify → restore Nuwa's marginal-call tie-breaker ("if missing info would degrade quality, research — rather search once more than fabricate").
- **P3 (§8 note):** file-type "Raw audio/video → transcribe" row → append "(via installed video-transcript skill, e.g. gemini-video job in info-gathering-skills.md; else available tooling)".
- Re-score after P0-1..4: expected **69/69 → 100%/100%/0**, at which point ship-ready language becomes signable.

## 12. Sign-off

**I would not stake my reputation on 100%. I would stake it on 97.1% weighted / 94.2% strict / 0 FAILs with four specified PARTIALs and a four-line fix list.** Prior 100% verdict: contested and reduced. Nuwa and frozen v1: untouched (this report is the only file written).

## 13. Addendum — fixes applied 2026-09-04, re-score

User authorized applying P0-1..P0-4. Changes (only these files touched):

- `SKILL.md:432` → "Show the scorecard **and ask for confirmation** before calling it done." (C57)
- `SKILL.md:450` → "Show a diff summary **and ask for confirmation**." (C62)
- `SKILL.md:101-106` → tier-confirm now states magnitude: tens-of-dollars top-model anchor (quoted, not invented), fast ≈1/3 standard, deep highest. (C09)
- `scripts/merge_research.py:26-27,50` → bilingual marker/contradiction regexes restored. Verified live: Chinese fixture now reports **30/60 + 5 contradictions** (was "unlabeled" + 0), byte-identical signals to Nuwa's script; English fixture reports 30/60 + 5, no regression. (C28)

**Re-score: PASS 69 / PARTIAL 0 / FAIL 0 → weighted 100%, strict 100%.** The §2 gate (weighted ≥95%, FAIL=0, no PARTIAL on critical IDs) now holds. Ship-ready language is signable. P1–P3 (§11) remain open as unscored hardening, not parity blockers.

## 14. Addendum — P1–P3 hardening applied 2026-09-04

User authorized the remaining fix list. Changes:

- **P1** `scripts/quality_check.py` → bilingual section/marker regexes (心智模型/表达DNA/表达风格/诚实边界/来源/张力/矛盾/局限/失效/不适用/盲区/一手/二手/…). Verified live on Nuwa's own `examples/feynman-perspective/SKILL.md`: was 3/7 with three pure language-detection FAILs, now **5/7 with the same two true content FAILs Nuwa's checker reports** (boundary 0 items, tensions 1<2); only delta vs Nuwa's 4/6 is the additive vacuous-pass memory check. Behavioral parity on the script contract.
- **P2** `references/skill-template.md` Step 1 → restored marginal-call tie-breaker ("if the answer would be materially worse without current information, research first; rather search once more than fabricate").
- **P3** `SKILL.md` file-type table → raw-audio/video row now names the video-transcript skill path via `info-gathering-skills.md`.

No score change (P1–P3 were unscored); the D8 caveat and §7 items 5/10 and §8 gemini-video note are closed. Nuwa / frozen v1 still untouched.

