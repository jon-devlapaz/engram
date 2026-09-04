#!/usr/bin/env python3
"""Engram preflight doctor — pack helpers, scripts, and host CLIs.

Exit codes:
  0  no blocker failures
  1  one or more blocker failures
  2  doctor crashed
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any


HELPERS = (
    "gemini-video",
    "web-article-reader",
    "agent-reach",
    "deep-research",
    "pdf",
)

SCRIPTS = (
    "download_subtitles.sh",
    "srt_to_transcript.py",
    "merge_research.py",
)


def _which(name: str) -> str | None:
    return shutil.which(name)


def _can_import(mod: str) -> bool:
    return importlib.util.find_spec(mod) is not None


def check(
    *,
    id: str,
    title: str,
    status: str,
    severity: str,
    detail: str,
    wizard: str | None = None,
) -> dict[str, Any]:
    return {
        "id": id,
        "title": title,
        "status": status,
        "severity": severity,
        "detail": detail,
        "wizard": wizard,
    }


def resolve_pack(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()
    # Default: parent of scripts/ (this file lives in scripts/)
    return Path(__file__).resolve().parent.parent


def run_checks(pack: Path) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    # --- Pack helpers ---
    for name in HELPERS:
        skill = pack / "helpers" / name / "SKILL.md"
        if skill.is_file():
            checks.append(
                check(
                    id=f"helper-{name}",
                    title=f"Helper {name}/SKILL.md",
                    status="pass",
                    severity="blocker",
                    detail=str(skill),
                    wizard=None,
                )
            )
        else:
            checks.append(
                check(
                    id=f"helper-{name}",
                    title=f"Helper {name}/SKILL.md",
                    status="fail",
                    severity="blocker",
                    detail=f"Missing {skill} — pack incomplete",
                    wizard="reinstall-pack",
                )
            )

    # --- Pack scripts ---
    for name in SCRIPTS:
        path = pack / "scripts" / name
        if path.is_file():
            checks.append(
                check(
                    id=f"script-{name}",
                    title=f"Script {name}",
                    status="pass",
                    severity="blocker",
                    detail=str(path),
                    wizard=None,
                )
            )
        else:
            checks.append(
                check(
                    id=f"script-{name}",
                    title=f"Script {name}",
                    status="fail",
                    severity="blocker",
                    detail=f"Missing {path}",
                    wizard="reinstall-pack",
                )
            )

    # --- python3 (blocker) ---
    py = _which("python3")
    if py:
        checks.append(
            check(
                id="cli-python3",
                title="CLI python3",
                status="pass",
                severity="blocker",
                detail=py,
                wizard=None,
            )
        )
    else:
        checks.append(
            check(
                id="cli-python3",
                title="CLI python3",
                status="fail",
                severity="blocker",
                detail="python3 not on PATH",
                wizard="install-python",
            )
        )

    # --- yt-dlp (blocker) ---
    ytdlp = _which("yt-dlp")
    if ytdlp:
        checks.append(
            check(
                id="cli-yt-dlp",
                title="CLI yt-dlp",
                status="pass",
                severity="blocker",
                detail=ytdlp,
                wizard=None,
            )
        )
    else:
        checks.append(
            check(
                id="cli-yt-dlp",
                title="CLI yt-dlp",
                status="fail",
                severity="blocker",
                detail="yt-dlp not on PATH — YouTube captions / discover will fail",
                wizard="install-ytdlp",
            )
        )

    # --- ffmpeg (optional) ---
    ffmpeg = _which("ffmpeg")
    if ffmpeg:
        checks.append(
            check(
                id="cli-ffmpeg",
                title="CLI ffmpeg",
                status="pass",
                severity="optional",
                detail=ffmpeg,
                wizard=None,
            )
        )
    else:
        checks.append(
            check(
                id="cli-ffmpeg",
                title="CLI ffmpeg",
                status="warn",
                severity="optional",
                detail="ffmpeg not on PATH — some media paths may fail",
                wizard="install-ffmpeg",
            )
        )

    # --- pdftotext / poppler (optional) ---
    pdftotext = _which("pdftotext")
    if pdftotext:
        checks.append(
            check(
                id="cli-pdftotext",
                title="CLI pdftotext (poppler)",
                status="pass",
                severity="optional",
                detail=pdftotext,
                wizard=None,
            )
        )
    else:
        checks.append(
            check(
                id="cli-pdftotext",
                title="CLI pdftotext (poppler)",
                status="warn",
                severity="optional",
                detail="pdftotext not on PATH — install poppler for PDF text extract",
                wizard="install-poppler",
            )
        )

    # --- agent-reach CLI (optional warn) ---
    ar = _which("agent-reach")
    if ar:
        checks.append(
            check(
                id="cli-agent-reach",
                title="CLI agent-reach",
                status="pass",
                severity="optional",
                detail=ar,
                wizard=None,
            )
        )
    else:
        checks.append(
            check(
                id="cli-agent-reach",
                title="CLI agent-reach",
                status="warn",
                severity="optional",
                detail=(
                    "agent-reach not on PATH — helper SKILL.md still usable for "
                    "zero-config paths; full multi-backend needs install "
                    "(Jung Phase-1 postmortem: CLI/mcporter absent)"
                ),
                wizard="install-agent-reach",
            )
        )

    # --- playwright import or CLI (optional) ---
    pw_cli = _which("playwright")
    pw_mod = _can_import("playwright")
    if pw_mod or pw_cli:
        detail_parts = []
        if pw_mod:
            detail_parts.append("import playwright OK")
        if pw_cli:
            detail_parts.append(f"CLI {pw_cli}")
        checks.append(
            check(
                id="playwright",
                title="Playwright",
                status="pass",
                severity="optional",
                detail="; ".join(detail_parts),
                wizard=None,
            )
        )
    else:
        checks.append(
            check(
                id="playwright",
                title="Playwright",
                status="warn",
                severity="optional",
                detail="Neither playwright import nor CLI found — WeChat/fallback scrape may fail",
                wizard="install-playwright",
            )
        )

    # --- gemini SDK + API key (optional warn) ---
    has_genai = _can_import("google.genai")
    has_generativeai = _can_import("google.generativeai")
    # Prefer process env; also accept helpers/gemini-video/.env (local, gitignored)
    key_set = bool(os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"))
    env_file = pack / "helpers" / "gemini-video" / ".env"
    if not key_set and env_file.is_file():
        try:
            for line in env_file.read_text().splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, _, v = line.partition("=")
                if k.strip() in ("GEMINI_API_KEY", "GOOGLE_API_KEY") and v.strip():
                    key_set = True
                    break
        except OSError:
            pass
    sdk_ok = has_genai or has_generativeai
    if sdk_ok and key_set:
        sdk_name = "google.genai" if has_genai else "google.generativeai"
        if os.environ.get("GEMINI_API_KEY"):
            key_src = "GEMINI_API_KEY env"
        elif os.environ.get("GOOGLE_API_KEY"):
            key_src = "GOOGLE_API_KEY env"
        else:
            key_src = "helpers/gemini-video/.env"
        checks.append(
            check(
                id="gemini",
                title="Gemini SDK + API key",
                status="pass",
                severity="optional",
                detail=f"{sdk_name} import OK; key via {key_src} (value not shown)",
                wizard=None,
            )
        )
    else:
        parts = []
        if not sdk_ok:
            parts.append("neither google.genai nor google.generativeai importable")
        else:
            parts.append(
                "SDK OK ("
                + ("google.genai" if has_genai else "google.generativeai")
                + ")"
            )
        if not key_set:
            parts.append("GEMINI_API_KEY/GOOGLE_API_KEY unset")
        else:
            parts.append("API key env set (value not shown)")
        checks.append(
            check(
                id="gemini",
                title="Gemini SDK + API key",
                status="warn",
                severity="optional",
                detail="; ".join(parts)
                + " — local no-caption video path needs both (never paste keys into ledgers)",
                wizard="install-gemini-video",
            )
        )

    # --- pdf helper Python deps hint (info/optional when markitdown missing) ---
    has_markitdown = _can_import("markitdown")
    if has_markitdown:
        checks.append(
            check(
                id="pdf-python-deps",
                title="PDF helper Python deps",
                status="pass",
                severity="optional",
                detail="markitdown importable",
                wizard=None,
            )
        )
    else:
        checks.append(
            check(
                id="pdf-python-deps",
                title="PDF helper Python deps",
                status="warn",
                severity="optional",
                detail="markitdown not importable — pip -r helpers/pdf/requirements.txt when using pdf helper",
                wizard="install-pdf-deps",
            )
        )

    # --- url-cache process note (warn + wizard) ---
    checks.append(
        check(
            id="url-cache-process",
            title="URL cache process",
            status="warn",
            severity="info",
            detail=(
                "Prefer fetch-once into sources/url-cache/ for repeated URLs "
                "(enable-url-cache wizard). Not a host install check."
            ),
            wizard="enable-url-cache",
        )
    )

    return checks


def next_wizards(checks: list[dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for c in checks:
        if c["status"] in ("warn", "fail") and c.get("wizard"):
            w = c["wizard"]
            if w not in seen:
                seen.add(w)
                out.append(w)
    return out


def print_human(pack: Path, checks: list[dict[str, Any]], wizards: list[str]) -> None:
    print(f"Engram doctor — pack: {pack}")
    print()
    # Column widths
    rows = []
    for c in checks:
        rows.append(
            (
                c["status"].upper(),
                c["severity"],
                c["id"],
                c["title"],
                c["detail"][:90] + ("…" if len(c["detail"]) > 90 else ""),
                c["wizard"] or "—",
            )
        )
    headers = ("STATUS", "SEV", "ID", "TITLE", "DETAIL", "WIZARD")
    widths = [len(h) for h in headers]
    for r in rows:
        for i, cell in enumerate(r):
            widths[i] = max(widths[i], len(cell))

    def fmt(row: tuple[str, ...]) -> str:
        return "  ".join(cell.ljust(widths[i]) for i, cell in enumerate(row))

    print(fmt(headers))
    print(fmt(tuple("-" * w for w in widths)))
    for r in rows:
        print(fmt(r))
    print()
    blockers_failed = sum(
        1 for c in checks if c["severity"] == "blocker" and c["status"] == "fail"
    )
    warns = sum(1 for c in checks if c["status"] == "warn")
    print(f"Summary: blocker_fails={blockers_failed} warns={warns}")
    if wizards:
        print("next_wizards: " + ", ".join(wizards))
    else:
        print("next_wizards: (none)")
    print("Troubleshooting: helpers/doctor/SKILL.md")


def main(argv: list[str] | None = None) -> int:
    try:
        parser = argparse.ArgumentParser(description="Engram preflight doctor")
        parser.add_argument(
            "--json",
            action="store_true",
            help="Emit JSON report (includes next_wizards)",
        )
        parser.add_argument(
            "--pack",
            default=None,
            help="Engram pack root (default: parent of scripts/)",
        )
        args = parser.parse_args(argv)

        pack = resolve_pack(args.pack)
        checks = run_checks(pack)
        wizards = next_wizards(checks)

        if args.json:
            payload = {
                "pack": str(pack),
                "checks": checks,
                "next_wizards": wizards,
                "blocker_fails": sum(
                    1
                    for c in checks
                    if c["severity"] == "blocker" and c["status"] == "fail"
                ),
            }
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        else:
            print_human(pack, checks, wizards)

        if any(c["severity"] == "blocker" and c["status"] == "fail" for c in checks):
            return 1
        return 0
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 — doctor must never hang mid-run
        print(f"engram_doctor crashed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
