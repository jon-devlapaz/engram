#!/usr/bin/env python3
"""Engram AX quality gate suite (hill-climb 2.7.6).

Exit codes:
  0  all checks PASS (warns allowed)
  1  one or more FAIL
  2  gate crashed
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any


def _row(
    *,
    id: str,
    title: str,
    status: str,
    detail: str,
) -> dict[str, Any]:
    return {"id": id, "title": title, "status": status, "detail": detail}


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        return f"__READ_ERROR__:{exc}"


def check_pack(pack: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    skill = pack / "SKILL.md"
    skill_text = _read(skill) if skill.is_file() else ""

    # A. ax-ops.md
    ax_ops = pack / "references" / "ax-ops.md"
    if ax_ops.is_file():
        rows.append(
            _row(
                id="A",
                title="references/ax-ops.md exists",
                status="pass",
                detail=str(ax_ops),
            )
        )
    else:
        rows.append(
            _row(
                id="A",
                title="references/ax-ops.md exists",
                status="fail",
                detail=f"missing {ax_ops}",
            )
        )

    # B. checkpoint verbs approve / revise / stop for 1.5 and 2.5
    if skill.is_file():
        has_verbs = all(
            re.search(rf"\b{v}\b", skill_text, re.IGNORECASE)
            for v in ("approve", "revise", "stop")
        )
        # Prefer section presence near checkpoints
        has_15 = bool(
            re.search(
                r"Phase 1\.5.*?(?:approve|revise|stop)",
                skill_text,
                re.IGNORECASE | re.DOTALL,
            )
        )
        has_25 = bool(
            re.search(
                r"Phase 2\.5.*?(?:approve|revise|stop)",
                skill_text,
                re.IGNORECASE | re.DOTALL,
            )
        )
        # Also accept explicit hard-verb language near both checkpoints
        hard = bool(
            re.search(
                r"approve\s*\|\s*revise\s*\|\s*stop",
                skill_text,
                re.IGNORECASE,
            )
        )
        ok = has_verbs and (hard or (has_15 and has_25))
        rows.append(
            _row(
                id="B",
                title="SKILL checkpoint verbs approve/revise/stop",
                status="pass" if ok else "fail",
                detail=(
                    f"verbs={has_verbs} hard={hard} near_1.5={has_15} near_2.5={has_25}"
                    if skill.is_file()
                    else "SKILL.md missing"
                ),
            )
        )
    else:
        rows.append(
            _row(
                id="B",
                title="SKILL checkpoint verbs approve/revise/stop",
                status="fail",
                detail=f"missing {skill}",
            )
        )

    # C. STATUS.md requirement + AX beat language
    if skill.is_file():
        has_status = bool(re.search(r"STATUS\.md", skill_text))
        has_ax_beat = bool(
            re.search(r"AX\s+beat", skill_text, re.IGNORECASE)
        )
        ok = has_status and has_ax_beat
        rows.append(
            _row(
                id="C",
                title="SKILL STATUS.md + AX beat language",
                status="pass" if ok else "fail",
                detail=f"STATUS.md={has_status} AX beat={has_ax_beat}",
            )
        )
    else:
        rows.append(
            _row(
                id="C",
                title="SKILL STATUS.md + AX beat language",
                status="fail",
                detail="SKILL.md missing",
            )
        )

    # D. machine-down / host-session reconnect language (host-neutral)
    if skill.is_file():
        has_md = bool(
            re.search(r"machine[- ]down", skill_text, re.IGNORECASE)
        )
        has_reconnect = bool(
            re.search(
                r"reconnect|ListMachines|host session|user chat|Shell unavailable",
                skill_text,
                re.IGNORECASE,
            )
        )
        ok = has_md and has_reconnect
        rows.append(
            _row(
                id="D",
                title="SKILL machine-down / reconnect language",
                status="pass" if ok else "fail",
                detail=(
                    f"machine-down={has_md} "
                    f"reconnect/host-session={has_reconnect}"
                ),
            )
        )
    else:
        rows.append(
            _row(
                id="D",
                title="SKILL machine-down / reconnect language",
                status="fail",
                detail="SKILL.md missing",
            )
        )

    # E. phase1_gate.py
    p1 = pack / "scripts" / "phase1_gate.py"
    if p1.is_file():
        rows.append(
            _row(
                id="E",
                title="scripts/phase1_gate.py exists",
                status="pass",
                detail=str(p1),
            )
        )
    else:
        rows.append(
            _row(
                id="E",
                title="scripts/phase1_gate.py exists",
                status="fail",
                detail=f"missing {p1}",
            )
        )

    return rows


def _has_status_keys(text: str) -> tuple[bool, str]:
    """Require phase, fidelity, stakes, gate (heading or key: value)."""
    required = ("phase", "fidelity", "stakes", "gate")
    found = []
    missing = []
    for key in required:
        # Match markdown heading or key: value (case-insensitive)
        pat = rf"(?:^#+\s*{key}\b|^[-*]\s*{key}\s*:|^{key}\s*:)"
        if re.search(pat, text, re.IGNORECASE | re.MULTILINE):
            found.append(key)
        else:
            missing.append(key)
    ok = not missing
    return ok, f"found={found} missing={missing}"


def _captcha_stub_hits(articles: Path) -> list[Path]:
    hits: list[Path] = []
    if not articles.is_dir():
        return hits
    patterns = (
        re.compile(r"Robot Challenge", re.IGNORECASE),
        re.compile(r"CAPTCHA", re.IGNORECASE),
        re.compile(r"maybe requiring CAPTCHA", re.IGNORECASE),
        re.compile(r"Performing security verification", re.IGNORECASE),
        re.compile(r"Just a moment\.\.\.", re.IGNORECASE),
    )
    for path in sorted(articles.glob("*.md")):
        try:
            head = path.read_text(encoding="utf-8", errors="replace")[:4000]
        except OSError:
            continue
        if any(p.search(head) for p in patterns):
            hits.append(path)
    return hits


def check_engram(engram: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    # F. STATUS.md keys
    status = engram / "STATUS.md"
    if status.is_file():
        text = _read(status)
        ok, detail = _has_status_keys(text)
        rows.append(
            _row(
                id="F",
                title="STATUS.md phase/fidelity/stakes/gate",
                status="pass" if ok else "fail",
                detail=detail,
            )
        )
    else:
        rows.append(
            _row(
                id="F",
                title="STATUS.md phase/fidelity/stakes/gate",
                status="fail",
                detail=f"missing {status}",
            )
        )

    # G. sources/INDEX.md
    index = engram / "sources" / "INDEX.md"
    if index.is_file():
        rows.append(
            _row(
                id="G",
                title="sources/INDEX.md exists",
                status="pass",
                detail=str(index),
            )
        )
    else:
        rows.append(
            _row(
                id="G",
                title="sources/INDEX.md exists",
                status="fail",
                detail=f"missing {index}",
            )
        )

    # H. No CAPTCHA stubs under sources/articles/
    articles = engram / "sources" / "articles"
    hits = _captcha_stub_hits(articles)
    if hits:
        rows.append(
            _row(
                id="H",
                title="No CAPTCHA stubs under articles/",
                status="fail",
                detail="stubs still in articles/: "
                + ", ".join(p.name for p in hits),
            )
        )
    else:
        rows.append(
            _row(
                id="H",
                title="No CAPTCHA stubs under articles/",
                status="pass",
                detail="none under sources/articles/ (quarantine → sources/stubs/)",
            )
        )

    # I. url-cache — FAIL missing dir; empty OK/WARN at 0.5; FAIL empty post-gather
    cache = engram / "sources" / "url-cache"
    md = sorted(cache.glob("*.md")) if cache.is_dir() else []
    phase_val = ""
    status_path = engram / "STATUS.md"
    if status_path.is_file():
        st = _read(status_path)
        if not st.startswith("__READ_ERROR__"):
            m = re.search(
                r"(?:^|\n)\s*[-*]?\s*phase\s*:\s*(.+)$",
                st,
                re.IGNORECASE | re.MULTILINE,
            )
            if m:
                phase_val = m.group(1).strip()
            else:
                m2 = re.search(
                    r"^#+\s*phase\b\s*(.*)$",
                    st,
                    re.IGNORECASE | re.MULTILINE,
                )
                if m2:
                    phase_val = m2.group(1).strip()
    # Post-gather if phase value mentions 1.5 / Phase 2+ / G* milestones
    post_gather = bool(
        re.search(
            r"(?:1\.5|\b2\.5\b|\bPhase\s*[1234]\b|\b[234]\b|\bG\d*\b|post-gather|G7|G8)",
            phase_val,
            re.IGNORECASE,
        )
    )
    # Explicit early phases win over loose digit matches
    if re.search(r"^(?:0(?:\.5)?|pre-phase-1|pre-research)\b", phase_val, re.IGNORECASE):
        post_gather = False
    pre_or_unset = (not phase_val) or bool(
        re.search(
            r"^(?:0(?:\.5)?|pre-phase-1|pre-research)\b",
            phase_val,
            re.IGNORECASE,
        )
    )

    if not cache.is_dir():
        rows.append(
            _row(
                id="I",
                title="sources/url-cache present",
                status="fail",
                detail=f"missing directory: {cache}",
            )
        )
    elif md:
        rows.append(
            _row(
                id="I",
                title="sources/url-cache nonempty",
                status="pass",
                detail=f"{len(md)} *.md",
            )
        )
    elif post_gather and not pre_or_unset:
        rows.append(
            _row(
                id="I",
                title="sources/url-cache nonempty",
                status="fail",
                detail=f"empty after Phase 1.5+/post-gather (phase={phase_val!r}): {cache}",
            )
        )
    else:
        rows.append(
            _row(
                id="I",
                title="sources/url-cache nonempty",
                status="warn",
                detail="empty OK at 0.5 / pre-research (dir exists)",
            )
        )

    # J. AX-EVAL.md optional warn
    ax_eval = engram / "references" / "AX-EVAL.md"
    if ax_eval.is_file():
        rows.append(
            _row(
                id="J",
                title="references/AX-EVAL.md (optional)",
                status="pass",
                detail=str(ax_eval),
            )
        )
    else:
        rows.append(
            _row(
                id="J",
                title="references/AX-EVAL.md (optional)",
                status="warn",
                detail=f"missing {ax_eval} (warn only)",
            )
        )

    return rows


def print_table(rows: list[dict[str, Any]]) -> None:
    headers = ("STATUS", "ID", "TITLE", "DETAIL")
    data = [
        (
            r["status"].upper(),
            r["id"],
            r["title"],
            r["detail"][:100] + ("…" if len(r["detail"]) > 100 else ""),
        )
        for r in rows
    ]
    widths = [len(h) for h in headers]
    for row in data:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    def fmt(row: tuple[str, ...]) -> str:
        return "  ".join(cell.ljust(widths[i]) for i, cell in enumerate(row))

    print(fmt(headers))
    print(fmt(tuple("-" * w for w in widths)))
    for row in data:
        print(fmt(row))


def resolve_pack(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()
    return Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    try:
        parser = argparse.ArgumentParser(
            description="Engram AX quality gate (2.7.6)"
        )
        parser.add_argument(
            "--pack",
            default=None,
            help="Engram pack root (default: parent of scripts/)",
        )
        parser.add_argument(
            "--engram",
            default=None,
            help="Optional engram directory for checks F–J",
        )
        args = parser.parse_args(argv)

        pack = resolve_pack(args.pack)
        rows = check_pack(pack)

        engram: Path | None = None
        if args.engram:
            engram = Path(args.engram).expanduser().resolve()
            if not engram.is_dir():
                print(f"FAIL: engram directory missing: {engram}", file=sys.stderr)
                print("ax_gate: FAIL")
                return 1
            rows.extend(check_engram(engram))

        print(f"Engram AX gate — pack: {pack}")
        if engram:
            print(f"Engram: {engram}")
        print()
        print_table(rows)
        print()

        fails = sum(1 for r in rows if r["status"] == "fail")
        warns = sum(1 for r in rows if r["status"] == "warn")
        passes = sum(1 for r in rows if r["status"] == "pass")
        print(f"Summary: pass={passes} warn={warns} fail={fails}")

        if fails:
            print("ax_gate: FAIL")
            return 1
        print("ax_gate: PASS")
        return 0
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001
        print(f"ax_gate crashed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
