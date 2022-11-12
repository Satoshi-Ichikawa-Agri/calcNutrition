"""要件
pyocrを使用して、食品ラベルのkcal部分を読み取る
読み取ったデータを合計し、テキスト形式、CSV形式、データベース形式を選択して保存
保存先からその値を取得
「◯/◯/◯(実行した日の年月日)の摂取カロリーは◯◯kcalです。」と表示
"""
import sys
import csv

from PIL import Image
import pyocr
import pyocr.builders


# オブジェクトの生成
tools = pyocr.get_available_tools()
# tesseractを格納
tool = tools[0]
# 読み込んだ画像に文字列が無い場合、エラーを返す
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

# 使用する画像のpathをlistdictに格納する
data = [
    "images/01.png",
    "images/02.png",
    "images/03.png",
    "images/04.png",
    "images/05.png",
]

# 空のリスト
result = []

# 画像の解析結果を格納
for text in data:
    img = Image.open(text)
    # 分析
    num = tool.image_to_string(
        img,
        lang="eng",
        builder=pyocr.builders.TextBuilder(),
    )
    result += num
    print(result)

# Textへの書込み
with open("text.txt", mode="w") as f:
    f.writelines(result)
