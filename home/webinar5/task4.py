#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import re

def rle_compress(text: str):
    text = re.sub(r"(\S)(\d+)", r"\g<1>!\g<2>", text)
    matches_nospace_series = re.findall(r"(([\S ])\2{2,})", text)

    for detected in matches_nospace_series:
        series = detected[0]
        symbol = detected[1]
        text = re.sub(series, f"{symbol}{len(series)}", text)

    return text

def rle_decompress(text:str):
    pass

#with open("task4.input", encoding="utf-8") as f:
#    text = f.readline()
#
#with open("task4.output", "w", encoding="utf-8") as f:
#    f.write(remove_abv_words(text))