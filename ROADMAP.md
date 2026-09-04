# Engram ↔ Nuwa process-parity roadmap

> **Historical.** Stages G0–G8 record how Engram reached Nuwa process parity.
> **Operational how-to is `SKILL.md`.** Do not treat this file as the distill runbook.
> Parity status as of 2.5.0: adversarial re-score **69/69** (see `docs/audit/` and
> `references/parity-checklist.md`).


Baseline (2026-09-03 audit): **~72% weighted / ~64% full-pass** on 69 core
process items. Spine exists. Operational procedures that change a distill
are incomplete.

Goal: **≥95% weighted** on the same checklist, with every FAIL closed or
explicitly marked INTENTIONAL, and a dry-run distill that exercises the
new paths.

Locked INTENTIONAL cuts (do not "fix" these):
1. No Z-Library / LibGen / pirate acquisition
2. Write path = `~/.tink/skills/engrams/<slug>/` (not `.claude/skills/`)
3. Fork attribution (Engram), not 花叔 creator block

Method for every stage:
- Port procedure from Nuwa SKILL.md into Engram SKILL.md (English)
- Keep Nuwa untouched
- Re-run the parity scorer (same item list) before calling the stage done
- Do not start the next stage until the gate passes

---

## Stage 0 — Freeze the measuring stick

**Status: COMPLETE 2026-09-03 — G0 PASS**  
Artifact: `references/parity-checklist.md`

**Work**
- [x] Save the 69-item audit checklist as `references/parity-checklist.md`
  (PASS / PARTIAL / FAIL / INTENTIONAL definitions + current scores)
- [x] Re-score instructions embedded in that file (read pack; no vibes)

**Gate G0 — PASS when**
- [x] Checklist file exists and lists every FAIL/PARTIAL from the audit
- [x] INTENTIONAL cuts listed and agreed (I1–I4)
- [x] Current score recorded: 72% weighted / 64% strict

**Exit:** measuring stick frozen. No distill runs against a moving bar.

---

## Stage 1 — Corpus acquisition parity (biggest run change)

**Status: COMPLETE 2026-09-03 — G1 PASS**  
Closed: C19, C20, C21, C22, C30, C09. I1 (no pirate ingest) remains locked.

Closes: three modes, local-first four-step, file-type→ledger map,
copy-into-`sources/` + local-corpus mode, podcast transcript hint.

**Work**
1. [x] Add Nuwa's mode table to Phase 1 (pure-web / local-first / pure-local)
2. [x] Add file-type → ledger coverage table
3. [x] Phase 0.5 checklist: copy into `sources/`, mark mode
4. [x] Podcast transcript sites (podcastnotes.org)
5. [x] Pirate refusal remains in Tools (I1)

**Gate G1 — PASS when**
- [x] All three modes named with trigger + strategy
- [x] Four-step local-first procedure is copy-pasteable by an agent
- [x] File-type table present
- [x] 0.5 checklist includes sources/ ingest + mode flag
- [x] Parity scorer: C19–C22, C30 → PASS; C09 → PASS
- [x] Dry-run calibration baked into SKILL.md: Foo.pdf + Bar.srt → local-first; 01+03 / 02+03; web only for thin/empty ledgers

**Exit score:** ~80% weighted / ~72% strict (FAIL 9)

---

## Stage 2 — Checkpoint discipline (when the human intervenes)

**Status: COMPLETE 2026-09-03 — G2 PASS**  
Closed: C38, C47. Waiver: `waiver: run-through` only.

Closes: 1.5 and 2.5 default **pause** like Nuwa; "don't block delivery"
stays for Phase 0 clarifying questions only.

**Work**
1. [x] Phase 1.5 pause after merge_research
2. [x] Phase 2.5 pause after synthesis summary
3. [x] Phase 0 defaults remain non-blocking; 1.5/2.5 are gates
4. [x] One-line waiver only (`run through` / `don't stop at checkpoints` / `skip the gates`)

**Gate G2 — PASS when**
- [x] SKILL.md says pause at 1.5 and 2.5 unless an explicit run-through waiver
- [x] Waiver language is one line, not a loophole that deletes the gates
- [x] Parity: C38, C47 → PASS

**Exit score:** ~81% weighted / ~75% strict (FAIL still 9)

---

## Stage 3 — Intake & recommendation (Phase 0B depth)

**Status: COMPLETE 2026-09-03 — G3 PASS**  
Closed: C10, C12, C14.

Closes: 10-row demand table, candidate card format, person-vs-topic
choice at intake (not only in the framework).

**Work**
1. [x] Ten demand dimensions in English
2. [x] Candidate card: lens / why / limit; max 3; prefer existing
3. [x] Person vs topic at 0B Step 2
4. [x] Max-two-questions rule kept; paper calibration in SKILL.md

**Gate G3 — PASS when**
- [x] All 10 dimensions present with example phrasing + framework direction
- [x] Candidate card template present
- [x] Person vs topic decision is in Phase 0B
- [x] Paper exercise baked in: wrong products → Startup & business, ≤3 candidates

**Exit score:** ~84% weighted / ~80% strict (FAIL 8)

---

## Stage 4 — Runtime construction depth (Phase 3)

**Status: COMPLETE 2026-09-03 — G4 PASS**  
Closed: C49, C51.

Closes: frontmatter length cap, Agentic Protocol Step-2 worked examples.

**Work**
1. [x] Frontmatter warning: ~300 chars practical, hard fail near skill-loader
   ~1024; prefer name + clear triggers over keyword stuffing
2. [x] Port four worked examples for research-track derivation:
   Munger / Feynman / Taleb / MrBeast (English, same causal shape)
3. [x] Require Step-2 tracks to be derived from *this* subject's models, with
   the examples as calibration not copy-paste content into every engram

**Gate G4 — PASS when**
- [x] Length cap text present
- [x] Four examples present
- [x] Template + SKILL.md both say: tracks come from models, not generic search
- [x] Paper exercise: given 3 fake mental models, agent writes 3–5 research
      tracks that clearly descend from those models

**Exit score:** ~87% weighted / ~83% strict (FAIL 6)

---

## Stage 5 — Special scenarios & source playbooks

**Status: COMPLETE 2026-09-03 — G5 PASS**  
Closed: C33, C66, C67, C68, C18, C29, C69, C70.

Closes: living vs historical, topic-skill phase variants, distill-yourself,
obscure-person procedure, China outlet allowlist, named info skills,
China/West playbook fullness.

**Work**
1. [x] Living vs historical section (cutoff discipline vs biography bias)
2. [x] Topic-skill phase variant table (full Nuwa rows)
3. [x] Distill-yourself: required materials + self-serving-memory warning
4. [x] Obscure person: warn at 0.5 if <10 sources; 2–3 models; expand boundary
5. [x] Chinese outlet allowlist (36kr, LatePost, Caixin, GeekPark, etc.) +
   Bilibili/Xiaoyuzhou originals
6. [x] Named skill scan table — map Nuwa names to whatever exists under
   `~/.tink/skills/` (pdf/video/article readers); say "use if present"

**Gate G5 — PASS when**
- [x] Each special scenario has a procedure, not a one-liner
- [x] Outlet allowlist present
- [x] Topic-skill table has phase-by-phase variants
- [x] Self-distill names materials + bias risk
- [x] Former Special/China FAILs → PASS or PARTIAL≤1

**Exit score:** ~96% weighted / ~94% strict (FAIL 2)

---

## Stage 6 — Taste, anti-patterns, meta

**Status: COMPLETE 2026-09-03 — G6 PASS**  
Closed: C64, C65, C60, C71.

Closes: 品味守则 three lines; numbered 10-row anti-pattern table;
`.last-update-check` procedure (non-git skip when Engram is not a clone).

**Work**
1. [x] Taste rules: long-form > quotes; controversy > consensus; change > fixed
2. [x] Expand anti-patterns to Nuwa's 10-row table + Engram extras (pirate,
   deceptive CTT, etc.)
3. [x] Version self-check ported. Engram is not a git clone; the
   procedure's non-git branch writes the date and stays silent (I4).

**Gate G6 — PASS when**
- [x] Three taste lines present
- [x] Anti-pattern table ≥ Nuwa's 10 + Engram extras
- [x] Version check either implemented or INTENTIONAL with reason
- [x] Weighted parity ≥ **95%**; FAIL count = 0 except INTENTIONAL

**Exit score:** ~100% weighted / ~100% strict (FAIL 0)

---

## Stage 7 — Integration dry-run (proves the manual)

**Status: COMPLETE 2026-09-04 — G7 PASS**  
Subject: **Paul Graham** (user choice; Ng/Karpathy were defaults).  
Mind-only, standard, pure-web + one user-supplied YouTube Q&A.

**Work**
1. [x] Mind-only dry-run, no CTT claim — `paul-graham`
2. [x] Stages 0–6 procedures into engram folder
3. [x] pure-web; pause 1.5 + 2.5; merge_research; quality_check;
   fidelity dual-agent; false-memory veto
4. [x] `FIDELITY.md` (97/100 A) + `PARITY-RUN.md`

**Gate G7 — PASS when**
- [x] Directory self-contained with 01–06 present
- [x] `quality_check.py` PASS (7/7)
- [x] Fidelity grade ≥ B **and** false-memory veto PASS (A + PASS)
- [x] No research written outside the engram folder
- [x] PARITY-RUN.md maps steps to Stages 1–6
- [x] Distiller checklist still ≥95% (G6 unchanged)

**Exit:** process parity demonstrated. Artifact:
`~/.tink/skills/engrams/paul-graham/`

---

## Stage 8 — Stakes layer (after parity; next hill after mind)

Only after G7. Does not count toward Nuwa parity. **Does not block
shipping a mind engram** — G7 still ships. Engram's default product is
mind / thinking advisor; **G8 makes that mind carry weight**: skin in
the game, why-of-existence, productive urgency.

**Policy (decisive)**
- Stakes are **corpus-evidenced**, never invented pathos or fake urgency.
- Soft partner-register / mushy intimate texture is **not** G8 and is
  **not** the proven path for task quality. Keep it a separate opt-in.
- Empty 07 is fine. Prefer writings, decisions, and real downside over
  relational mush.
- The agent should **invoke** why it exists under consequential asks —
  not perform feelings.

**Work**
- Write `STAKES.md` / `08-stakes`: why this engram exists; subject's
  skin in the game; productive-urgency triggers + anti-melodrama rules
- Wire runtime retrieval before high-leverage advice
- Stakes probe (consequential framing changes answer the corpus way;
  silence stays Unrecorded)

**Gate G8 — PASS when**
- [ ] G7 already green
- [ ] Evidenced STAKES artifact (why / skin / urgency)
- [ ] Runtime hooks retrieve stakes on consequential advice
- [ ] Stakes probe PASS (no invented pathos; no immersion smuggled in)

---

## Sequence diagram

```
G0 freeze checklist
    → G1 corpus modes / local-first
        → G2 checkpoint pauses
            → G3 Phase 0B depth
                → G4 protocol examples + frontmatter cap
                    → G5 special scenarios + outlets
                        → G6 taste / anti / meta
                            → G7 dry-run distill
                                → G8 stakes (why / skin / productive urgency)
```

No skipping gates. If a stage fails, fix that stage; do not paper over
with Stage 7.

## Effort sketch (order-of-magnitude)

| Stage | Nature | Rough size |
|---|---|---|
| 0 | Checklist file | small |
| 1 | SKILL.md Phase 1 surgery | medium |
| 2 | Checkpoint wording | small |
| 3 | Phase 0B port | medium |
| 4 | Phase 3 examples | small–medium |
| 5 | Special scenarios | medium–large |
| 6 | Taste + anti table | small |
| 7 | Full dry-run | large (real research) |
| 8 | Optional | large + consent |

## Definition of done for the whole roadmap

1. Checklist score ≥95% weighted, 0 non-intentional FAILs
2. G7 dry-run green
3. Nuwa tree untouched
4. INTENTIONAL cuts still documented in CONSTITUTION.md / SKILL.md
