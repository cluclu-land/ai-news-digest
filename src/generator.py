"""
HTML生成モジュール (generator.py)
要約された記事データからスマホ向けHTMLファイルをレンダリングして出力する
"""

import datetime
import os
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "..", "templates")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "docs")


def generate_html(articles: list[dict], output_file: str = "index.html") -> str:
    """記事リストからHTMLを生成して保存する"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("index.html.jinja2")

    # 日本時間 (JST) のフォーマット
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    updated_str = now.strftime("%Y年%m月%d日 %H:%M")

    rendered = template.render(
        articles=articles,
        updated_time=updated_str,
    )

    output_path = os.path.join(OUTPUT_DIR, output_file)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered)

    print(f"HTMLが正常に生成されました: {output_path}")
    return output_path
