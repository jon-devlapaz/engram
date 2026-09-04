# Nuwa process map (system of record)

**Source:** `upstream Nuwa checkout / ` (prefer over thin `Nuwa snapshot / `).  
**Purpose:** process graph for Engram v2 parity audits. Marketing / WeChat / community promo omitted.

## Phase graph

```
Entry
  ├─ named person/topic ──► Phase 0A (clarify) ──► Phase 0.5
  └─ vague need ──────────► Phase 0B (diagnose → ≤3 cards)
                              ├─ pick existing skill → DONE (activate)
                              └─ pick new distill → 0A details → 0.5

0.5 create dir + China/obscure/corpus switches
  └─► Phase 1 six-agent swarm (or serial degrade)
        └─► Phase 1.5 PAUSE (merge_research table) ── user OK / supplement
              └─► Phase 2 synthesis (must read extraction-framework)
                    └─► Phase 2.5 PAUSE (synthesis summary) ── user OK / revise
                          └─► Phase 3 build (skill-template + Agentic Protocol)
                                └─► Phase 4 validate (pass table + scorecard)
                                      └─► Phase 5 dual-agent refine → ship
Update path: read cutoff → agents 2+5+6 incremental → surgical patch
```

## Pause gates

| Gate | Default | Waiver |
|---|---|---|
| Phase 0 clarifying | **Non-blocking** — defaults; do not hold deliverable behind questions | n/a |
| Phase 1.5 research review | **PAUSE** for user OK / supplement | none in Nuwa SKILL (Engram adds `waiver: run-through`) |
| Phase 2.5 synthesis summary | **PAUSE** for user OK / revise | same |
| Phase 4 show validation | Show results before calling done | — |
| Phase 5 show diff summary | User confirms applied edits | — |

## Swarm shape (Phase 1)

| Agent | File | Hunt focus |
|---|---|---|
| 1 Writings | `01-writings.md` | Books, long form, coined terms, reading lists |
| 2 Conversations | `02-conversations.md` | Podcasts, long video, AMA, pressed answers |
| 3 Expression | `03-expression-dna.md` | Short posts, debates, fingerprint |
| 4 External | `04-external-views.md` | Criticism, biography, peer contrast |
| 5 Decisions | `05-decisions.md` | Dated actions, regret, talk vs walk |
| 6 Timeline | `06-timeline.md` | Milestones, thought-shifts, **last 12 months** |

Hard rules: write file inside skill; locator + confidence; said vs about vs inference; keep contradictions.

Acquisition modes: pure-web / local-first (classify → gaps → search gaps → label origin) / pure-local.

## Synthesis gates (Phase 2)

Must read `references/extraction-framework.md`.

1. Models 3–7: scan → 15–30 candidates → triple verify (cross-domain, generative, exclusive) → rank by exclusivity  
2. Heuristics 5–10 with cases  
3. Expression DNA (fingerprint / poles / taboos)  
4. Values, anti-patterns, tensions  
5. Intellectual lineage  
6. Honest boundary  

## Build / validate / refine

**Phase 3:** fill every `skill-template.md` section; frontmatter ~300 / loader ~1024; derive Agentic Protocol Step-2 tracks from *this* subject's models (calibration: Munger / Feynman / Taleb / MrBeast); walk framework quality checklist.

**Phase 4:** independent answerer (no web) + judge; six-row pass table; iterate 2→4 at most twice; show validation; fidelity-scorecard 30/20/20/15/15 dual-agent.

**Phase 5:** Agent A — 8-dimension structure + 3 dry-runs, rewrite two weakest; Agent B — triggers + role-play operability (routing / frequency / failure prevention) + missing facts, 2–3 patches; apply non-conflicting edits; show summary.

## Special scenarios (in Nuwa SKILL)

- Living vs historical (cutoff vs biography bias)  
- Topic-skill phase-variant table (0A–4)  
- China vs West source playbook + blacklist (Zhihu / WeChat / Baidu) + Chinese outlet allowlist  
- Obscure person (<10 sources): warn, 2–3 models, expand boundary, prefer user corpus  
- Distill yourself: halt for corpus; self-serving-memory warning  

## Taste / anti / meta

- Taste: long-form > quotes; controversy > consensus; change > fixed  
- Anti-pattern 10-row table  
- Silent version self-check (30-day `.last-update-check`; non-git skip)  
- Update: agents 2+5+6 incremental  

## Scripts (behavioral jobs)

| Script | Job |
|---|---|
| `download_subtitles.sh` | yt-dlp captions; Nuwa prefers zh then en then auto |
| `srt_to_transcript.py` | Strip timestamps / dupes / HTML → readable transcript |
| `merge_research.py` | Phase 1.5 table: source counts, primary share, findings, contradictions |
| `quality_check.py` | Phase 4 mechanical six checks (models, limits, DNA, boundary, tensions, primary) |

## References spine

- `extraction-framework.md` — triple verify, DNA, contradictions, thin-info, person vs topic, quality self-check  
- `skill-template.md` — frontmatter → role-play → identity → models → heuristics → DNA → timeline → values → lineage → boundary → sources (+ Nuwa creator attribution block)  
- `fidelity-scorecard.md` — five dimensions, independent dual-agent, FIDELITY.md  

## Intentional Engram cuts (not Nuwa bugs)

I1 pirate books · I2 write path `~/.tink/skills/engrams/` · I3 Engram attribution · I4 non-git version skip  

## Additive Engram (out of Nuwa parity %)

Memory / TRACE admission · Stage 8 stakes · optional immersion / informed CTT · peer curiosity · intimate ledger 07  
