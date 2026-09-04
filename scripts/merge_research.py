#!/usr/bin/env python3
"""Phase 1.5 research review table.

    python3 merge_research.py <engram-directory>

Scans references/research/01-06 (required) and 07-intimate (optional).
"""

import sys
import re
from pathlib import Path

AGENTS = {
    "01-writings": "writings",
    "02-conversations": "conversations",
    "03-expression-dna": "expression",
    "04-external-views": "external views",
    "05-decisions": "decisions",
    "06-timeline": "timeline",
    "07-intimate": "intimate",
}


def count_sources(content: str) -> dict:
    urls = re.findall(r"https?://[^\s\)]+", content)
    primary = len(re.findall(r"primary|first-party|subject said|own writing|original|一手|本人|原文|原始|直接引用", content, re.IGNORECASE))
    secondary = len(re.findall(r"secondary|witness said|commentary|profile|according to|二手|转述|总结|评论|分析", content, re.IGNORECASE))
    return {
        "url_count": len(urls),
        "unique_urls": len(set(urls)),
        "primary_markers": primary,
        "secondary_markers": secondary,
    }


def extract_key_findings(content: str, max_items: int = 3) -> list[str]:
    headings = re.findall(r"^##\s+(.+)$", content, re.MULTILINE)
    if headings:
        return headings[:max_items]
    bolds = re.findall(r"\*\*(.+?)\*\*", content)
    if bolds:
        return bolds[:max_items]
    lines = [l.strip() for l in content.split("\n") if l.strip() and not l.startswith("#")]
    return [l[:50] + "..." if len(l) > 50 else l for l in lines[:max_items]]


def find_contradictions(files: dict[str, str]) -> list[str]:
    out = []
    for name, content in files.items():
        matches = re.findall(r"(?:contradiction|however|but in fact|dispute|tension|矛盾|相反|但实际上|争议).{0,100}", content, re.IGNORECASE)
        for m in matches:
            out.append(f"{AGENTS.get(name, name)}: {m[:80]}")
    return out[:5]


def main():
    if len(sys.argv) < 2:
        print("usage: python3 merge_research.py <engram-directory>")
        sys.exit(1)
    skill_dir = Path(sys.argv[1])
    research_dir = skill_dir / "references" / "research"
    if not research_dir.exists():
        print(f"missing: {research_dir}")
        sys.exit(1)

    files = {}
    rows = []
    total_sources = 0
    total_primary = 0
    total_secondary = 0
    missing = []

    for key, label in AGENTS.items():
        md_file = research_dir / f"{key}.md"
        optional = key == "07-intimate"
        if not md_file.exists():
            if optional:
                rows.append(f"| {label:<16} | skipped          | no intimate corpus |")
            else:
                missing.append(label)
                rows.append(f"| {label:<16} | MISSING          | — |")
            continue
        content = md_file.read_text(encoding="utf-8")
        files[key] = content
        stats = count_sources(content)
        findings = extract_key_findings(content)
        total_sources += stats["unique_urls"]
        total_primary += stats["primary_markers"]
        total_secondary += stats["secondary_markers"]
        findings_str = ", ".join(findings) if findings else "—"
        if len(findings_str) > 40:
            findings_str = findings_str[:37] + "..."
        rows.append(f"| {label:<16} | {stats['unique_urls']:<16} | {findings_str} |")

    contradictions = find_contradictions(files)
    print("| ledger           | unique URLs      | key findings |")
    print("|------------------|------------------|--------------|")
    for row in rows:
        print(row)
    ratio = f"{total_primary}/{total_primary + total_secondary}" if (total_primary + total_secondary) else "unlabeled"
    print(f"| total            | {total_sources:<16} | primary markers: {ratio} |")
    print(f"| contradictions   | {len(contradictions):<16} | {(contradictions[0][:40] if contradictions else '—')} |")
    print(f"| thin ledgers     | {len(missing):<16} | {', '.join(missing) or 'none'} |")
    if total_sources < 10:
        print("\nWARN total unique URLs < 10 — lower the ceiling or keep researching")
    if missing:
        print(f"\nWARN missing required ledgers: {', '.join(missing)}")


if __name__ == "__main__":
    main()
