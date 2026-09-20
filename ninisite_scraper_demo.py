# -*- coding: utf-8 -*-
"""
Ninisite Discussion Scraper — Public Portfolio Version

Demonstrates the architecture of a Playwright-based pipeline for collecting
and structuring Persian online discussions.

IMPORTANT:
- No credentials are included.
- Production-specific selectors and extraction rules are intentionally omitted.
- Use responsibly and comply with applicable website terms and privacy rules.
"""

from __future__ import annotations

import os
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

import pandas as pd
from playwright.sync_api import sync_playwright


BASE_URL = "https://www.ninisite.com"
SEARCH_URL = BASE_URL + "/search?q={query}&page={page}"
KEYWORD = os.getenv("NINISITE_KEYWORD", "sample keyword")
MAX_SEARCH_PAGES = int(os.getenv("MAX_SEARCH_PAGES", "3"))
OUTPUT_DIR = Path(__file__).resolve().parent / "output"

COLUMNS = [
    "search_query",
    "topic_title",
    "topic_url",
    "post_type",
    "post_id",
    "username",
    "published_at",
    "text",
    "scraped_at",
]


def clean_text(value: str | None) -> str:
    """Normalize whitespace while preserving Persian/Unicode text."""
    return re.sub(r"\s+", " ", str(value or "").replace("\u200c", " ")).strip()


def discover_topics(page, keyword: str) -> list[dict]:
    """
    Discover discussion URLs from search-result pages.

    The public version keeps the overall workflow visible while omitting
    production-specific discovery rules.
    """
    topics, seen = [], set()

    for page_no in range(1, MAX_SEARCH_PAGES + 1):
        url = SEARCH_URL.format(query=quote(keyword), page=page_no)
        page.goto(url, wait_until="domcontentloaded", timeout=60_000)

        # Generic portfolio example. Production discovery logic is omitted.
        links = page.locator('a[href*="/discussion/topic/"]').evaluate_all(
            """els => els.map(a => ({
                href: a.href,
                title: (a.innerText || '').trim()
            }))"""
        )

        for item in links:
            href = (item.get("href") or "").split("#", 1)[0].split("?", 1)[0]
            if not href or href in seen:
                continue
            seen.add(href)
            topics.append(
                {
                    "topic_title": clean_text(item.get("title")) or "Untitled",
                    "topic_url": href,
                    "search_page": page_no,
                }
            )

    return topics


def extract_posts(page, topic: dict) -> list[dict]:
    """
    Extract structured posts/comments from one discussion.

    Production-specific DOM selectors and extraction rules are intentionally
    omitted from this public portfolio version.
    """
    # Replace this demo block with site-specific extraction logic in a private
    # implementation. Returning an empty list keeps the public demo safe.
    return []


def build_dataset(page, topics: list[dict], keyword: str) -> pd.DataFrame:
    """Run extraction and return a normalized tabular dataset."""
    rows = []

    for topic in topics:
        page.goto(topic["topic_url"], wait_until="domcontentloaded", timeout=60_000)

        for post in extract_posts(page, topic):
            rows.append(
                {
                    "search_query": keyword,
                    "topic_title": topic["topic_title"],
                    "topic_url": topic["topic_url"],
                    "post_type": post.get("post_type", ""),
                    "post_id": post.get("post_id", ""),
                    "username": clean_text(post.get("username")),
                    "published_at": clean_text(post.get("published_at")),
                    "text": clean_text(post.get("text")),
                    "scraped_at": datetime.now().isoformat(timespec="seconds"),
                }
            )

    return pd.DataFrame(rows, columns=COLUMNS)


def save_dataset(df: pd.DataFrame) -> None:
    """Export structured results to CSV and Excel."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    df.to_csv(OUTPUT_DIR / "discussions.csv", index=False, encoding="utf-8-sig")
    df.to_excel(OUTPUT_DIR / "discussions.xlsx", index=False)


def main() -> None:
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=True)
        context = browser.new_context(locale="fa-IR")
        page = context.new_page()

        try:
            topics = discover_topics(page, KEYWORD)
            dataset = build_dataset(page, topics, KEYWORD)
            save_dataset(dataset)
            print(f"Discovered topics: {len(topics)}")
            print(f"Extracted records: {len(dataset)}")
        finally:
            context.close()
            browser.close()


if __name__ == "__main__":
    main()
