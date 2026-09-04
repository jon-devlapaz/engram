#!/usr/bin/env python3
"""
Fetch a WeChat article and save it as clean Markdown.
Uses Playwright to render the page and extract content.

Usage:
    python3 fetch_wechat.py <article_url> [output_dir]
"""

import os
import re
import sys
from playwright.sync_api import sync_playwright


def fetch_article(url: str) -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"],
        )
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
                "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                "Version/17.0 Mobile/15E148 Safari/604.1"
            ),
            viewport={"width": 390, "height": 844},
            locale="zh-CN",
        )
        page = context.new_page()

        print(f"Opening {url} ...")
        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        # Wait for content to render
        try:
            page.wait_for_selector("#js_content", timeout=15000)
            print("Article content loaded.")
        except Exception:
            print("Waiting extra time for content...")
            page.wait_for_timeout(5000)

        # Extract article data
        data = page.evaluate("""() => {
            const title = document.querySelector('#activity-name')?.textContent?.trim() ||
                          document.querySelector('h1')?.textContent?.trim() || '';

            const author = document.querySelector('#js_name')?.textContent?.trim() ||
                           document.querySelector('.rich_media_meta_nickname')?.textContent?.trim() || '';

            const publishDate = document.querySelector('#publish_time')?.textContent?.trim() ||
                                document.querySelector('.rich_media_meta_text')?.textContent?.trim() || '';

            const contentEl = document.querySelector('#js_content');
            if (!contentEl) return { title, author, publishDate, html: '', text: '' };

            return {
                title,
                author,
                publishDate,
                html: contentEl.innerHTML,
                text: contentEl.innerText,
            };
        }""")

        # Also extract structured content with formatting
        md_content = page.evaluate("""() => {
            const content = document.querySelector('#js_content');
            if (!content) return '';

            function nodeToMd(node, depth) {
                if (node.nodeType === Node.TEXT_NODE) {
                    return node.textContent;
                }
                if (node.nodeType !== Node.ELEMENT_NODE) return '';

                const tag = node.tagName.toLowerCase();
                const style = window.getComputedStyle(node);
                const display = style.display;

                // Skip hidden elements
                if (display === 'none' || style.visibility === 'hidden') return '';

                // Images
                if (tag === 'img') {
                    const src = node.getAttribute('data-src') || node.getAttribute('src') || '';
                    const alt = node.getAttribute('alt') || '';
                    if (src) return '\\n\\n![' + alt + '](' + src + ')\\n\\n';
                    return '';
                }

                // Line breaks
                if (tag === 'br') return '\\n';

                // Links
                if (tag === 'a') {
                    const href = node.getAttribute('href') || '';
                    const text = node.textContent.trim();
                    if (href && text && !href.startsWith('javascript:')) {
                        return '[' + text + '](' + href + ')';
                    }
                    return text;
                }

                // Collect children
                let children = '';
                for (const child of node.childNodes) {
                    children += nodeToMd(child, depth + 1);
                }

                // Headings
                if (/^h[1-6]$/.test(tag)) {
                    const level = parseInt(tag[1]);
                    const prefix = '#'.repeat(level) + ' ';
                    return '\\n\\n' + prefix + children.trim() + '\\n\\n';
                }

                // Bold
                if (tag === 'strong' || tag === 'b') {
                    const text = children.trim();
                    if (text) return '**' + text + '**';
                    return '';
                }

                // Italic
                if (tag === 'em' || tag === 'i') {
                    const text = children.trim();
                    if (text) return '*' + text + '*';
                    return '';
                }

                // Blockquote
                if (tag === 'blockquote') {
                    const lines = children.trim().split('\\n');
                    return '\\n\\n' + lines.map(l => '> ' + l).join('\\n') + '\\n\\n';
                }

                // Code
                if (tag === 'code') {
                    return '`' + children + '`';
                }
                if (tag === 'pre') {
                    return '\\n\\n```\\n' + children.trim() + '\\n```\\n\\n';
                }

                // Lists
                if (tag === 'ul' || tag === 'ol') {
                    return '\\n' + children + '\\n';
                }
                if (tag === 'li') {
                    return '- ' + children.trim() + '\\n';
                }

                // Block elements - add line breaks
                if (['p', 'div', 'section', 'article'].includes(tag)) {
                    const text = children.trim();
                    if (text) return '\\n\\n' + text + '\\n\\n';
                    return '';
                }

                return children;
            }

            return nodeToMd(content, 0);
        }""")

        browser.close()

        data["markdown"] = md_content
        return data


def clean_markdown(raw: str) -> str:
    """Clean up the raw markdown output."""
    # Collapse multiple blank lines to max 2
    text = re.sub(r'\n{3,}', '\n\n', raw)
    # Remove leading/trailing whitespace per line
    lines = [line.rstrip() for line in text.split('\n')]
    text = '\n'.join(lines)
    return text.strip()


def sanitize_filename(title: str) -> str:
    """Make a safe filename from article title."""
    name = re.sub(r'[\\/:*?"<>|]', '', title)
    name = name.strip()
    if not name:
        name = "untitled"
    return name


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_wechat.py <article_url> [output_dir]")
        sys.exit(1)

    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."

    data = fetch_article(url)

    title = data.get("title", "").strip()
    author = data.get("author", "").strip()
    pub_date = data.get("publishDate", "").strip()
    md_body = data.get("markdown", "").strip()

    if not md_body:
        # Fallback to plain text
        md_body = data.get("text", "").strip()

    if not md_body:
        print("ERROR: Could not extract article content.")
        sys.exit(1)

    md_body = clean_markdown(md_body)

    # Build final markdown
    lines = []
    lines.append(f"# {title}" if title else "# Untitled Article")
    lines.append("")
    if author:
        lines.append(f"**Author:** {author}")
        lines.append("")
    if pub_date:
        lines.append(f"**Date:** {pub_date}")
        lines.append("")
    lines.append(f"**Source:** [{url}]({url})")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(md_body)
    lines.append("")

    final_md = '\n'.join(lines)

    # Save
    os.makedirs(output_dir, exist_ok=True)
    filename = sanitize_filename(title if title else "untitled") + ".md"
    output_path = os.path.join(output_dir, filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_md)

    print(f"\nTitle: {title}")
    print(f"Author: {author}")
    print(f"Saved to: {output_path}")
    print(f"\n{'='*60}")
    print("Preview (first 800 chars):")
    print("=" * 60)
    print(final_md[:800])
    if len(final_md) > 800:
        print(f"\n... ({len(final_md)} total chars)")


if __name__ == "__main__":
    main()
