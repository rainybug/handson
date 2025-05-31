import os 
import csv
import xml.etree.ElementTree as ET
from glob import glob

# パス設定
img_root = "CROHME23/IMG/train"          # 画像ファイルのルート
inkml_root = "CROHME23/InkML/train"      # inkmlファイルのルート
output_csv = "latex_labels.csv"          # 出力CSVファイル名

# データセット分割（サブフォルダ）
splits = ["CROHME2023", "CROHME2019"]

# InkMLのネームスペースを定義
NS = {"ink": "http://www.w3.org/2003/InkML"}

data = []  # 出力用データリスト

# 各データセット（分割）を処理
for split in splits:
    img_dir = os.path.join(img_root, split)       # 画像フォルダパス
    inkml_dir = os.path.join(inkml_root, split)   # inkmlフォルダパス
    print(f"Processing: {split}")

    # png画像ファイルをループ
    for img_path in glob(os.path.join(img_dir, "*.png")):
        base = os.path.splitext(os.path.basename(img_path))[0]    # ファイル名（拡張子なし）
        inkml_path = os.path.join(inkml_dir, base + ".inkml")     # 対応するinkmlファイル
        rel_path = os.path.relpath(img_path)                      # 相対パス
        if not os.path.exists(inkml_path):
            print(f"inkml not found for {base}.png")
            continue  # inkmlファイルが存在しない場合はスキップ

        try:
            tree = ET.parse(inkml_path)     # inkmlファイルを解析
            root = tree.getroot()

            # ink:annotationタグをネームスペース指定で検索
            found = False
            for ann in root.findall(".//ink:annotation", NS):
                if ann.attrib.get("type") == "truth":   # タイプが'truth'のannotation
                    latex = ann.text.strip()           # LaTeX文字列を抽出
                    data.append({"filename": rel_path, "latex": latex})  # 出力データに追加
                    found = True
                    break
            if not found:
                print(f"No 'truth' annotation in {base}.inkml")  # 'truth' annotationが見つからない場合

        except Exception as e:
            print(f"Failed to parse {base}.inkml: {e}")  # 解析エラー時の出力

# CSVファイルにデータを書き出し
with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["filename", "latex"])
    writer.writeheader()         # ヘッダー行を書き込む
    writer.writerows(data)       # データを書き込む

print(f"Done. Saved to {output_csv} ({len(data)} entries)")  # 完了メッセージ
