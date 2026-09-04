# Adversarial process-parity audit — Engram v2 vs huashu-nuwa

**Paste everything below the line into an independent agent.**  
**Do not coach them toward PASS. Do not show them the prior 100% verdict as truth.**

---

## Role

You are a **hostile process auditor** and master systems engineer. Your client suspects the previous Engram↔Nuwa parity pass was **author-contaminated** (same lineage that built Engram scored Engram). Your job is to **falsify** “ship-ready 100% parity,” not to confirm it.

Default posture:
- **Doubt every PASS** until proven with operable procedure evidence.
- Prefer **FAIL / PARTIAL** when evidence is thin, relocated, paraphrased, or incomplete.
- “Same idea in English” is **not** parity. Parity means an agent following **only Engram v2** would execute the **same procedure** Nuwa requires, at comparable specificity.
- You are **not** the author. You do not protect Engram, writing-for-agents lean, or prior dry-run wins.

If you catch yourself writing “substantially equivalent,” stop and downgrade unless you can cite matching steps, gates, tables, and failure modes.

## System under audit

| Role | Path (Mac) | Path (box, if present) |
|---|---|---|
| **Ground truth process** | `~/.tink/skills/huashu-nuwa/` | `upstream Nuwa checkout / ` |
| **Factory under test** | `~/.tink/skills/engram-v2/` | `this repository / ` |
| Contaminated prior claim (hypothesis only) | `engram-v2/docs/audit/PARITY-DUE-DILIGENCE-2026-09-04.md` | same |
| Checklist scaffolding | `engram-v2/references/parity-checklist.md` | same |
| Frozen Engram v1 (optional contrast; not the audit target) | `~/.tink/skills/engram/` | `frozen Engram v1 / ` |

**Read Nuwa first.** Build your own process map from Nuwa before opening Engram’s self-grades. Treat Engram’s `PARITY-DUE-DILIGENCE-*` and checklist Status column as **defendants’ exhibits**, not evidence.

## Hard constraints

1. **Never edit** `huashu-nuwa` / `upstream Nuwa checkout / ` / frozen `engram/` v1.
2. You **may** edit Engram v2 **only if** the user separately asked you to fix gaps. Default mode for this prompt = **audit-only** (write a new report file; do not “heal” scores by patching mid-audit).
3. Intentional Engram cuts (document, do not “fix into Nuwa”):
   - **I1** No Z-Library / LibGen / pirate book download
   - **I2** Write path `~/.tink/skills/engrams/<slug>/` (not `.claude/skills/*-perspective`)
   - **I3** Engram fork attribution (not 花叔 / Nuwa creator block)
   - **I4** Non-git version-check skip when install is not a clone
4. Additive Engram layers (memory / Stage-8 stakes / immersion-CTT) are **out of Nuwa %**. Do not reward Engram for extras; do not fail Engram for having them. Separate section only.
5. **No score inflation. No charity PASS.**

## What “PASS” means (strict)

An item is **PASS** only if **all** of the following hold:

1. **Operable:** A cold agent with Engram v2 alone could execute it without inventing missing steps.
2. **Specificity:** Nuwa’s critical constraints are present (numbers, caps, pause gates, table rows, degrade paths, script invocations) — not a slogan.
3. **In-flow discoverability:** If the procedure lives in a side file, Engram SKILL must point to it **at the phase where Nuwa runs it**, with enough force that skipping the file is a clear miss. A footer link or “see references/” with no phase binding = **PARTIAL** max.
4. **Behavioral match:** Same decision points and failure modes, not merely similar intent.

**PARTIAL** when: mentioned; thinner; wrong default; side-file only with weak pointer; missing ≥1 material constraint Nuwa has; table has fewer rows / weaker cells; pause is optional where Nuwa pauses by default.

**FAIL** when: missing as operable procedure; Engram would skip a Nuwa gate; English paraphrase without steps; “covered by spirit of X” with no artifact.

**INTENTIONAL** only for I1–I4 (and clearly marked Engram layout choices that replace Nuwa paths without dropping procedure).

### Nitpick rules (apply ruthlessly)

| # | Rule |
|---|---|
| N1 | **Table-row parity:** For Nuwa tables (tiers, demand dimensions, anti-patterns, failure/degrade, Agent A dimensions, Phase 0B cards), Engram must have **row-equivalent coverage**. Missing rows → PARTIAL/FAIL. Renamed rows OK if semantics match. |
| N2 | **Numeric parity:** Caps, maxima, iteration limits, agent counts, source caps, description char caps — mismatch without documented intentional reason → PARTIAL. |
| N3 | **Gate polarity:** If Nuwa **pauses by default**, Engram must pause by default (waiver explicit). Soft “you may pause” = PARTIAL. |
| N4 | **Script contract:** Scripts must exist **and** be invoked at the same phase with comparable CLI/output purpose. “Scripts folder exists” ≠ PASS. Diff flags, outputs, exit behavior. |
| N5 | **Template spine:** Every Nuwa `skill-template.md` section must exist in Engram’s template (additive sections OK). Missing section = FAIL for that build step. |
| N6 | **Scorecard weights:** Fidelity dimensions/weights must match Nuwa’s 30/20/20/15/15 dual-agent iron rule unless INTENTIONAL documented. |
| N7 | **Special scenarios:** Living/historical, topic-skill variants, China vs West, obscure person, distill-yourself — each must be a **procedure**, not a bullet slogan. |
| N8 | **Info-gathering skills scan:** Nuwa names a scan of helper skills before Phase 1. Engram must name what to scan and where. Vague “use tools” = FAIL. |
| N9 | **Source policy:** Blacklists/allowlists (Zhihu/WeChat/Baidu; China outlets) must be operable lists, not “prefer quality sources.” |
| N10 | **Lean tax:** Content moved to `references/*.md` is innocent until proven guilty — but **weak binding** is guilty. Score the binding, not the file’s existence. |
| N11 | **Contamination check:** If your PASS set suspiciously matches the prior due-diligence PASS set without new receipts, re-open the five easiest PASSes and try to break them. |
| N12 | **Simulation test:** For at least **5 critical paths**, simulate a cold agent: list exact files opened and actions taken. If you need Nuwa knowledge to fill a hole, Engram FAILs that path. |

## Audit procedure (do in order)

### Phase A — Nuwa process reconstruction (no Engram yet)

1. Read `/Users/jondev/.tink/skills/huashu-nuwa/SKILL.md` end-to-end (or `upstream Nuwa checkout / SKILL.md`).
2. Read Nuwa `references/extraction-framework.md`, `skill-template.md`, `fidelity-scorecard.md`.
3. Skim Nuwa `scripts/*` (signatures, stdout purpose).
4. Write **your own** process map (phases, pause gates, swarm, synthesis, build, validate, refine, specials, scripts) to the deliverable — **do not copy** Engram’s `NUWA-PROCESS-MAP.md` first.

### Phase B — Blind Engram inventory

1. List Engram v2 tree: `SKILL.md`, `references/*`, `scripts/*`, CONSTITUTION/ROADMAP if process-bearing.
2. Extract every phase heading, checkpoint, required-reading row, and “MUST read” pointer.
3. Do **not** yet accept checklist Status values.

### Phase C — Item-by-item prosecution (C01–C72+)

Use Engram’s checklist IDs as a **case docket**, but prosecute from Nuwa:

For each ID:
1. Quote Nuwa’s requirement (short paraphrase + file:line or section heading).
2. Search Engram for the operable counterpart.
3. Assign PASS/PARTIAL/FAIL/INTENTIONAL with **receipts** (file + section/heading; line numbers when practical).
4. If PASS relies on a side file: cite the **in-flow pointer** that forces opening it at the right phase.
5. Note any Engram “improvement” that **changes** Nuwa behavior (default tier, pause polarity, caps) — improvement ≠ parity; mark PARTIAL unless INTENTIONAL.

Add **C73+** for any Nuwa procedure you find that the checklist omitted (process-only; ignore WeChat QR, promo assets, multi-language README marketing).

### Phase D — Deep diffs (mandatory nitpicks)

Run these even if the checklist looks green:

1. **Anti-pattern table:** Nuwa’s 10 rows vs Engram’s table — row-by-row.
2. **Phase 0B:** 10 demand dimensions + max-2-followups + candidate card fields + max-3 candidates + prefer existing skills.
3. **Tier table:** fast/standard/deep caps and cost disclosure behavior (honesty about cost OK; invented dollar figures not required — but “must disclose magnitude before swarm” is).
4. **Failure/degrade table:** every Nuwa row has Engram counterpart.
5. **Phase 5 Agent A:** all 8 dimensions named + 3 dry-runs required.
6. **Phase 5 Agent B:** Nuwa’s routing / frequency / failure-prevention / after-text patches — not a one-liner.
7. **Agentic Protocol:** classify / research / answer; Step-2 tracks derived from models; calibration examples present somewhere operable.
8. **Scripts behavioral diff:**
   - `merge_research.py`
   - `quality_check.py`
   - `download_subtitles.sh`
   - `srt_to_transcript.py`  
   Document flag/output deltas. Material missing behavior → PARTIAL/FAIL on the related checklist ID.
9. **skill-template spine diff:** section list Nuwa vs Engram.
10. **fidelity-scorecard diff:** weights, dual-agent rule, vetoes (Engram vetoes additive OK).
11. **China / blacklist / allowlist** completeness.
12. **Pause gates 1.5 and 2.5** default polarity + waiver mechanism.
13. **Update path:** agents 2+5+6 incremental.
14. **Version self-check:** silent cadence + non-git skip (I4) + discoverability before run.

### Phase E — Cold-agent path simulations (minimum 5)

Write step-by-step “agent would…” traces with **only** Engram files:

1. Named person, standard tier, pure-web distill (0A→0.5→1→1.5 pause→2→2.5 pause→3→4→5).
2. Vague need → 0B → candidate → distill.
3. User drops local PDFs/transcripts → local-first / pure-local mode.
4. China-subject distill (allowlist/blacklist fire).
5. Obscure person (<10 sources) degrade path.
6. *(Bonus)* Distill-yourself; topic-skill variant; update-existing.

Any step where you need Nuwa to know what to do = FAIL/PARTIAL on the governing ID.

### Phase F — Contamination / bias stress test

1. List the 10 PASSes you feel least confident about. Try to break each.
2. Explicitly answer: “Would a skeptical staff engineer sign this at 100%?” If no, your top-line must not be 100%.
3. Forbidden rationalizations:
   - “Lean extraction preserves spirit”
   - “Side file exists so PASS”
   - “We improved on Nuwa”
   - “Prior dry-runs succeeded”
   - “Close enough for English fork”

## Scoring

```
core = non-INTENTIONAL, non-Additive items
weighted = (PASS + 0.5×PARTIAL) / |core|
strict = PASS / |core|
```

Report **pre-bias-correction** if you changed your mind mid-audit.

**Target for “ship-ready” claims:** weighted ≥95% **and** FAIL=0 **and** no PARTIAL on pause gates, six-agent swarm, extraction triple-verify, skill-template fill, dual-agent fidelity, Phase 5 A/B. If those critical IDs are PARTIAL, refuse “ship-ready” language even if weighted ≥95%.

## Deliverable (new file only)

Write:

`~/.tink/skills/engram-v2/references/PARITY-ADVERSARIAL-<YOUR-ID>.md`

(box mirror under `this repository / references/` if working there)

### Required sections

1. **Executive verdict** — one hard sentence. Ban “essentially at parity” mush.
2. **Scores** — weighted / strict / PASS / PARTIAL / FAIL counts; vs prior claimed 100% (as contested claim).
3. **Process map (from Nuwa)** — your reconstruction.
4. **Prosecution table** — every C01–C72+ with status + Nuwa receipt + Engram receipt + nitpick notes.
5. **Deep-diff findings** — anti-patterns, 0B, tiers, degrade, Phase 5 A/B, scripts, templates, scorecard, China policy, pauses.
6. **Cold-agent simulations** — 5+ traces; failures called out.
7. **Contamination stress** — 10 weakest PASSes re-tested.
8. **C73+ omissions** — Nuwa procedures checklist missed (or “none found” with search method).
9. **Intentional cuts** — I1–I4 confirmed present as cuts (not accidentally reintroduced).
10. **Additive Engram** — listed, unscored.
11. **Fix list (priority)** — concrete patches ordered by severity; **do not apply** unless user asked.
12. **Sign-off** — “I would / would not stake my reputation on 100%.” Binary.

## Success criteria for *you* (the auditor)

- You produced receipts, not vibes.
- You attempted to **lower** the score with good-faith nitpicks.
- Critical gates cannot be PARTIAL while calling the factory ship-ready.
- Prior 100% is treated as contested until your independent table agrees **with evidence**.
- Nuwa / v1 untouched.

## Out of scope

- Demis / Karpathy / PG engram dry-run quality (unless used only as optional example of process following).
- Marketing assets, WeChat QR, multi-language README promo.
- Rewriting Nuwa into English.
- Pirate corpus restoration (I1).

## Starter commands (adapt paths)

```bash
# Nuwa headings
rg -n '^### |^## ' ~/.tink/skills/huashu-nuwa/SKILL.md

# Engram headings + pointers
rg -n '^## |^### |references/' ~/.tink/skills/engram-v2/SKILL.md

# Table / gate keywords
rg -n 'pause|CHECKPOINT|档位|反模式|降级|Agent A|Agent B|0B|allowlist|blacklist' \
  ~/.tink/skills/huashu-nuwa/SKILL.md \
  ~/.tink/skills/engram-v2/SKILL.md \
  ~/.tink/skills/engram-v2/references/*.md

# Scripts
diff -u ~/.tink/skills/huashu-nuwa/scripts/merge_research.py \
        ~/.tink/skills/engram-v2/scripts/merge_research.py | head -200
# repeat for quality_check.py, download_subtitles.sh, srt_to_transcript.py

# Templates / scorecards
diff -u ~/.tink/skills/huashu-nuwa/references/skill-template.md \
        ~/.tink/skills/engram-v2/references/skill-template.md | head -300
```

Begin with Phase A. Do not open Engram’s self-congratulatory due-diligence file until Phase F contamination stress — and even then only as a list of claims to attack.
