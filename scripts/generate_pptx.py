"""
PowerPoint (.pptx) スライド自動生成スクリプト
青を基調とした落ち着いたフォーマルなビジネスデザイン
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# --- カラーパレット定義（フォーマル・ネイビー/ブルー） ---
COLOR_PRIMARY_DARK = RGBColor(15, 35, 60)      # 深いネイビー (#0F233C)
COLOR_PRIMARY_BLUE = RGBColor(26, 82, 138)     # ロイヤルブルー (#1A528A)
COLOR_ACCENT_BLUE  = RGBColor(41, 128, 185)    # アクセントブルー (#2980B9)
COLOR_LIGHT_BLUE   = RGBColor(235, 244, 252)   # ペールブルー (#EBF4FC)
COLOR_BG_LIGHT     = RGBColor(248, 250, 252)   # 背景薄グレー (#F8FAFC)
COLOR_WHITE        = RGBColor(255, 255, 255)   # 白
COLOR_TEXT_MAIN    = RGBColor(30, 41, 59)      # メイン文字色 (#1E293B)
COLOR_TEXT_MUTED   = RGBColor(100, 116, 139)   # 補助文字色 (#64748B)
COLOR_BORDER       = RGBColor(226, 232, 240)   # ボーダー色 (#E2E8F0)
COLOR_TAG_BG       = RGBColor(224, 242, 254)   # タグ背景 (#E0F2FE)
COLOR_SUCCESS      = RGBColor(22, 101, 52)     # グリーンアクセント (#166534)

FONT_HEADING = "Meiryo"
FONT_BODY = "Meiryo"


def apply_background(slide, color):
    """スライド全体の背景色を設定"""
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_header(slide, title_text, category_text="AI NEWS DIGEST ARCHITECTURE"):
    """共通ヘッダー（カテゴリータグ、タイトル、区切り線）を追加"""
    # カテゴリタグ
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.3))
    tf_c = cat_box.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = category_text
    p_c.font.name = FONT_HEADING
    p_c.font.size = Pt(10)
    p_c.font.bold = True
    p_c.font.color.rgb = COLOR_ACCENT_BLUE

    # タイトル
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(11.7), Inches(0.6))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(22)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_PRIMARY_DARK

    # 水平仕切り線
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.3), Inches(11.7), Inches(0.02)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = COLOR_BORDER
    line.line.color.rgb = COLOR_BORDER


def add_card(slide, left, top, width, height, bg_color=COLOR_WHITE, border_color=COLOR_BORDER):
    """角丸カード風の矩形シェイプを追加"""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1)
    return card


def create_presentation(output_path: str):
    prs = Presentation()
    # 16:9 ワイドスクリーン
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # ==========================================
    # SLIDE 1: 表紙
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_background(s1, COLOR_PRIMARY_DARK)

    # 装飾アクセントライン
    accent_bar = s1.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(1.8), Inches(0.12), Inches(3.6)
    )
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = COLOR_ACCENT_BLUE
    accent_bar.line.fill.background()

    # タイトルボックス
    t_box = s1.shapes.add_textbox(Inches(1.5), Inches(1.7), Inches(10.5), Inches(3.8))
    tf = t_box.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "CLOUD-NATIVE & ZERO-COST AUTOMATION"
    p0.font.name = FONT_HEADING
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_ACCENT_BLUE
    p0.space_after = Pt(14)

    p1 = tf.add_paragraph()
    p1.text = "毎朝自動更新 AIニュースまとめシステム"
    p1.font.name = FONT_HEADING
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE
    p1.space_after = Pt(14)

    p2 = tf.add_paragraph()
    p2.text = "完全無料で運用するサーバーレス情報収集・要約アーキテクチャ仕様書"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(16)
    p2.font.color.rgb = COLOR_LIGHT_BLUE
    p2.space_after = Pt(28)

    p3 = tf.add_paragraph()
    p3.text = "GitHub Actions × Google Gemini API × GitHub Pages"
    p3.font.name = FONT_BODY
    p3.font.size = Pt(13)
    p3.font.color.rgb = RGBColor(148, 163, 184)

    # ==========================================
    # SLIDE 2: 背景と解決アプローチ (Why & What)
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_background(s2, COLOR_BG_LIGHT)
    add_header(s2, "背景と目的: スキマ時間に1分で掴むAI動向")

    # 左カード: 課題 (Challenges)
    add_card(s2, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    c1_box = s2.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(4.8))
    c1_tf = c1_box.text_frame
    c1_tf.word_wrap = True

    p = c1_tf.paragraphs[0]
    p.text = "直面していた課題"
    p.font.name = FONT_HEADING
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(16)

    bullets1 = [
        ("AIトレンドの激流", "日進月歩で大量の情報が発信され、網羅的なキャッチアップに時間がかかる。"),
        ("英語ソースの壁", "OpenAIやGoogle等の一次速報は英語が多く、朝の通勤中に読むハードルが高い。"),
        ("アプリ管理の煩わしさ", "専用アプリを入れたり、定期的なアカウント管理・ログインを行う手間を避けたい。"),
        ("固定費はゼロにしたい", "個人利用においてサーバー維持費や高額なLLM API料金はかけたくない。"),
    ]
    for title, desc in bullets1:
        p_t = c1_tf.add_paragraph()
        p_t.text = f"● {title}"
        p_t.font.bold = True
        p_t.font.size = Pt(13)
        p_t.font.color.rgb = COLOR_PRIMARY_BLUE
        p_d = c1_tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.space_after = Pt(10)

    # 右カード: 解決アプローチ (Solutions)
    add_card(s2, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.2))
    c2_box = s2.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(5.0), Inches(4.8))
    c2_tf = c2_box.text_frame
    c2_tf.word_wrap = True

    p = c2_tf.paragraphs[0]
    p.text = "本システムによる解決策"
    p.font.name = FONT_HEADING
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(16)

    bullets2 = [
        ("毎朝6:30の全自動実行", "PCを起動していなくてもクラウド（GitHub Actions）が自律稼働し収集・要約。"),
        ("Geminiによる構造化要約", "3行要点＋一言ポイント＋タグで、1記事あたり10秒で本質が理解可能。"),
        ("ブラウザ完結（URL共有）", "アプリ不要。SafariやChromeのホーム画面追加でネイティブ同様の操作性。"),
        ("完全無料（維持費0円）", "GitHubの無料枠とGemini Free Tierの最適化により、永久に費用ゼロ。"),
    ]
    for title, desc in bullets2:
        p_t = c2_tf.add_paragraph()
        p_t.text = f"✔ {title}"
        p_t.font.bold = True
        p_t.font.size = Pt(13)
        p_t.font.color.rgb = COLOR_SUCCESS
        p_d = c2_tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.space_after = Pt(10)

    # ==========================================
    # SLIDE 3: 全体システムアーキテクチャ (Architecture)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_background(s3, COLOR_BG_LIGHT)
    add_header(s3, "システム全体アーキテクチャ: 4つのレイヤー構成")

    # 4列のカード配置
    layers = [
        ("1. 収集レイヤー", "Data Collection", COLOR_PRIMARY_BLUE, [
            "主要AI情報源のRSS",
            "OpenAI公式 / Google AI",
            "TechCrunch / The Verge",
            "ITmedia AI+ (国内)",
            "重複URLの自動排除",
            "最新順ソート & 抽出",
        ]),
        ("2. 自動化・統制", "Orchestration", COLOR_PRIMARY_DARK, [
            "GitHub Actions",
            "毎朝JST 6:30 Cron実行",
            "手動トリガー対応",
            "Ubuntu最新ランナー",
            "APIキーをSecrets保管",
            "平均実行時間: 約35秒",
        ]),
        ("3. AI要約エンジン", "AI Summarization", COLOR_ACCENT_BLUE, [
            "Google Gemini API",
            "gemini-2.5-flash 採用",
            "一括構造化JSONプロンプト",
            "日本語3行要約の生成",
            "「ここがポイント」抽出",
            "API消費を最小1回に圧縮",
        ]),
        ("4. 配信・閲覧", "Delivery & UI", COLOR_PRIMARY_BLUE, [
            "GitHub Pages",
            "静的HTML (Jinja2生成)",
            "スマホ特化カード型UI",
            "ダークモード自動追従",
            "ホーム画面追加でPWAライク",
            "URLだけで全端末から閲覧",
        ]),
    ]

    card_w = Inches(2.7)
    card_h = Inches(5.1)
    card_gap = Inches(0.28)
    start_x = Inches(0.8)

    for i, (title, sub, col, items) in enumerate(layers):
        x = start_x + i * (card_w + card_gap)
        add_card(s3, x, Inches(1.6), card_w, card_h)

        # ヘッダーカラー帯
        band = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, Inches(1.6), card_w, Inches(0.9))
        band.fill.solid()
        band.fill.fore_color.rgb = col
        band.line.fill.background()

        b_box = s3.shapes.add_textbox(x + Inches(0.15), Inches(1.65), card_w - Inches(0.3), Inches(0.8))
        b_tf = b_box.text_frame
        b_tf.word_wrap = True
        bp0 = b_tf.paragraphs[0]
        bp0.text = title
        bp0.font.name = FONT_HEADING
        bp0.font.size = Pt(13)
        bp0.font.bold = True
        bp0.font.color.rgb = COLOR_WHITE
        bp1 = b_tf.add_paragraph()
        bp1.text = sub
        bp1.font.size = Pt(9)
        bp1.font.color.rgb = COLOR_LIGHT_BLUE

        # 項目リスト
        content_box = s3.shapes.add_textbox(x + Inches(0.15), Inches(2.6), card_w - Inches(0.3), Inches(3.9))
        c_tf = content_box.text_frame
        c_tf.word_wrap = True
        for idx, item in enumerate(items):
            p = c_tf.paragraphs[0] if idx == 0 else c_tf.add_paragraph()
            p.text = f"• {item}"
            p.font.size = Pt(11)
            p.font.color.rgb = COLOR_TEXT_MAIN
            p.space_after = Pt(8)

    # ==========================================
    # SLIDE 4: 採用技術スタックと選定理由 (Tech Stack)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_background(s4, COLOR_BG_LIGHT)
    add_header(s4, "採用技術スタックと選定理由")

    tech_items = [
        ("GitHub Actions", "サーバーレスCron実行", "サーバー構築・保守が完全不要。月2,000分の無料枠があり、リポジトリと一体でコード・Secrets・実行履歴を一元管理できるため。"),
        ("Google Gemini API", "高速・高精度な言語モデル", "gemini-2.5-flashの高速レスポンスと高い日本語要約力。何より無料利用枠（Free Tier）が充実しており、個人開発で費用が一切発生しないため。"),
        ("GitHub Pages", "無料静的ホスティング", "リポジトリの docs フォルダから直接Webサイトを公開可能。サーバー代が永久無料であり、スマホやPCのブラウザからURLを開くだけで閲覧できるため。"),
        ("Python & Jinja2", "スクリプト＆HTMLテンプレート", "feedparserやbeautifulsoup4による迅速なRSS取得と、Jinja2による柔軟で美しいレスポンシブHTML生成が最小限の依存関係で実現できるため。"),
    ]

    for i, (name, role, reason) in enumerate(tech_items):
        y = Inches(1.6) + i * Inches(1.3)
        add_card(s4, Inches(0.8), y, Inches(11.7), Inches(1.15))

        box = s4.shapes.add_textbox(Inches(1.1), y + Inches(0.1), Inches(11.1), Inches(0.95))
        tf = box.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = name
        p.font.name = FONT_HEADING
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY_DARK

        # 役割バッジ風
        p_sub = tf.add_paragraph()
        p_sub.text = f"役割: {role}"
        p_sub.font.bold = True
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = COLOR_ACCENT_BLUE

        p_desc = tf.add_paragraph()
        p_desc.text = f"選定理由: {reason}"
        p_desc.font.size = Pt(10.5)
        p_desc.font.color.rgb = COLOR_TEXT_MUTED

    # ==========================================
    # SLIDE 5: 完全無料運用の成立メカニズム (Zero Cost)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_background(s5, COLOR_BG_LIGHT)
    add_header(s5, "完全無料運用のメカニズム: 各社無料枠の最適化")

    cards = [
        ("GitHub Actions 実行時間", "月2,000分 無料枠", [
            "1回の実行時間: 約35秒",
            "月間合計: 35秒 × 30日 ＝ 約18分/月",
            "無料枠消費率: わずか 0.9% 未満",
            "残存枠で十分なテスト・開発が可能",
        ]),
        ("Google Gemini API コスト", "Free Tier (無料枠)", [
            "複数記事を一括プロンプトで要約",
            "1日あたりわずか 1〜2回 のAPIコール",
            "Geminiの無料枠上限（15 RPM / 1,500 RPD）に対し余裕の運用",
            "API課金発生のリスクを構造的に遮断",
        ]),
        ("GitHub Pages 配信コスト", "無期限 無料ホスティング", [
            "静的HTMLファイル配信のため負荷ゼロ",
            "月間100GBの無料帯域枠",
            "サーバー保守・ドメイン代不要",
            "独自証明書（HTTPS）も自動付与",
        ]),
    ]

    card_w3 = Inches(3.68)
    for i, (title, badge, items) in enumerate(cards):
        x = Inches(0.8) + i * (card_w3 + Inches(0.33))
        add_card(s5, x, Inches(1.6), card_w3, Inches(5.1))

        # バッジ部分
        b_box = s5.shapes.add_textbox(x + Inches(0.2), Inches(1.8), card_w3 - Inches(0.4), Inches(0.8))
        b_tf = b_box.text_frame
        b_tf.word_wrap = True
        p0 = b_tf.paragraphs[0]
        p0.text = title
        p0.font.name = FONT_HEADING
        p0.font.size = Pt(14)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_PRIMARY_DARK

        p1 = b_tf.add_paragraph()
        p1.text = badge
        p1.font.bold = True
        p1.font.size = Pt(12)
        p1.font.color.rgb = COLOR_SUCCESS
        p1.space_after = Pt(12)

        # 項目
        i_box = s5.shapes.add_textbox(x + Inches(0.2), Inches(2.7), card_w3 - Inches(0.4), Inches(3.8))
        i_tf = i_box.text_frame
        i_tf.word_wrap = True
        for idx, item in enumerate(items):
            p = i_tf.paragraphs[0] if idx == 0 else i_tf.add_paragraph()
            p.text = f"✔ {item}"
            p.font.size = Pt(11)
            p.font.color.rgb = COLOR_TEXT_MAIN
            p.space_after = Pt(10)

    # ==========================================
    # SLIDE 6: 毎朝の自動処理パイプライン詳細 (Pipeline)
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_background(s6, COLOR_BG_LIGHT)
    add_header(s6, "毎朝の自動処理パイプライン: 5つのステップ")

    pipeline_steps = [
        ("Step 1", "Cronトリガー起動", "毎朝JST 6:30（UTC 21:30）にGitHub Actionsが自動起動。Ubuntu仮想環境を即座に立ち上げ。"),
        ("Step 2", "RSSフェッチ & フィルタ", "OpenAI、Google、TechCrunch等から最新記事を取得。URL重複を排除し最新順に整列。"),
        ("Step 3", "Gemini一括要約", "上位記事を束ねてGemini APIへ投入。日本語タイトル、3行要点、重要ポイントを一括生成。"),
        ("Step 4", "レスポンシブHTML生成", "Jinja2テンプレートにデータを注入。スマホ最適化・ダークモード対応の index.html を出力。"),
        ("Step 5", "自動コミット & デプロイ", "GitHub Actions Botが docs/index.html をコミット＆Push。GitHub Pagesが即座に反映。"),
    ]

    for i, (step_num, title, desc) in enumerate(pipeline_steps):
        y = Inches(1.6) + i * Inches(1.02)
        add_card(s6, Inches(0.8), y, Inches(11.7), Inches(0.9))

        # ステップバッジ
        badge = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), y + Inches(0.18), Inches(1.1), Inches(0.54))
        badge.fill.solid()
        badge.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
        badge.line.fill.background()
        tf_b = badge.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.text = step_num
        p_b.font.name = FONT_HEADING
        p_b.font.size = Pt(12)
        p_b.font.bold = True
        p_b.font.color.rgb = COLOR_WHITE
        p_b.alignment = PP_ALIGN.CENTER

        # 内容テキスト
        box = s6.shapes.add_textbox(Inches(2.3), y + Inches(0.1), Inches(10.0), Inches(0.7))
        tf = box.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.name = FONT_HEADING
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_PRIMARY_DARK

        p1 = tf.add_paragraph()
        p1.text = desc
        p1.font.size = Pt(10.5)
        p1.font.color.rgb = COLOR_TEXT_MUTED

    # ==========================================
    # SLIDE 7: 拡張性と今後の展望 (Extensibility)
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_background(s7, COLOR_BG_LIGHT)
    add_header(s7, "拡張性と今後の展望: プラットフォームの発展性")

    extensions = [
        ("情報源（ソース）の多角化", "現在は主要RSSが中心だが、ArXivの最新注目論文やHackerNews、AI開発者のX（旧Twitter）まとめなど、情報源を自在に追加・拡充可能。"),
        ("マルチチャネル配信", "HTML生成に加え、Discord Webhook、LINE Messaging API、自分宛てメールなどへのマルチ配信も数行のコード追加で実現可能。"),
        ("パーソナライズ要約", "関心のあるキーワード（例: 「画像生成」「オンデバイスAI」「LangChain」など）を指定し、重み付けや優先度判定をAIに行わせる高度化。"),
        ("過去ログのアーカイブ機能", "日別のまとめを docs/archives/ 配下に静的HTMLとして蓄積し、カレンダー形式で過去のニュースを検索・振り返り可能にする拡張。"),
    ]

    for i, (title, desc) in enumerate(extensions):
        y = Inches(1.6) + i * Inches(1.3)
        add_card(s7, Inches(0.8), y, Inches(11.7), Inches(1.15))

        box = s7.shapes.add_textbox(Inches(1.1), y + Inches(0.12), Inches(11.1), Inches(0.9))
        tf = box.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = f"◆ {title}"
        p0.font.name = FONT_HEADING
        p0.font.size = Pt(15)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_PRIMARY_BLUE
        p0.space_after = Pt(4)

        p1 = tf.add_paragraph()
        p1.text = desc
        p1.font.size = Pt(11)
        p1.font.color.rgb = COLOR_TEXT_MUTED

    # ==========================================
    # SLIDE 8: まとめ・振り返り (Summary)
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_background(s8, COLOR_PRIMARY_DARK)

    # まとめカード（白）
    add_card(s8, Inches(1.5), Inches(1.2), Inches(10.33), Inches(5.1), bg_color=COLOR_WHITE)

    s_box = s8.shapes.add_textbox(Inches(1.9), Inches(1.5), Inches(9.5), Inches(4.5))
    s_tf = s_box.text_frame
    s_tf.word_wrap = True

    p0 = s_tf.paragraphs[0]
    p0.text = "まとめ: サーバーレス個人DXの実現"
    p0.font.name = FONT_HEADING
    p0.font.size = Pt(24)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_PRIMARY_DARK
    p0.space_after = Pt(20)

    conclusions = [
        ("無料枠だけで実用システムは構築できる", "GitHub ActionsとGemini APIの無料枠を組み合わせることで、サーバー代もAPI費用も一切かけずに運用可能。"),
        ("ブラウザ×PWAライクが最も持続可能", "アプリ開発・ストア公開・OSアップデート追従のコストを排除し、URL1本で全端末から閲覧できる身軽さを実現。"),
        ("自分専用の情報キュレーション", "既存のニュースアプリのような雑音（広告や無関係なニュース）を排し、純粋に知りたい情報だけを毎朝スキマ時間に摂取できる環境が完成。"),
    ]

    for title, desc in conclusions:
        p_t = s_tf.add_paragraph()
        p_t.text = f"✔ {title}"
        p_t.font.name = FONT_HEADING
        p_t.font.bold = True
        p_t.font.size = Pt(14)
        p_t.font.color.rgb = COLOR_PRIMARY_BLUE
        p_d = s_tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11.5)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.space_after = Pt(14)

    # 保存
    prs.save(output_path)
    print(f"PowerPointスライドが生成されました: {output_path}")


if __name__ == "__main__":
    output_file = os.path.join(os.path.dirname(__file__), "..", "ai_news_system_architecture.pptx")
    create_presentation(os.path.abspath(output_file))
