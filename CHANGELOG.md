# Changelog — Engram

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
