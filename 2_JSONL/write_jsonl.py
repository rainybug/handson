import csv
import json
import os

# 入力CSVファイル (latexラベルが含まれている)
csv_path = "latex_labels.csv"
# 出力JSONLファイル (LLaMA用データ)
jsonl_path = "llama_latex_data.jsonl"

# 画像ファイルのベースパス (学習時に使う相対パスまたは絶対パス)
image_base_path = "CROHME23/IMG/train"

# CSVファイルを読み込み、JSONLファイルに書き出し
with open(csv_path, newline='', encoding='utf-8') as csvfile, open(jsonl_path, 'w', encoding='utf-8') as jsonlfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        filename = row["filename"]  # 画像ファイルの相対パス
        latex = row["latex"]        # 対応するLaTeX数式

        # 学習用プロンプト (LLaMA用)
        prompt = "[INST] Can you explain the mathematical expression in this image? [/INST]"

        # 実際の画像パスを作成
        # 学習時にこのパスが画像ローダーの仕様に合わせる必要あり
        image_path = os.path.join(image_base_path, filename)

        # JSONLデータを1行分作成
        record = {
            "image": image_path,   # 画像ファイルのパス
            "text": prompt,        # 学習用入力テキスト
            "label": latex         # 正解のLaTeXラベル
        }

        # JSON形式で1行書き込み (ensure_ascii=Falseで日本語など文字化け回避)
        jsonlfile.write(json.dumps(record, ensure_ascii=False) + "\n")

# 完了メッセージ
print(f"JSONLファイル保存完了: {jsonl_path}")
