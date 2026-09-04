# Engram

**Engram** turns a person (or a vague need) into a **runnable thinking-advisor skill** — mental models, heuristics, expression DNA, honest boundaries — plus memory traces and Stage-8 *stakes*. Soft immersion is opt-in only.

| | |
|---|---|
| **Version** | 2.7.2 |
| **License** | MIT (`LICENSE`) |

## Install

Place this tree where your agent loads skills (example: `<skills-root>/engram/`).

`<skills-root>` is your agent's skills directory — whatever path that is on the host. Engram never assumes a vendor home folder.

1. Read `CONSTITUTION.md`, then `SKILL.md`.
2. Open `references/` files as the phase table in `SKILL.md` directs.
3. Write distilled outputs to `engrams/<slug>/`.

```bash
python3 scripts/engram_doctor.py          # preflight (helpers + CLIs)
python3 scripts/merge_research.py path/to/engrams/<slug>
python3 scripts/quality_check.py path/to/engrams/<slug>/SKILL.md
```

## Nested helpers (Phase 1)

Shipped under `helpers/` — skill-within-skill:

| Folder | Job |
|---|---|
| `gemini-video` | local video → transcript (`GEMINI_API_KEY`) |
| `web-article-reader` | full article → markdown |
| `agent-reach` | multi-platform gather |
| `deep-research` | structured deep research |
| `pdf` | PDF/DOCX/EPUB → markdown (MIT `huashu-md-html`) |
| `doctor` | preflight + troubleshooting wizards (`scripts/engram_doctor.py`) |

See `helpers/README.md` and `helpers/THIRD_PARTY.md`.

Phase 1 **hard-binds** these into every agent spawn (Helper block + per-agent routing in `SKILL.md` / `references/info-gathering-skills.md`).


## What ships in this pack

```
SKILL.md            # Distiller
CONSTITUTION.md     # Non-negotiables
helpers/            # Nested Phase-1 skills (video, article, reach, research, pdf, doctor)
references/         # Phase refs (template, scorecard, scenarios, …)
scripts/            # engram_doctor, merge_research, quality_check, captions, srt clean
LICENSE VERSION CHANGELOG.md README.md
```

## Intentional cuts

| ID | Cut |
|---|---|
| I1 | Books only from user-supplied or otherwise legal access |
| I2 | Write path `engrams/<slug>/` |
| I3 | Engram attribution on shipped person-skills |
| I4 | Non-git version-check skip when the install is not a clone |

## Not in this repo

- Distilled person skills (publish separately)
- Promo / marketing assets

## Contributing

Prefer process fixes with receipts. Keep intentional cuts documented.
