"""
設定ファイル: RSSフィード一覧や取得件数などの設定
"""

# RSSフィード一覧
RSS_FEEDS = [
    {
        "name": "OpenAI News",
        "url": "https://openai.com/news/rss.xml",
        "category": "公式発表",
        "language": "en",
    },
    {
        "name": "Google AI Blog",
        "url": "https://blog.google/technology/ai/rss/",
        "category": "公式発表",
        "language": "en",
    },
    {
        "name": "TechCrunch AI",
        "url": "https://techcrunch.com/category/artificial-intelligence/feed/",
        "category": "海外メディア",
        "language": "en",
    },
    {
        "name": "The Verge AI",
        "url": "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml",
        "category": "海外メディア",
        "language": "en",
    },
    {
        "name": "ITmedia AI+",
        "url": "https://rss.itmedia.co.jp/rss/2.0/aiplus.xml",
        "category": "国内メディア",
        "language": "ja",
    },
]

# 各フィードから取得する最大件数
MAX_ARTICLES_PER_FEED = 5

# 最終的に要約・表示する厳選記事の上限（朝サクッと読める5〜8本程度）
MAX_TOTAL_ARTICLES = 7

# 使用するGeminiモデル名（無料枠で高速・安定動作するモデル）
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-1.5-flash"
