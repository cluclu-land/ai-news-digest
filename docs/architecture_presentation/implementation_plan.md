# 実装手順書: アーキテクチャ資料（PowerPoint & HTMLインフォグラフィック）

## 1. 成果物の配置計画
- docs/architecture_presentation/
  - task.md
  - implementation_plan.md
  - walkthrough.md
- ai_news_system_architecture.pptx （プロジェクトルート直下に生成）
- docs/infographic.html （GitHub Pagesでもそのまま公開・閲覧可能な場所に配置）
- scripts/
  - generate_pptx.py （PowerPoint生成スクリプト）

## 2. スライド (.pptx) の構成計画
青（濃紺 #0F2B48、プライマリーブルー #1E6091、アクセント #184E77、背景 #F8FAFC）を基調とした16:9ワイドスライド。
- スライド1: 表紙（タイトル: 毎朝更新AIニュースまとめシステムの技術と構成 / サブタイトル: 完全無料で実現するサーバーレス情報収集パイプライン）
- スライド2: 背景と解決アプローチ（忙しい朝の課題、アプリ不要のWeb閲覧、完全無料の要件）
- スライド3: 全体システムアーキテクチャ（入力: RSS → 処理: GitHub Actions + Python → AI: Gemini 1.5/2.5 Flash → 配信: GitHub Pages）
- スライド4: 主要採用技術と選定理由（GitHub Actions, Google Gemini API, GitHub Pages, Feedparser/Jinja2）
- スライド5: 完全無料運用の成立要因（月2000分枠、Gemini無料利用枠、GitHub Pages静的配信の組み合わせ）
- スライド6: 自動化パイプラインの流れ（朝6:30 Cron起動 → 取得 → 一括プロンプト要約 → HTML生成 → 自動Git Push → デプロイ）
- スライド7: 今後の発展・拡張性（RSSソースの拡充、多言語対応、LINE/Discordへのマルチ配信対応）
- スライド8: まとめ・学び（サーバーレス＋無料AI APIによる個人DXの可能性）

## 3. HTMLインフォグラフィックの構成計画
- SVGアニメーションによるデータフロー可視化（パルスする信号、流れるコネクタ線）
- 4大コンポーネント（Collector, AI Engine, Orchestration, Web Delivery）のインタラクティブカード
- 各技術の「なぜこれを選んだか」「無料枠のメリット」「スペック」をポップアップ/タブで詳細表示
- 配色・タイポグラフィ: 洗練されたモダンダーク/サイバーテックデザイン、グラデーション、グラスモフィズム
- レスポンシブ＆自己完結型（単体HTMLファイルとして外部通信なしでも表示可能）

## 4. 実行手順
1. 依存ライブラリ（python-pptx）のインストール
2. scripts/generate_pptx.py の作成と実行
3. docs/infographic.html の作成
4. 生成物の検証
5. walkthrough.md 作成とGitコミット
