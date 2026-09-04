#!/usr/bin/env python3
"""Clean SRT/VTT to readable transcript.

    python3 srt_to_transcript.py input.srt [output.txt]
"""

import sys
import re
from pathlib import Path


def clean_srt(content: str) -> str:
    lines = content.strip().split("\n")
    texts = []
    for line in lines:
        line = line.strip()
        if re.match(r"^\d+$", line):
            continue
        if re.match(r"\d{2}:\d{2}:\d{2}", line):
            continue
        if not line:
            continue
        line = re.sub(r"<[^>]+>", "", line)
        line = re.sub(r"align:.*$|position:.*$", "", line).strip()
        if line:
            texts.append(line)
    deduped = []
    for text in texts:
        if not deduped or text != deduped[-1]:
            deduped.append(text)
    result = []
    current = []
    for text in deduped:
        current.append(text)
        joined = " ".join(current)
        if len(joined) > 200 or re.search(r"[。！？.!?]$", text):
            result.append(joined)
            current = []
    if current:
        result.append(" ".join(current))
    return "\n\n".join(result)


def clean_vtt(content: str) -> str:
    content = re.sub(r"^WEBVTT.*?\n\n", "", content, flags=re.DOTALL)
    content = re.sub(r"NOTE.*?\n\n", "", content, flags=re.DOTALL)
    return clean_srt(content)


def main():
    if len(sys.argv) < 2:
        print("usage: python3 srt_to_transcript.py <input.srt|input.vtt> [output.txt]")
        sys.exit(1)
    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"missing: {input_path}")
        sys.exit(1)
    output_path = Path(sys.argv[2]) if len(sys.argv) >= 3 else input_path.parent / f"{input_path.stem}_transcript.txt"
    content = input_path.read_text(encoding="utf-8")
    transcript = clean_vtt(content) if input_path.suffix.lower() == ".vtt" or content.startswith("WEBVTT") else clean_srt(content)
    output_path.write_text(transcript, encoding="utf-8")
    print(f"wrote {output_path}  chars={len(transcript)}")


if __name__ == "__main__":
    main()
