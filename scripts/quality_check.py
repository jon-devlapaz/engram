#!/usr/bin/env python3
"""Phase 4 mechanical QA. Port of Nuwa scripts/quality_check.py.

    python3 quality_check.py <path-to-SKILL.md>
"""

import sys
import re
from pathlib import Path


def check_mental_models(content: str) -> tuple[bool, str]:
    models = re.findall(r"^###\s+(?:Model|Mental model|模型|心智模型)\s*\d", content, re.MULTILINE | re.IGNORECASE)
    if not models:
        in_section = False
        count = 0
        for line in content.split("\n"):
            if re.match(r"^##\s+.*(Mental Model|Core mental model|心智模型)", line, re.IGNORECASE):
                in_section = True
                continue
            if in_section and re.match(r"^##\s+", line) and "mental model" not in line.lower() and "心智模型" not in line:
                break
            if in_section and re.match(r"^###\s+", line):
                count += 1
        if count > 0:
            passed = 3 <= count <= 7
            return passed, f"{count} mental models {'PASS' if passed else 'FAIL (need 3-7)'}"
    count = len(models)
    if count == 0:
        return False, "no mental-model section detected"
    passed = 3 <= count <= 7
    return passed, f"{count} mental models {'PASS' if passed else 'FAIL (need 3-7)'}"


def check_limitations(content: str) -> tuple[bool, str]:
    has = bool(re.search(r"limit|fail|blind spot|does not apply|局限|失效|不适用|盲区", content, re.IGNORECASE))
    return has, "limitations labeled" if has else "FAIL no limitations"


def check_expression_dna(content: str) -> tuple[bool, str]:
    if not re.search(r"Expression DNA|voice rules|表达DNA|表达风格", content, re.IGNORECASE):
        return False, "FAIL no Expression DNA section"
    markers = len(re.findall(
        r"sentence|vocabular|diction|humor|pacing|certainty|citation|taboo|句式|词汇|语气|幽默|节奏|确定性|引用|口头禅",
        content, re.IGNORECASE,
    ))
    passed = markers >= 3
    return passed, f"expression DNA markers: {markers} {'PASS' if passed else 'FAIL (need >=3)'}"


def check_honest_boundary(content: str) -> tuple[bool, str]:
    m = re.search(
        r"(?:##\s+.*(?:Honest boundary|诚实边界))(.*?)(?=\n##\s|\Z)",
        content, re.DOTALL | re.IGNORECASE,
    )
    if not m:
        return False, "FAIL no Honest boundary section"
    items = re.findall(r"^[-*]\s+", m.group(1), re.MULTILINE)
    count = len(items)
    passed = count >= 3
    return passed, f"honest boundary: {count} {'PASS' if passed else 'FAIL (need >=3)'}"


def check_tensions(content: str) -> tuple[bool, str]:
    n = len(re.findall(r"tension|paradox|contradiction|unsettled|on the one hand|张力|矛盾", content, re.IGNORECASE))
    passed = n >= 2
    return passed, f"tensions: {n} {'PASS' if passed else 'FAIL (need >=2)'}"


def check_primary_sources(content: str) -> tuple[bool, str]:
    m = re.search(
        r"(?:##\s+.*(?:Source|Reference|来源))(.*?)(?=\n##\s|\Z)",
        content, re.DOTALL | re.IGNORECASE,
    )
    if not m:
        return True, "no sources section (skip)"
    text = m.group(1)
    primary = len(re.findall(r"primary|first-party|own writing|original|subject said|一手|本人|原文|原始|直接引用|本人著作", text, re.IGNORECASE))
    secondary = len(re.findall(r"secondary|second-hand|commentary|profile|witness said|according to|二手|转述|总结|评论|分析", text, re.IGNORECASE))
    total = primary + secondary
    if total == 0:
        return True, "source types unlabeled (skip)"
    ratio = primary / total
    passed = ratio > 0.5
    return passed, f"primary share: {primary}/{total} ({ratio:.0%}) {'PASS' if passed else 'FAIL (need >50%)'}"


def check_memory_file(skill_path: Path) -> tuple[bool, str]:
    memory = skill_path.parent / "MEMORY.md"
    if not memory.exists():
        return True, "no MEMORY.md (mind-only; skip engram check)"
    text = memory.read_text(encoding="utf-8")
    if re.search(r"I remember.*(childhood|that day)(?!.*source)", text, re.IGNORECASE):
        return False, "FAIL MEMORY.md looks narrated without traces"
    traces = len(re.findall(r"^###\s+TRACE-", text, re.MULTILINE))
    return True, f"MEMORY.md traces: {traces}"


def main():
    if len(sys.argv) < 2:
        print("usage: python3 quality_check.py <SKILL.md>")
        sys.exit(1)
    skill_path = Path(sys.argv[1])
    if not skill_path.exists():
        print(f"missing: {skill_path}")
        sys.exit(1)
    content = skill_path.read_text(encoding="utf-8")
    checks = [
        ("mental model count", check_mental_models),
        ("model limitations", check_limitations),
        ("expression DNA", check_expression_dna),
        ("honest boundary", check_honest_boundary),
        ("tensions", check_tensions),
        ("primary sources", check_primary_sources),
    ]
    print(f"quality check: {skill_path}")
    print("=" * 50)
    passed_count = 0
    for name, fn in checks:
        ok, detail = fn(content)
        print(f"  {name:<22} {'PASS' if ok else 'FAIL'}  {detail}")
        if ok:
            passed_count += 1
    ok_m, detail_m = check_memory_file(skill_path)
    print(f"  {'memory store':<22} {'PASS' if ok_m else 'FAIL'}  {detail_m}")
    if ok_m:
        passed_count += 1
    total = len(checks) + 1
    print("=" * 50)
    print(f"result: {passed_count}/{total}")
    sys.exit(0 if passed_count == total else 1)


if __name__ == "__main__":
    main()
