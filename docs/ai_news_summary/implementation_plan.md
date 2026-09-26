# 実装手順書: AIニュースまとめシステム

## 1. ディレクトリ構造計画
プロジェクトルート
├── .github/
│   └── workflows/
│       └── daily_update.yml   # 毎朝実行するGitHub Actions定義
├── docs/
│   ├── ai_news_summary/      # 本ドキュメント管理用
│   │   ├── task.md
│   │   ├── implementation_plan.md
│   │   └── walkthrough.md
│   └── index.html            # GitHub Pagesで公開されるWebページ（自動生成）
├── src/
│   ├── config.py             # RSSソース一覧やプロンプト設定
│   ├── fetcher.py            # RSS取得・記事本文抽出処理
│   ├── summarizer.py         # Gemini APIによる要約処理
│   ├── generator.py          # HTML生成処理（Jinja2またはテンプレート文字列）
│   └── main.py               # 全体実行オーケストレーション
├── templates/
│   └── index.html.jinja2     # スマホ向けカード型レイアウトのHTMLテンプレート
├── requirements.txt          # Python依存ライブラリ
├── .env.example              # 環境変数サンプル（GEMINI_API_KEY）
└── .gitignore                # 不要ファイル・APIキー除外

## 2. 採用する技術スタック
- 言語: Python 3.10+
- ライブラリ:
  - feedparser: RSSフィード解析
  - google-genai または google-generativeai: Gemini APIクライアント
  - jinja2: HTMLテンプレートエンジン
  - beautifulsoup4: HTMLクリーニング・抜粋用
  - python-dotenv: ローカル開発時の環境変数読込
- ニュース情報源（RSS）:
  - 海外AI主要情報（OpenAIブログ、Google AIブログ、TechCrunch AIなど）
  - 国内主要AI・IT情報（ITmedia AI+、GIGAZINE AI、Zenn/Qiita人気記事など）
  ※ 重複排除、最新24時間〜48時間以内の記事を対象にフィルタリング

## 3. 実装ステップ

### フェーズ1: ローカル開発環境の準備
- requirements.txt の定義
- .gitignore の作成（APIキーやキャッシュのコミット防止）
- .env によるローカルAPIキー設定の仕組み作成

### フェーズ2: ニュース収集＆要約ロジックの実装
- 主要RSSからの最新記事取得と重複排除
- Gemini API（gemini-1.5-flash / gemini-2.0-flash）を用いた要約
  - 1記事につき「3行まとめ」「なぜ重要か」「元記事リンク」の構造化出力
  - 朝のスキマ時間（3〜5分）で全件把握できるボリュームに調整

### フェーズ3: スマホ向けUI/HTML生成の実装
- モバイルファーストのレスポンシブデザイン
  - カード型デザイン
  - ダークモード自動切替
  - 1タップで元記事を開くボタン
  - 記事のジャンル別タグ（海外速報、国内動向、ツール・技術など）
  - 日付表示および更新時刻表示

### フェーズ4: ローカル検証
- テスト実行で実際のニュースを取得・要約し、HTMLを出力
- ブラウザで表示確認（スマホ表示モード等で確認）

### フェーズ5: GitHub連携とGitHub Actions / Pages設定
- GitHubリポジトリの作成
- Secretsに GEMINI_API_KEY を登録
- GitHub Actionsによる自動実行（毎朝6:30 JST）の設定
- GitHub Pagesの有効化（docsフォルダ配信）
- スマホからのアクセス確認
