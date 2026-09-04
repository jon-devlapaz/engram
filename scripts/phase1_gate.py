#!/usr/bin/env python3
"""Phase 1 spawn gate — doctor blockers + engram url-cache preflight.

Exit codes:
  0  safe to spawn Phase 1 (doctor blockers clear + url-cache present)
  1  not safe (blocker_fails > 0 and/or url-cache missing)
  2  gate crashed
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path


def _load_doctor():
    doctor_path = Path(__file__).resolve().parent / "engram_doctor.py"
    spec = importlib.util.spec_from_file_location("engram_doctor", doctor_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load engram_doctor from {doctor_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(argv: list[str] | None = None) -> int:
    try:
        parser = argparse.ArgumentParser(
            description="Engram Phase 1 gate (doctor + url-cache)"
        )
        parser.add_argument(
            "--engram",
            required=True,
            help="Engram directory (must contain sources/url-cache/)",
        )
        parser.add_argument(
            "--pack",
            default=None,
            help="Engram pack root (default: parent of scripts/)",
        )
        parser.add_argument(
            "--mkdir-cache",
            action="store_true",
            help="Create <engram>/sources/url-cache/ if missing",
        )
        args = parser.parse_args(argv)

        engram = Path(args.engram).expanduser().resolve()
        if not engram.is_dir():
            print(f"FAIL: engram directory missing: {engram}", file=sys.stderr)
            print("phase1_gate: FAIL")
            return 1

        cache = engram / "sources" / "url-cache"
        cache_ok = cache.is_dir()
        if not cache_ok and args.mkdir_cache:
            cache.mkdir(parents=True, exist_ok=True)
            cache_ok = cache.is_dir()
            print(f"Created url-cache: {cache}")

        doctor = _load_doctor()
        pack = doctor.resolve_pack(args.pack)
        checks = doctor.run_checks(pack)
        wizards = doctor.next_wizards(checks)
        doctor.print_human(pack, checks, wizards)

        blocker_fails = sum(
            1 for c in checks if c["severity"] == "blocker" and c["status"] == "fail"
        )

        print()
        print(f"Engram: {engram}")
        if cache_ok:
            print(f"url-cache: PASS ({cache})")
        else:
            print(
                f"url-cache: FAIL (missing {cache}; pass --mkdir-cache to create)",
                file=sys.stderr,
            )

        safe = blocker_fails == 0 and cache_ok
        if safe:
            print("phase1_gate: PASS — safe to spawn Phase 1")
            return 0

        reasons = []
        if blocker_fails > 0:
            reasons.append(f"blocker_fails={blocker_fails}")
        if not cache_ok:
            reasons.append("url-cache missing")
        print(f"phase1_gate: FAIL — {'; '.join(reasons)}")
        return 1
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001
        print(f"phase1_gate crashed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
