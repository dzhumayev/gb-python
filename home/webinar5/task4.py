#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import re

def rle_compress(text: str):
    text = re.sub(r"(#)(\d+)", r"\g<1>_\g<2>", text)
    matches_series = re.findall(r"(([\S ])\2{3,})", text)

    for match in matches_series:
        series = match[0]
        symbol = match[1]
        repl = f"#{len(series)}{symbol}"
        text = re.sub(series, repl, text)

    return text

def rle_decompress(text:str):
    patterns = [r"(([^_])(\d+))", r"(?<!_)(([_])(\d+))"]

    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            code = match[0]
            symbol = match[1]
            length = int(match[2])
            repl = symbol * length
            text = re.sub(code, repl, text)

    return re.sub(r"(?<=[\S ])(_)(?=\d+)", "", text)

#with open("task4.input", encoding="utf-8") as f:
#    text = f.readline()
#
#with open("task4.output", "w", encoding="utf-8") as f:
#    f.write(remove_abv_words(text))