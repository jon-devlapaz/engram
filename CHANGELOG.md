# Changelog — engram-v2

## [2.5.1] — pure skill surface (2026-09-04)

Removed non-northstar weight from the skill pack: `docs/audit/`, `ROADMAP.md`,
`parity-checklist.md` (archived outside the skill). Skill frontmatter name
`engram`. No distill-procedure change.

---

## [2.5.0] — publish prep (2026-09-04)

Packaging only: LICENSE (MIT), public README, VERSION semver, `.gitignore`,
audit artifacts moved to `docs/audit/`, scrubbed private path / app-only links.
No process behavior change vs v2.5 hardening.

---

## [v2.5] — P1–P3 hardening (2026-09-04)

Unscored adversarial hardening (parallel independent agent). Not parity blockers.

- **P1** `quality_check.py`: bilingual section/heading/marker regexes
  (心智模型 / 表达DNA / 诚实边界 / 张力·矛盾 / 一手… + DNA style CN markers)
- **P2** Protocol tie-breaker restored: Judgment call in `skill-template.md`
  Step 1; mirrored in `SKILL.md` Phase 3 Agentic notes + `agentic-protocol.md`
- **P3** File-type "Raw audio/video" row points at
  `references/info-gathering-skills.md` (gemini-video / installed
  video-transcript skill, else available tooling)

---

## [v2.4] — adversarial parity closures (2026-09-04)

Hostile audit (`docs/audit/PARITY-ADVERSARIAL-HOSTILE-2026-09-04.md`) falsified prior
100%: **97.1% weighted / 94.2% strict / 4 PARTIAL**. User authorized P0 fixes:

- **C09** SKILL tier-confirm: cost magnitude anchor (Nuwa tens-of-dollars
  quote; fast ≈1/3; deep highest) — dropped "leave cost unmeasured"
- **C57** Phase 4: show scorecard **and ask for confirmation**
- **C62** Phase 5: diff summary **and ask for confirmation**
- **C28** `merge_research.py`: restore bilingual primary/secondary/
  contradiction regexes (Chinese fixture 30/60 + 5 matches Nuwa)

**Re-score after fixes: 69/69 PASS → 100% weighted / 100% strict.**
P1–P3 hardening (bilingual quality_check headings, protocol tie-breaker,
transcribe-row pointer) remain optional unscored.

---

## [v2.3] — Nuwa process-parity due diligence (2026-09-04)

Factory-only. Re-verified C01–C72 against engram-v2 after lean extraction
(Stage 6 ~100% claim was for pre-v2 lean). Closed two PARTIALs; FAIL=0.

### Parity
- Fresh Evidence citations in `references/parity-checklist.md`
- `docs/audit/NUWA-PROCESS-MAP.md` — Nuwa phase graph / gates / swarm
- `docs/audit/PARITY-DUE-DILIGENCE-2026-09-04.md` — executive report
- Score after fixes: **100% weighted / 100% strict / FAIL 0**

### Closeable gaps fixed
- Phase 5 Agent B: Nuwa-level routing / frequency / failure-prevention
- Version self-check added to required-reading table (`before run`)
- Tools: scripts live in this pack; Engram en-first captions noted

### Unchanged
- I1–I4 intentional cuts; no pirate ingest; no Nuwa creator attribution
- Additive layers (memory, Stage 8, immersion) out of Nuwa %
- SKILL stays lean (~536 lines); no return to ~769

---

## [v2.2] — fluid attribution + tension dual-voice (2026-09-04)

Factory-only lesson from Demis independent eval (confirmed 96/100; gap to 98).
No Demis dry-run rewrite required for this change — next distill inherits it.

### Template / protocol
- `skill-template.md`: fluid spoken attribution (not `[Subject said]`
  brackets); tension dual-voice in Step 3 + Values; Expression DNA
  citation + mid-answer texture cues; builder note → FIDELITY-GAPS.
- `agentic-protocol.md`: Step 3 packaging items 3–4 updated.
- `FIDELITY-GAPS.md`: Gap toward 98 section (factory levers).
- Phase 3 ship checklist: fluid attribution + tension dual-voice MUST.

### Not in scope of this change
- Demis `builds/v2/` polish (optional, separate from factory).
- Frozen v1 distiller untouched.

---

## [v2.1] — hybrid Step-3 / Evidence classes restore (2026-09-04)

Lesson from Demis Hassabis shared-corpus eval: lean packaging that
thinned Step 3 and Evidence classes cost ~5 FIDELITY pts vs v1.

### Template / protocol
- `references/skill-template.md`: Evidence classes + stakes/peer/cutoff
  role rules; full Step-3 sequence; stakes on core principle; Evidence
  lines require locatable primary URLs/DOIs; Sources self-contained.
- `references/agentic-protocol.md`: Step 3 packaging section — thin
  Step 3 = fidelity regression.
- `references/FIDELITY-GAPS.md`: lean ≠ delete Step-3 / Evidence classes.
- Phase 3 checklist: shipped SKILL MUST include Evidence classes + full
  Step-3 sequence + denser Evidence URLs (hybrid lesson 2026-09-04).

### Preserved writing-for-agents wins
- Short description; extracted special scenarios; mind-first once in
  Defaults; concrete Step-2 look-ats. Do not re-bloat to ~769 lines.

---

## [v2] — writing-for-agents rewrite (2026-09-04)

Relative to frozen Engram v1 (`engram/` beside this pack).

### Writing / agent UX
- Slimmed frontmatter `description` (~200–280 chars): front-loaded
  triggers (`engram`, `distill [person]`); one product line; Stage 8 =
  stakes; one negative branch (ordinary how-would-X → perspective skills).
- Short opening: mind-first, stakes, pure-web/local-first, Unrecorded;
  policy pointed once at Defaults + Stage 8.
- Soft negations flipped to positive targets where safe; hard guardrails
  kept (huashu-nuwa, I1 pirate ban, write-path, informed CTT, Unrecorded).

### Extractions (SKILL leaner; procedure preserved)
- `references/special-scenarios.md` — Living vs historical through Distill
  yourself; China allowlist + blacklist moved here; Phase 1 keeps a
  one-liner pointer.
- `references/agentic-protocol.md` — Munger/Feynman/Taleb/MrBeast
  calibration table; Answer-workflow skeleton stays in skill-template only.
- `references/optional-immersion.md` — Stage 8 immersion/CTT one-line
  pointer target (opt-in, user-supplied, informed CTT, empty 07 fine).
- `references/vague-need.md` — Phase 0B demand → candidate cards.
- `references/info-gathering-skills.md` — optional helper skills by job.
- `references/version-self-check.md` — silent 30-day update check.

### Hygiene
- Phase 3 note: after 2.5 OK, finish Phase 3 SKILL before Phase 4 fidelity.
- Required-reading table lists new disclosed refs.
- README names engram-v2; ROADMAP notes operational how-to is SKILL.md.
- Audit artifact: `docs/audit/WRITING-FOR-AGENTS-AUDIT.md`.

### Preserved (process parity)
- Phases 0–5, quality gates 1.5 / 2.5, six agents, I1–I4 intent.
- Peer curiosity, merge/quality scripts paths, Stage 8 stakes section.
- Mind-first + stakes purpose in CONSTITUTION (light naming only).
