#!/usr/bin/env python3
"""
Scrape a tweet from X (Twitter) and save it as Markdown.

Uses fxtwitter API as the primary method (reliable, no auth needed).
Falls back to Playwright browser automation if the API fails.

Usage:
    python3 scrape_tweet.py <tweet_url> [output_dir]
"""

import json
import os
import re
import sys
import urllib.request
import urllib.error


def parse_tweet_url(url: str) -> tuple:
    """Extract screen_name and tweet_id from a tweet URL."""
    pattern = r"(?:twitter\.com|x\.com)/(\w+)/status/(\d+)"
    match = re.search(pattern, url)
    if not match:
        raise ValueError(f"Invalid tweet URL: {url}")
    return match.group(1), match.group(2)


def fetch_via_fxtwitter(screen_name: str, tweet_id: str) -> dict:
    """Fetch tweet data via fxtwitter API."""
    api_url = f"https://api.fxtwitter.com/{screen_name}/status/{tweet_id}"
    req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    tweet = data.get("tweet", {})
    author = tweet.get("author", {})

    # Extract article content blocks if present (long-form tweet / X article)
    article = tweet.get("article")
    full_text = ""
    if article and article.get("content"):
        blocks = article["content"].get("blocks", [])
        for block in blocks:
            text = block.get("text", "").strip()
            if not text or text == " ":
                continue
            # Check for time codes like "0:13" (video markers) - skip them
            if re.match(r"^\d+:\d+$", text):
                continue
            block_type = block.get("type", "unstyled")
            # Apply bold inline styles
            inline_styles = block.get("inlineStyleRanges", [])
            for style in sorted(inline_styles, key=lambda s: s["offset"], reverse=True):
                if style["style"] == "Bold":
                    start = style["offset"]
                    end = start + style["length"]
                    text = text[:start] + "**" + text[start:end] + "**" + text[end:]
            full_text += text + "\n\n"
    else:
        full_text = tweet.get("text", "") or tweet.get("raw_text", {}).get("text", "")

    # Extract image URLs
    images = []
    if article:
        for media in article.get("media_entities", []):
            info = media.get("media_info", {})
            img_url = info.get("original_img_url")
            if img_url:
                images.append(img_url)
        # Also check cover image
        cover = article.get("cover_media", {})
        cover_info = cover.get("media_info", {})
        cover_url = cover_info.get("original_img_url")
        if cover_url:
            images.insert(0, cover_url)

    return {
        "authorName": author.get("name", ""),
        "authorHandle": f"@{author.get('screen_name', '')}",
        "tweetText": full_text.strip(),
        "timestamp": tweet.get("created_at", ""),
        "articleTitle": article.get("title", "") if article else "",
        "images": images,
        "likes": str(tweet.get("likes", "")),
        "retweets": str(tweet.get("retweets", "")),
        "replies": str(tweet.get("replies", "")),
        "views": str(tweet.get("views", "")),
    }


def fetch_via_playwright(url: str) -> dict:
    """Fallback: use Playwright to scrape the tweet page."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"],
        )
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 900},
        )
        context.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"
        )
        page = context.new_page()

        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(8000)

        try:
            page.wait_for_selector('article[data-testid="tweet"]', timeout=20000)
        except Exception:
            page.wait_for_timeout(5000)

        tweet_data = page.evaluate("""() => {
            const articles = document.querySelectorAll('article[data-testid="tweet"]');
            if (!articles.length) return null;
            const tw = articles[0];
            const textEl = tw.querySelector('div[data-testid="tweetText"]');
            const timeEl = tw.querySelector('time');
            return {
                tweetText: textEl ? textEl.innerText : '',
                timestamp: timeEl ? (timeEl.getAttribute('datetime') || '') : '',
            };
        }""")

        browser.close()

        if not tweet_data or not tweet_data.get("tweetText"):
            return None
        return {
            "authorName": "",
            "authorHandle": "",
            "tweetText": tweet_data["tweetText"],
            "timestamp": tweet_data.get("timestamp", ""),
            "articleTitle": "",
            "images": [],
            "likes": "",
            "retweets": "",
            "replies": "",
            "views": "",
        }


def to_markdown(data: dict, url: str) -> str:
    """Convert extracted tweet data to Markdown format."""
    lines = []

    author = data.get("authorName") or "Unknown"
    handle = data.get("authorHandle") or ""
    timestamp = data.get("timestamp") or ""
    title = data.get("articleTitle") or ""

    # Title
    if title:
        lines.append(f"# {title}")
    elif handle:
        lines.append(f"# Tweet by {author} ({handle})")
    else:
        lines.append("# Tweet")
    lines.append("")

    # Meta info
    if author and handle:
        lines.append(f"**Author:** {author} ({handle})")
        lines.append("")
    if timestamp:
        lines.append(f"**Date:** {timestamp}")
        lines.append("")

    # Engagement
    metrics = []
    for key, label in [("likes", "Likes"), ("retweets", "Retweets"),
                        ("replies", "Replies"), ("views", "Views")]:
        val = data.get(key, "")
        if val and val != "0":
            metrics.append(f"**{label}:** {val}")
    if metrics:
        lines.append(" | ".join(metrics))
        lines.append("")

    lines.append(f"**Source:** [{url}]({url})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Tweet body
    lines.append(data.get("tweetText", ""))
    lines.append("")

    # Images
    images = data.get("images", [])
    if images:
        lines.append("---")
        lines.append("")
        lines.append("## Images")
        lines.append("")
        for i, img_url in enumerate(images, 1):
            lines.append(f"![Image {i}]({img_url})")
            lines.append("")

    return "\n".join(lines)


def sanitize_filename(title: str) -> str:
    """Make a safe filename from article title."""
    name = re.sub(r'[\\/:*?"<>|]', '', title)
    name = name.strip()
    if not name:
        name = "tweet"
    return name


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scrape_tweet.py <tweet_url> [output_dir]")
        sys.exit(1)

    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."

    screen_name, tweet_id = parse_tweet_url(url)
    data = None

    # Method 1: fxtwitter API
    print(f"Fetching tweet via fxtwitter API ({screen_name}/{tweet_id}) ...")
    try:
        data = fetch_via_fxtwitter(screen_name, tweet_id)
        print("Successfully fetched via API.")
    except Exception as e:
        print(f"API method failed: {e}")

    # Method 2: Playwright fallback
    if not data or not data.get("tweetText"):
        print("Trying Playwright fallback ...")
        try:
            data = fetch_via_playwright(url)
            if data:
                print("Successfully fetched via Playwright.")
            else:
                print("Playwright extraction returned no data.")
        except Exception as e:
            print(f"Playwright method failed: {e}")

    if not data or not data.get("tweetText"):
        print("ERROR: Could not extract tweet content via any method.")
        sys.exit(1)

    md_content = to_markdown(data, url)

    # Determine filename
    title = data.get("articleTitle") or f"Tweet by {data.get('authorName', 'Unknown')}"
    filename = sanitize_filename(title) + ".md"

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"\nTitle: {title}")
    print(f"Saved to: {output_path}")
    print(f"\n{'='*60}")
    print("Preview (first 600 chars):")
    print("=" * 60)
    print(md_content[:600])
    if len(md_content) > 600:
        print(f"\n... ({len(md_content)} total chars)")


if __name__ == "__main__":
    main()
