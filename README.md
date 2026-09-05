# Engram

**Engram** turns a person (or a vague need) into a **runnable thinking-advisor skill** — mental models, heuristics, expression DNA, honest boundaries — plus memory traces and Stage-8 *stakes*. Soft immersion is opt-in only.

| | |
|---|---|
| **Version** | 3.0.0 |
| **License** | MIT (`LICENSE`) |

**v3 purity.** Distill-only northstar: canonical pack path is `engram/` (matching GitHub). Scripts own **deterministic** structure gates (`quality_check`, `test_smoke`, doctor/phase1/ax); agents own **judgment** (fidelity-scorecard, Stage 8 stakes, synthesis). No audit stubs; no vendor branding in load-bearing docs.

## Happy path

User says `distill <name>`; agent owns scripts. User consents only for
host installs and checkpoints 1.5/2.5 (`approve | revise | stop`).
See `references/happy-path.md`.

## Install

Place this tree where your agent loads skills:

```text
<skills-root>/engram/
```

`<skills-root>` is your agent's skills directory — whatever path that is on the host. Engram never assumes a vendor home folder. Install name is **`engram` only** (not a versioned folder name).

1. Read `CONSTITUTION.md`, then `SKILL.md`.
2. Open `references/` files as the phase table in `SKILL.md` directs.
3. Write distilled outputs to `engrams/<slug>/`.

```bash
python3 scripts/engram_doctor.py --engram path/to/engrams/<slug>
python3 scripts/phase1_gate.py --engram path/to/engrams/<slug>
python3 scripts/ax_gate.py --engram path/to/engrams/<slug>
python3 scripts/merge_research.py --engram path/to/engrams/<slug>
python3 scripts/quality_check.py --engram path/to/engrams/<slug>
python3 scripts/test_smoke.py   # pack regression vs examples/minimal-fixture
```

Prefer `--engram <dir>` (canonical). Positional `<dir>` / `<SKILL.md>` still accepted for backward compatibility.

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
scripts/            # doctor, phase1_gate, ax_gate, merge_research, quality_check, test_smoke, captions
examples/           # minimal-fixture (smoke / onboarding — not a real subject)
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
