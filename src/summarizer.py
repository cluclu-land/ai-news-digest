"""
AI要約モジュール (summarizer.py)
Google Gemini APIを使用して、ニュース記事を日本語で構造化要約する
"""

import json
import os
from google import genai
from google.genai import types
from src.config import GEMINI_MODEL, GEMINI_FALLBACK_MODEL, MAX_TOTAL_ARTICLES


def create_gemini_client():
    """Gemini APIクライアントを生成する"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("環境変数 GEMINI_API_KEY が設定されていません。")
    return genai.Client(api_key=api_key)


def summarize_articles(articles: list[dict]) -> list[dict]:
    """
    収集した記事リストから重要なものを厳選し、日本語で要約する。
    1回のリクエストで複数記事を一括処理し、API消費を最小限に抑える。
    """
    if not articles:
        return []

    client = create_gemini_client()

    # 最大件数（上位）に絞り込み
    target_articles = articles[:MAX_TOTAL_ARTICLES]

    # プロンプト用の記事データ成形
    input_list = []
    for idx, art in enumerate(target_articles):
        input_list.append(
            {
                "id": idx,
                "source": art["source"],
                "category": art["category"],
                "title": art["title"],
                "summary": art["summary"],
                "link": art["link"],
            }
        )

    prompt = f"""
あなたは多忙なビジネスパーソンやエンジニア向けに最新AIニュースを届けるプロの編集者です。
以下の記事リストを精査し、通勤中やスキマ時間にスマホで1〜2分で全体を把握できるように、日本語で要約してください。

【記事リスト】
{json.dumps(input_list, ensure_ascii=False, indent=2)}

【要約ルール】
1. 各記事について、日本語で以下の情報を生成してください:
   - "title_ja": 日本語でわかりやすく魅力的な要約タイトル（30文字以内程度）
   - "bullets": 記事の重要ポイントを3点以内の箇条書きリスト（それぞれ50文字以内）
   - "takeaway": 「なぜ重要か / どんな影響があるか」を一言で（60文字以内）
   - "tag": 記事のジャンル（例: 「LLM」「画像生成」「企業動向」「法規制・倫理」「新機能」など1単語）
2. 専門用語をわかりやすく解説し、スマホで流し読みしやすい文体にしてください。
3. 出力は必ず以下のJSONフォーマット配列のみを返してください（Markdownのコードブロックは不要、純粋なJSON文字列）。

[
  {{
    "id": 0,
    "title_ja": "日本語タイトル",
    "bullets": [
      "ポイント1",
      "ポイント2",
      "ポイント3"
    ],
    "takeaway": "このニュースの重要性や影響",
    "tag": "LLM"
  }}
]
"""

    response_text = ""
    # モデルの呼び出し（優先モデル、失敗時はフォールバックモデル）
    for model_name in [GEMINI_MODEL, GEMINI_FALLBACK_MODEL, "gemini-1.5-flash-latest"]:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    temperature=0.2,
                ),
            )
            response_text = response.text
            break
        except Exception as e:
            print(f"Model {model_name} failed: {e}. Trying fallback...")

    if not response_text:
        print("要約の生成に失敗しました。")
        return []

    try:
        # JSONのパース
        clean_text = response_text.strip()
        if clean_text.startswith("```json"):
            clean_text = clean_text[7:]
        if clean_text.startswith("```"):
            clean_text = clean_text[3:]
        if clean_text.endswith("```"):
            clean_text = clean_text[:-3]
        summaries = json.loads(clean_text.strip())

        # 元の記事データとマージ
        result = []
        for item in summaries:
            item_id = item.get("id")
            if item_id is not None and 0 <= item_id < len(target_articles):
                base_art = target_articles[item_id].copy()
                base_art.update(
                    {
                        "title_ja": item.get("title_ja", base_art["title"]),
                        "bullets": item.get("bullets", []),
                        "takeaway": item.get("takeaway", ""),
                        "tag": item.get("tag", base_art["category"]),
                    }
                )
                result.append(base_art)
        return result
    except Exception as e:
        print(f"JSONパースエラー: {e}\nレスポンス: {response_text}")
        return []
