"""要件
pyocrを使用して、食品ラベルのkcal部分を読み取る
読み取ったデータを合計し、テキスト形式、CSV形式、データベース形式を選択して保存
保存先からその値を取得
「◯/◯/◯(実行した日の年月日)の摂取カロリーは◯◯kcalです。」と表示
"""
import datetime
import sys

from PIL import Image
import pyocr
import pyocr.builders


# オブジェクトの生成
tools = pyocr.get_available_tools()

# get_available_toolsに何も存在しない場合、エラーを返す
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

# tesseractを格納
tool = tools[0]

# pyocr.buildersを生成する
builder = pyocr.builders.DigitBuilder(tesseract_layout=6)

# 本日日付を取得
today = str(datetime.date.today())

# 使用する画像のpathをlistに格納する
data = [
    "images/01.png",
    "images/02.png",
    "images/03.png",
    "images/04.png",
    "images/05.png",
]


def reading_calculation(data, lang, builder):
    """画像の解析結果を格納
    data: 読み取りたいimageデータのpathのList
    lang: 読み取る言語 jpn/eng
    builder: builderオブジェクト Digit/Textなどある
    return: 合計
    """
    # 合計変数
    sum = 0
    # 画像パスの分だけ読み取りを行い、読み取り結果をnumに格納し、sumで加算していく
    for read_data in data:
        # 画像読込
        img = Image.open(read_data)
        # 分析
        num = int(
            tool.image_to_string(
                img,
                lang=lang,
                builder=builder,
            )
        )
        # 読み取り結果を加算
        sum += num
    return str(sum)


def text_write(content):
    """Textへ書込み
    受け取った値をテキストに書き込む
    """
    with open("text.txt", mode="w") as f:
        f.writelines(content)


def text_read():
    """Textを読込、結果を出力
    受け取ったテキストを読み込むに書き込む
    """
    with open("text.txt", mode="r") as f:
        reading_result = f.read()
        print(today + "の摂取カロリーは" + reading_result + "kcalです。")


def main():
    result = reading_calculation(data, "jpn", builder)
    return result


if __name__ == "__main__":
    result = main()
    text_write(result)
    text_read()
