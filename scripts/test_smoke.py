#!/usr/bin/env python3
"""Deterministic pack regression harness (Engram 2.7.8+).

    python3 scripts/test_smoke.py
    python3 scripts/test_smoke.py --pack <pack-root>

This suite asserts **deterministic** gates only; fidelity-scorecard /
Stage 8 stakes / synthesis quality are **non-deterministic judgment**
and are out of scope.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


SCRIPTS = (
    ("quality_check.py", ["--engram"]),
    ("merge_research.py", ["--engram"]),
    ("engram_doctor.py", ["--engram"]),
    ("phase1_gate.py", ["--engram"]),
    ("ax_gate.py", ["--engram"]),
)


def resolve_pack(argv: list[str] | None = None) -> Path:
    parser = argparse.ArgumentParser(
        description="Engram deterministic smoke suite (fixture only)"
    )
    parser.add_argument(
        "--pack",
        default=None,
        help="Engram pack root (default: parent of scripts/)",
    )
    args = parser.parse_args(argv)
    if args.pack:
        return Path(args.pack).expanduser().resolve()
    return Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    pack = resolve_pack(argv)
    scripts_dir = pack / "scripts"
    fixture = pack / "examples" / "minimal-fixture"
    if not fixture.is_dir():
        print(f"missing fixture: {fixture}", file=sys.stderr)
        return 1

    py = sys.executable or "python3"
    rows: list[tuple[str, int, str]] = []

    print(f"smoke: pack={pack}")
    print(f"smoke: fixture={fixture}")
    print()

    for name, flags in SCRIPTS:
        script = scripts_dir / name
        cmd = [py, str(script), *flags, str(fixture)]
        try:
            proc = subprocess.run(
                cmd,
                cwd=str(pack),
                capture_output=True,
                text=True,
            )
            code = proc.returncode
        except OSError as exc:
            print(f"FAILED to run {name}: {exc}", file=sys.stderr)
            code = 2
            proc = None  # type: ignore[assignment]

        status = "PASS" if code == 0 else "FAIL"
        rows.append((name, code, status))

        # Show child stdout/stderr briefly on failure for debugging
        if code != 0 and proc is not None:
            out = (proc.stdout or "") + (proc.stderr or "")
            for line in out.strip().splitlines()[-12:]:
                print(f"  | {line}")

    name_w = max(len(r[0]) for r in rows)
    print(f"{'script':<{name_w}}  exit  result")
    print(f"{'-' * name_w}  ----  ------")
    for name, code, status in rows:
        print(f"{name:<{name_w}}  {code:<4}  {status}")

    fails = sum(1 for _, code, _ in rows if code != 0)
    print()
    if fails:
        print(f"smoke: FAIL ({fails}/{len(rows)} scripts)")
        return 1
    print(f"smoke: PASS ({len(rows)}/{len(rows)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
