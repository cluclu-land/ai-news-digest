"""
ニュース収集モジュール (fetcher.py)
RSSフィードから最新のニュース記事を取得・整形する
"""

import datetime
from time import mktime
import feedparser
from bs4 import BeautifulSoup
from src.config import RSS_FEEDS, MAX_ARTICLES_PER_FEED


def clean_html(raw_html: str) -> str:
    """HTMLタグを除去してプレーンテキストにする"""
    if not raw_html:
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text(separator=" ", strip=True)


def parse_published_date(entry) -> datetime.datetime:
    """公開日時を取得・パースする"""
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        return datetime.datetime.fromtimestamp(mktime(entry.published_parsed))
    elif hasattr(entry, "updated_parsed") and entry.updated_parsed:
        return datetime.datetime.fromtimestamp(mktime(entry.updated_parsed))
    return datetime.datetime.now()


def fetch_latest_news() -> list[dict]:
    """設定されたすべてのRSSフィードから記事を収集する"""
    all_articles = []
    seen_links = set()

    for feed_info in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_info["url"])
            entries = feed.entries[:MAX_ARTICLES_PER_FEED]

            for entry in entries:
                link = entry.get("link", "").strip()
                if not link or link in seen_links:
                    continue
                seen_links.add(link)

                title = entry.get("title", "").strip()
                summary_raw = entry.get("summary", "") or entry.get("description", "")
                summary = clean_html(summary_raw)[:500]  # 先頭500文字程度
                published = parse_published_date(entry)

                all_articles.append(
                    {
                        "source": feed_info["name"],
                        "category": feed_info["category"],
                        "language": feed_info["language"],
                        "title": title,
                        "link": link,
                        "summary": summary,
                        "published": published,
                    }
                )
        except Exception as e:
            print(f"Error fetching {feed_info['name']}: {e}")

    # 公開日時の新しい順に並び替え
    all_articles.sort(key=lambda x: x["published"], reverse=True)
    return all_articles
