# Engram

**Engram** turns a person (or a vague need) into a **runnable thinking-advisor skill** — mental models, heuristics, expression DNA, honest boundaries — plus memory traces and Stage-8 *stakes*. Soft immersion is opt-in only.

| | |
|---|---|
| **Version** | 2.5.6 |
| **License** | MIT (`LICENSE`) |

## Install

Place this tree where your agent loads skills (example: `<skills-root>/engram/`).

`<skills-root>` is your agent's skills directory — whatever path that is on the host. Engram never assumes a vendor home folder.

1. Read `CONSTITUTION.md`, then `SKILL.md`.
2. Open `references/` files as the phase table in `SKILL.md` directs.
3. Write distilled outputs to `engrams/<slug>/`.

```bash
python3 scripts/merge_research.py path/to/engrams/<slug>
python3 scripts/quality_check.py path/to/engrams/<slug>/SKILL.md
```

## Recommended helpers

For **max-quality** Phase 1 corpora, install skills (any brand) that cover
these jobs — see `references/info-gathering-skills.md`:

| Job | Why it matters |
|---|---|
| Video → transcript | Local video without captions |
| Full-article reader | Real pages, not search snippets |
| Multi-platform gatherer | X / Reddit / YouTube fragments |
| Structured deep research | Depth on one dimension |
| PDF text extraction | User-supplied books / papers |

Engram still runs without them; corpus quality drops. Prefer installing
before a standard or deep distill.

## What ships in this pack

```
SKILL.md            # Distiller
CONSTITUTION.md     # Non-negotiables
references/         # Phase refs (template, scorecard, scenarios, …)
scripts/            # merge_research, quality_check, captions, srt clean
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
