# Changelog — Engram

## 2.7.7 — quality_check Sources heading swallow (2026-09-04)

- Fix greedy `re.DOTALL` + `Source` matching inside URLs like `.../resources/...`
  (Ada Lovelace dogfood): Sources/Honest-boundary headings are single-line + word-boundary.
- `download_subtitles.sh`: detect new captcha via `-newer MARKER` (not `-mmin -1`).
- `quality_check`: frontmatter `description` length — FAIL >1024, note >400.

## 2.7.6 — Happy-path bootstrap + Gemini dogfood fixes (2026-09-04)

- Add `references/happy-path.md`; README + SKILL Phase 0/0.5 point at it
  (agent owns scripts; user consents host installs + 1.5/2.5 only).
- P0: `engram_doctor._can_import` catches ModuleNotFoundError / ValueError /
  AttributeError so dotted `google.genai` never crashes doctor.
- P1: `ax_gate` check I — empty url-cache at phase 0.5 → WARN not FAIL;
  FAIL missing dir or empty after Phase 1.5+/G*.
- P1: `quality_check` counts ### Primary / ### Secondary bullets; honest
  boundary accepts numbered lists; template 4+1 primary PASS.
- P2: yt-dlp demoted to optional WARN (phase1_gate no longer blocked);
  `merge_research` counts local `sources/...` paths; `download_subtitles.sh`
  surfaces yt-dlp stderr + `-mmin -1` on auto-sub find; `--engram` on
  merge_research + quality_check (positional kept).
- P3: schema PERSON.md relational-texture typo; gemini-video `.env` path
  docstring; ax-ops / check D host-neutral reconnect language.

## 2.7.5 — AX hill-climb quality gates (2026-09-04)

- Doctor: optional `--engram`; url-cache-process **PASS** when
  `sources/url-cache/` has ≥1 `*.md` (warn + enable-url-cache if empty;
  pack-only doctor keeps info warn).
- `phase1_gate.py` passes `engram=` into `run_checks` so Jung smoke shows
  url-cache PASS not WARN.
- Add `scripts/ax_gate.py` (pack A–E; optional engram F–J) and
  `references/ax-ops.md` (STATUS schema, AX beat, hard verbs, machine-down,
  INDEX + stub quarantine).
- SKILL.md: STATUS.md at 0.5; **approve | revise | stop** at 1.5/2.5;
  AX beats after 1.5/2.5/4/G8; machine-down failure row; ax_gate on Done.

## 2.7.4 — Phase 1 spawn gate (2026-09-04)

- Add `scripts/phase1_gate.py`: runs doctor, requires `--engram` +
  `sources/url-cache/` (optional `--mkdir-cache`); exit 0 only when safe
  to spawn Phase 1 (`blocker_fails == 0` and cache present).
- Wire gate into SKILL.md Phase 0.5 checklist and info-gathering Preflight.

## 2.7.3 — Jung postmortem surgical process (2026-09-04)

- Hard doctor gate: no Phase 1 spawn while `blocker_fails > 0`.
- Mandatory url-cache write-on-miss (`sha256[:16].md`) + checklist mkdir.
- Spine-first spawn (Agent 6 / optional `00-spine.md`) to cut duplicate
  deep-research.
- Normalized helper log schema in `PARITY-RUN.md`.
- Optional I1 enrichment ask before deep gather when quote density matters.

## 2.7.2 — Gemini .env for doctor (2026-09-04)

Doctor accepts `helpers/gemini-video/.env` (gitignored) for API key presence.

## 2.7.1 — URL cache in Helper block (2026-09-04)

enable-url-cache wired into Helper block + pre-Phase-1 checklist.

## 2.7.0 — preflight doctor + troubleshooting wizards (2026-09-04)

`scripts/engram_doctor.py` checks nested helpers, pack scripts, and host
CLIs (python3 / yt-dlp blockers; ffmpeg, poppler, agent-reach, playwright,
gemini, pdf deps optional). `helpers/doctor/SKILL.md` wizards for WARN/FAIL
and mid-run helper failure (re-doctor → fix → resume). Detect-only for
agent-reach (Jung Phase-1 postmortem). Process note for `sources/url-cache`
fetch-once.

## 2.6.2 — hard-bind Phase 1 helpers (2026-09-04)

Mandatory Helper block in every Phase 1 agent prompt; per-agent helper
routing table; pre-Phase-1 checklist for `ENGRAM_PACK` + helpers present.
Reliable Nuwa-style “tell the swarm” with in-tree paths.

## 2.6.1 — English nested helpers (2026-09-04)

Translated `deep-research`, `web-article-reader`, and `pdf` SKILL.md to
English; Chinese originals kept as `SKILL.zh.md`. Quality gates: CJK < 2%,
heading/script parity, Engram path adaptations (no force ZH translation,
I1 on pdf).

## 2.6.0 — nested Phase-1 helpers (2026-09-04)

Vendored real helper skills under `helpers/` (skill-within-skill):
agent-reach, deep-research (huashu-research), gemini-video,
web-article-reader, pdf (huashu-md-html). Anthropic proprietary pdf
skill excluded (no redistribute).

## 2.5.6 — recommended Phase 1 helpers (2026-09-04)

Info-gathering skills reframed as recommended installs for max-quality
distills (not optional parity leftovers). Missing helper → tell the user
what to install; still never skip a ledger.

## 2.5.5 — machine-agnostic paths (2026-09-04)

Replaced host-specific skills-home paths with `<skills-root>/…`.

## 2.5.4 — source-policy wording (2026-09-04)

I1 stated as user-supplied / legal access only — without naming banned
sites.

## 2.5.3 — standalone voice (2026-09-04)

Removed third-party / upstream naming from the skill pack. Engram stands
alone in docs and runbook text.

## 2.5.2 — pure load-bearing text

Removed eval/history narrative from operational files.

## 2.5.1 — pure skill surface

Installable pack is CONSTITUTION + SKILL + references + scripts only.

## 2.5.0 — public packaging

MIT LICENSE, public README, semver VERSION, `.gitignore`.

## 2.0 — Engram

Mind-first default, Stage 8 = stakes, extracted phase refs, intentional
cuts I1–I4.
