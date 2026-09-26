"""
メイン実行スクリプト (main.py)
ニュース収集 -> AI要約 -> HTML生成を一連で実行する
"""

import argparse
import datetime
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# プロジェクトルートをsys.pathに追加
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# ローカルの .env を読み込む
load_dotenv(PROJECT_ROOT / ".env")

from src.fetcher import fetch_latest_news
from src.summarizer import summarize_articles
from src.generator import generate_html


def get_mock_articles():
    """APIキーがない場合やUIテスト用のダミーデータ"""
    return [
        {
            "id": 0,
            "source": "OpenAI News",
            "category": "公式発表",
            "tag": "LLM",
            "title_ja": "OpenAIが次世代モデルのプレビュー版を発表",
            "bullets": [
                "推論性能が前モデル比で約40%向上し、数学やコーディングで高スコアを記録",
                "思考プロセスの可視化機能が強化され、回答根拠の追跡が容易に",
                "開発者向けAPIの価格も従来比で約30%引き下げられる見通し",
            ],
            "takeaway": "業務でのAI自動化やコード生成の精度が劇的に改善される可能性が高いです。",
            "link": "https://openai.com/news/",
            "published": datetime.datetime.now(),
        },
        {
            "id": 1,
            "source": "Google AI Blog",
            "category": "公式発表",
            "tag": "マルチモーダル",
            "title_ja": "Googleが超軽量な新型オンデバイスAIを公開",
            "bullets": [
                "スマートフォンやタブレット端末の単体で高速に動作する軽量設計",
                "テキストだけでなく画像や音声のリアルタイム認識にもローカル対応",
                "通信環境のない場所やプライバシー重視の環境での活用が期待される",
            ],
            "takeaway": "スマホアプリやウェアラブル機器のオフラインAI機能が一気に普及しそうです。",
            "link": "https://blog.google/technology/ai/",
            "published": datetime.datetime.now(),
        },
        {
            "id": 2,
            "source": "ITmedia AI+",
            "category": "国内メディア",
            "tag": "企業動向",
            "title_ja": "国内大手企業で生成AIの業務導入率が8割を突破",
            "bullets": [
                "社内問い合わせ対応や資料作成での日常的な活用が定着",
                "一方で、ハルシネーション（誤情報）対策や著作権ガイドラインの策定が課題",
                "社員向けリスキリングやプロンプト研修の需要が急速に拡大中",
            ],
            "takeaway": "AIを使う人と使わない人の生産性格差が社内でも顕著になりつつあります。",
            "link": "https://www.itmedia.co.jp/aiplus/",
            "published": datetime.datetime.now(),
        },
    ]


def main():
    parser = argparse.ArgumentParser(description="AIニュースまとめ自動生成ツール")
    parser.add_argument("--mock", action="store_true", help="Gemini APIを使わずテスト用データでHTMLを生成する")
    args = parser.parse_args()

    print("=== AIニュースまとめ生成開始 ===")

    if args.mock:
        print("[テストモード] モックデータを使用してHTMLを生成します。")
        articles = get_mock_articles()
    else:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print("警告: GEMINI_API_KEY が設定されていません。")
            print("モックデータを使用してHTMLを生成します（本番実行時は .env または環境変数にAPIキーを設定してください）。")
            articles = get_mock_articles()
        else:
            print("1. 最新ニュースをRSSから収集しています...")
            raw_articles = fetch_latest_news()
            print(f"   -> {len(raw_articles)} 件の記事を収集しました。")

            if not raw_articles:
                print("記事が取得できませんでした。モックデータで代替します。")
                articles = get_mock_articles()
            else:
                print("2. Google Gemini APIで重要記事の要約を行っています...")
                articles = summarize_articles(raw_articles)
                print(f"   -> {len(articles)} 件の要約が完了しました。")

                if not articles:
                    print("要約に失敗したため、モックデータで代替します。")
                    articles = get_mock_articles()

    print("3. スマホ向けHTMLを生成しています...")
    output_path = generate_html(articles)
    print(f"=== 完了: {output_path} に出力されました ===")


if __name__ == "__main__":
    main()
