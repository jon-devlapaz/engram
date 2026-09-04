#!/bin/bash
# Download YouTube subtitles.
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
ERRLOG=$(mktemp)
MARKER=$(mktemp)
trap 'rm -f "$ERRLOG" "$MARKER"' EXIT
touch "$MARKER"

run_ytdlp() {
    if yt-dlp "$@" 2>"$ERRLOG"; then
        return 0
    fi
    echo "yt-dlp failed:" >&2
    cat "$ERRLOG" >&2
    return 1
}

find_new_subs() {
    # Duration-independent: anything newer than MARKER (not -mmin -1).
    find "$OUTPUT_DIR" \( -name "*.srt" -o -name "*.vtt" \) -newer "$MARKER" 2>/dev/null | head -1
}

echo ">>> listing subs..."
yt-dlp --list-subs --no-download "$URL" 2>"$ERRLOG" | tail -20 || {
    echo "yt-dlp --list-subs failed:" >&2
    cat "$ERRLOG" >&2
}
echo ">>> trying manual English..."
if run_ytdlp --write-subs --sub-langs "en,en-US,en-GB" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL"; then
    FOUND=$(find_new_subs)
    if [ -n "$FOUND" ]; then echo "ok: $FOUND"; exit 0; fi
fi
echo ">>> trying manual Chinese..."
if run_ytdlp --write-subs --sub-langs "zh-Hans,zh-Hant,zh,zh-CN,zh-TW" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL"; then
    FOUND=$(find_new_subs)
    if [ -n "$FOUND" ]; then echo "ok: $FOUND"; exit 0; fi
fi
echo ">>> trying auto subs..."
if run_ytdlp --write-auto-subs --sub-langs "en,zh-Hans,zh" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL"; then
    FOUND=$(find_new_subs)
    if [ -n "$FOUND" ]; then echo "ok auto: $FOUND"; exit 0; fi
fi
echo "no usable captions"
exit 1
