"""要件
pyocrを使用して、食品ラベルのkcal部分を読み取る
読み取ったデータを合計し、テキスト形式、CSV形式、データベース形式を選択して保存
保存先からその値を取得
「◯/◯/◯(実行した日の年月日)の摂取カロリーは◯◯kcalです。」と表示
"""
from PIL import Image
import pyocr


# オブジェクトの生成
tools = pyocr.get_available_tools()
# tesseractを格納
tool = tools[0]

# 使用する画像のpathをdictに格納する
kcal_image = {
    "1": "images/01.png",
    "2": "images/02.png",
    "3": "images/03.png",
    "4": "images/04.png",
    "5": "images/05.png",
}


img01 = Image.open(kcal_image["1"])
text = tool.image_to_string(
    img01,
    lang="eng+jpn",
    builder=pyocr.builders.TextBuilder(),
)
