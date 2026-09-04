# Engram nested helpers

Phase-1 info-gathering skills, vendored in-tree so one Engram install carries them.

| Folder | Job | Upstream |
|---|---|---|
| `gemini-video/` | local video → transcript | alex-tgk/saasaas `gemini-video-understanding` (MIT in skill header) |
| `web-article-reader/` | full article → markdown | maitty8879/Article-Reader |
| `agent-reach/` | multi-platform gather | Panniantong/Agent-Reach (MIT) |
| `deep-research/` | structured deep research | alchaincyf/huashu-skills `huashu-research` |
| `pdf/` | PDF/DOCX/EPUB/web → markdown | alchaincyf/huashu-md-html (MIT) |
| `doctor/` | preflight + troubleshooting wizards | Engram-authored (2.7.0) |

Each folder is a skill (`SKILL.md`). Phase 1 opens `helpers/<job>/SKILL.md` — no host skills-root scan required.

Anthropic’s proprietary document `pdf` skill is **not** included (redistribution forbidden).

See each `SOURCE.md` and `THIRD_PARTY.md`.

## Language

Procedure files (`SKILL.md`) are **English**. Where an upstream was Chinese,
the original is kept as `SKILL.zh.md` for provenance. Research corpus may
still be multilingual; helper *instructions* stay English for Engram.

## Preflight

Before Phase 1 (and after any mid-run helper failure):

```bash
python3 "$ENGRAM_PACK/scripts/engram_doctor.py"
python3 "$ENGRAM_PACK/scripts/engram_doctor.py" --json
```

Walk WARN/FAIL via `helpers/doctor/SKILL.md`. Doctor detects only — it does
not install host packages (especially not `agent-reach` without the user).
