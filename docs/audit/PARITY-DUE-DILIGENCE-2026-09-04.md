# Engram v2 ↔ Nuwa process-parity due diligence

**Date:** 2026-09-04 (America/Chicago)  
**System of record:** `upstream Nuwa checkout / ` (huashu-nuwa)  
**Audited factory:** `this repository / `  
**Frozen reference (untouched):** `frozen Engram v1 / `  
**Process map:** `docs/audit/NUWA-PROCESS-MAP.md`  
**Checklist:** `references/parity-checklist.md`

## Verdict

**Ship-ready process parity** for Nuwa distill procedure (core C01–C72 excl. I1–I4). Weighted **100%** / strict **100%** / FAIL **0** after two closeable PARTIAL fixes. Additive Engram layers remain out of the Nuwa %. Intentional cuts I1–I4 stay.

Honesty note: the Stage 6 “~100%” claim in the old checklist was scored against **pre-v2 lean**. This pass re-verified every ID against **engram-v2** after content moved to side files. Lean extraction held: strong in-flow pointers + operable procedures in references = PASS. Two thin spots were real and are now closed.

## Scores

| Checkpoint | Weighted | Strict | FAIL | PARTIAL |
|---|---|---|---|---|
| Stage 0 freeze (2026-09-03) | ~72% | ~64% | 14 | 11 |
| Claimed Stage 6 (pre-v2 lean) | ~100% | ~100% | 0 | 0 |
| **Re-score before fixes (engram-v2 lean)** | **~98.6%** | **~97.1%** | **0** | **2** |
| **After fixes (this pass)** | **100%** | **100%** | **0** | **0** |

Core denominator = 69 (excludes INTENTIONAL C34/C53/C72 and Additive).

## PARTIAL / FAIL found and disposition

| ID | Pre-fix | Issue | Fix | Post |
|---|---|---|---|---|
| C61 | PARTIAL | Agent B only said "role-play operability"; Nuwa names routing, frequency constraints, failure prevention + after-text patches | Expanded Phase 5 B in SKILL.md | PASS |
| C71 | PARTIAL | version-self-check only at SKILL end; easy to miss vs required-reading nav | Added `before run` row → `version-self-check.md` in required-reading table | PASS |
| — | FAIL | none | — | — |

Also documented (not scored as FAIL): scripts live in factory pack (not copied into each output engram); caption language order en-first vs Nuwa zh-first — intentional English runtime.

## Intentional cuts (unchanged)

| ID | Cut |
|---|---|
| I1 | No pirate book ingest (Z-Lib / LibGen) |
| I2 | Write path `~/.tink/skills/engrams/<slug>/` |
| I3 | Engram attribution, not 花叔 / Nuwa creator block |
| I4 | Non-git installs skip version pull quietly |

## Additive Engram layers (out of Nuwa %)

- Memory / TRACE four-test admission + `MEMORY.md`  
- Intimate ledger 07 + informed CTT / false-memory veto  
- Stage 8 stakes (`STAKES.md`, productive urgency)  
- Peer curiosity / `PEERS.md`  
- Optional immersion track (`optional-immersion.md`)

## Lean side-file verification (risk areas)

| Risk area | Location | Pointer strength | Result |
|---|---|---|---|
| Phase 0B 10-row + cards | `vague-need.md` | SKILL Phase 0B "read … follow" | PASS |
| China allowlist / blacklist / dual playbook | `special-scenarios.md` | 0.5 checklist + Phase 1 one-liner | PASS |
| Living / historical, topic variants, self-distill, obscure | `special-scenarios.md` | SKILL Special scenarios + 0.5 | PASS |
| Anti-pattern 10-row | SKILL Anti-patterns | in-flow table 1–10 (+11–17) | PASS |
| Taste rules | SKILL Taste rules | three tie-breakers in-flow | PASS |
| Agent A 8 dims + 3 dry-runs | SKILL Phase 5 | eight named dims | PASS |
| Version self-check | `version-self-check.md` | section + required-reading (fixed) | PASS |
| Info-gathering skills scan | `info-gathering-skills.md` | SKILL Named info-gathering skills | PASS |
| Podcast sites hint | SKILL Tools | podcastnotes.org + show site | PASS |
| Frontmatter cap | SKILL fill table + template | ~300 / ~1024 | PASS |
| Munger/Feynman/Taleb/MrBeast | `agentic-protocol.md` | SKILL Agentic Protocol generation | PASS |
| Degrade/failure table | SKILL Failure table | seven rows | PASS |
| merge / quality / subtitle scripts | `scripts/*` | Tools + 1.5 / Phase 4; pack path clarified | PASS |

## C73+ findings

No new process-parity IDs added. Reviewed and rejected as checklist items:

- Nuwa Phase 4.1/4.2/4.3 naming → already encoded in fidelity-scorecard item set  
- Per-engram scripts copy → packaging, documented intentional  
- Community / WeChat / promo → out of scope  

## Scripts / template parity

Behavioral jobs match Nuwa. Differences: English regexes/markers; Engram en-first captions; optional 07 in merge; additive memory check in quality_check. Template spine matches Nuwa sections; Engram adds Agentic Protocol in-template plus peers/stakes/evidence classes (additive).

## Files changed this pass

- `SKILL.md` — Agent B expand; version-self-check in required reading; scripts pack-path + caption-order note (~536 lines, under 600)  
- `references/parity-checklist.md` — full fresh Evidence + scores + changelog  
- `docs/audit/NUWA-PROCESS-MAP.md` — new  
- `docs/audit/PARITY-DUE-DILIGENCE-2026-09-04.md` — this report  
- `CHANGELOG.md` — [v2.3] entry  

Nuwa / huashu-nuwa / frozen engram v1: **not edited**.
