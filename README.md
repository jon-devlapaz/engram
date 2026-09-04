# Engram v2

**Engram** is an English, purist *process* fork of [Nuwa (女娲.skill)](https://github.com/alchaincyf/nuwa-skill).

It turns a named person (or a vague “I need a thinking advisor for X”) into a **runnable skill**: mental models, decision heuristics, expression DNA, honest boundaries — plus Engram additives (memory traces, Stage-8 *stakes*, optional immersion).

| | |
|---|---|
| **Version** | 2.5.0 (see `VERSION`, `CHANGELOG.md`) |
| **License** | MIT — see `LICENSE` |
| **Upstream** | [Nuwa](https://github.com/alchaincyf/nuwa-skill) by Huashu (花叔), MIT |
| **Default product** | Mind-first thinking advisor |
| **Stage 8** | Stakes (skin in the game / why / productive urgency) — not soft immersion |

Nuwa itself is **never modified**. Engram does not claim Nuwa endorsement.

## Quick start

1. Copy or clone this tree into your agent skills directory (example: `~/.tink/skills/engram-v2/`).
2. Read `CONSTITUTION.md`, then `SKILL.md`.
3. Open the `references/` file named for the current phase (table at the top of `SKILL.md`).
4. Distilled outputs land under `engrams/<slug>/` (not Nuwa’s `.claude/skills/*-perspective` path).

```bash
# After a distill, mechanical QA:
python3 scripts/quality_check.py path/to/engrams/<slug>/SKILL.md

# After Phase 1 research ledgers:
python3 scripts/merge_research.py path/to/engrams/<slug>
```

## Pipeline (Nuwa parity)

1. **Phase 0 / 0B** — named person or vague-need diagnosis  
2. **Phase 0.5** — create skill directory + schema  
3. **Phase 1** — six research agents → ledgers `01`–`06` (optional `07` only if immersion requested)  
4. **Phase 1.5 / 2.5** — pause checkpoints (unless `waiver: run-through`)  
5. **Phase 2** — triple-verified models + expression DNA (`extraction-framework.md`)  
6. **Phase 3** — fill `skill-template.md` (Agentic Protocol, Evidence classes, full Step-3)  
7. **Phase 4 / 5** — `quality_check.py` + dual-agent fidelity scorecard + refine  

Process parity vs Nuwa was adversarially re-scored at **69/69** after documented fixes. Receipts live in `docs/audit/` and `references/parity-checklist.md`.

## Intentional cuts vs Nuwa

| ID | Cut |
|---|---|
| I1 | No Z-Library / LibGen / pirate book download — legal sources / user-supplied files only |
| I2 | Write path `engrams/<slug>/` |
| I3 | Engram fork attribution (not the Nuwa creator block) |
| I4 | Non-git version-check skip when the install is not a clone |

## Layout

```
SKILL.md              # Distiller runbook
CONSTITUTION.md       # Non-negotiables
LICENSE / VERSION / CHANGELOG.md
references/           # Phase refs (template, scorecard, scenarios, …)
scripts/              # merge_research, quality_check, subtitles, srt clean
docs/audit/           # Parity / writing audits (historical receipts)
ROADMAP.md            # Historical G0–G8 gate log (not the runbook)
```

## What this repo is not

- Not a dump of distilled person skills (Paul Graham, Karpathy, Hassabis, …). Publish those separately if you choose.
- Not a weight-edit / “soul copy” system. Disclosed simulation only.
- Not permission to deceive evaluators or use the subject’s name as endorsement.

## Related

- Upstream Nuwa: https://github.com/alchaincyf/nuwa-skill  
- Engram v1 (frozen ancestor of this rewrite) may live beside this pack as `engram/` — do not mutate it as part of v2 work.

## Contributing

Prefer process fixes with receipts (checklist ID + Nuwa cite + Engram cite). Keep intentional cuts documented. Do not reintroduce pirate ingest.
