"""要件
pyocrを使用して、食品ラベルのkcal部分を読み取る
読み取ったデータを合計し、テキスト形式、CSV形式、データベース形式を選択して保存
保存先からその値を取得
「◯/◯/◯(実行した日の年月日)の摂取カロリーは◯◯kcalです。」と表示
"""
import sys
import csv
import datetime
import os

from PIL import Image
import pyocr
import pyocr.builders


# オブジェクトの生成
tools = pyocr.get_available_tools()
# 読み込んだ画像に文字列が無い場合、エラーを返す
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

# tesseractを格納
tool = tools[0]


# 使用する画像のpathをlistに格納する
data = [
    "images/01.png",
    "images/02.png",
    "images/03.png",
    "images/04.png",
    "images/05.png",
]
# data = os.listdir("images")
# print(data)
# print(type(data))


# 本日日付を取得
today = datetime.date.today()
today = str(today)

# 03.pngが読み込めないので、リサイズして挑戦(拡大)
img03 = Image.open(data[2])
resize_img03 = img03.resize((500, 400))
resize_img03.save("images/03_new.png")
data[2] = "images/03_new.png"

# 合計変数
sum = 0

# 画像の解析結果を格納
for text in data:
    if text == "images/03_new.png":
        continue
    # print(text)
    # print(type(text))
    img = Image.open(text)
    # 分析
    num = tool.image_to_string(
        img,
        lang="jpn",
        builder=pyocr.builders.DigitBuilder(),
    )

    num = int(num)
    print(num)
    print(type(num))
    sum += num
print(sum)


# Textへの書込み
with open("text.txt", mode="w") as f:
    f.writelines(str(sum))


# Textを読込、結果を出力
with open("text.txt", mode="r") as f:
    result = f.read()
    print(today + "の摂取カロリーは" + result + "kcalです。")
