#!/bin/bash
# Download YouTube subtitles. Port of Nuwa scripts/download_subtitles.sh.
# Usage: ./download_subtitles.sh <YouTube_URL> [output-dir]
# Prefer manual subs. Language order: English, then Chinese, then whatever exists.
# Do not use this to fetch private / unlisted intimate recordings without consent.

set -e
URL="$1"
OUTPUT_DIR="${2:-.}"
if [ -z "$URL" ]; then
    echo "usage: ./download_subtitles.sh <YouTube_URL> [output-dir]"
    exit 1
fi
mkdir -p "$OUTPUT_DIR"
echo ">>> listing subs..."
yt-dlp --list-subs --no-download "$URL" 2>/dev/null | tail -20
echo ">>> trying manual English..."
if yt-dlp --write-subs --sub-langs "en,en-US,en-GB" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find "$OUTPUT_DIR" -name "*.srt" -mmin -1 2>/dev/null | head -1)
    if [ -n "$FOUND" ]; then echo "ok: $FOUND"; exit 0; fi
fi
echo ">>> trying manual Chinese..."
if yt-dlp --write-subs --sub-langs "zh-Hans,zh-Hant,zh,zh-CN,zh-TW" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find "$OUTPUT_DIR" -name "*.srt" -mmin -1 2>/dev/null | head -1)
    if [ -n "$FOUND" ]; then echo "ok: $FOUND"; exit 0; fi
fi
echo ">>> trying auto subs..."
if yt-dlp --write-auto-subs --sub-langs "en,zh-Hans,zh" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find "$OUTPUT_DIR" \( -name "*.srt" -o -name "*.vtt" \) | head -1)
    if [ -n "$FOUND" ]; then echo "ok auto: $FOUND"; exit 0; fi
fi
echo "no usable captions"
exit 1
