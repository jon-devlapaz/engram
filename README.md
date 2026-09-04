# Engram

**Engram** is an English, purist *process* fork of [Nuwa (女娲.skill)](https://github.com/alchaincyf/nuwa-skill).

Northstar: turn a person (or a vague need) into a **runnable thinking-advisor skill** — mental models, heuristics, expression DNA, honest boundaries — with Engram additives (memory traces, Stage-8 *stakes*). Soft immersion is opt-in only.

| | |
|---|---|
| **Version** | 2.5.0 |
| **License** | MIT (`LICENSE`) |
| **Upstream** | [Nuwa](https://github.com/alchaincyf/nuwa-skill) · Huashu (花叔) · MIT |

This repository is the **skill pack only** (runbook + references + scripts). It is not a dump of distilled people, promo assets, or audit history.

## Install

Place this tree where your agent loads skills (example: `~/.tink/skills/engram/`).

1. Read `CONSTITUTION.md`, then `SKILL.md`.
2. Open `references/` files as the phase table in `SKILL.md` directs.
3. Write distilled outputs to `engrams/<slug>/` (not Nuwa’s `.claude/skills/*-perspective`).

```bash
python3 scripts/merge_research.py path/to/engrams/<slug>
python3 scripts/quality_check.py path/to/engrams/<slug>/SKILL.md
```

## What ships in this pack

```
SKILL.md            # Distiller
CONSTITUTION.md     # Non-negotiables
references/         # Phase refs (template, scorecard, scenarios, …)
scripts/            # merge_research, quality_check, captions, srt clean
LICENSE VERSION CHANGELOG.md README.md
```

## Intentional cuts vs Nuwa

| ID | Cut |
|---|---|
| I1 | No pirate book download (Z-Library / LibGen) |
| I2 | Write path `engrams/<slug>/` |
| I3 | Engram attribution (not Nuwa creator block) |
| I4 | Non-git version-check skip when not a clone |

## Not in this repo

- Distilled person skills (publish separately)
- Parity/audit receipts (kept out of the skill surface)
- Nuwa promo / WeChat / multi-language marketing

## Related

- Upstream: https://github.com/alchaincyf/nuwa-skill
