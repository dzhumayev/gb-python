# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import re


def rle_compress(text: str):
    escape = '#'
    text = re.sub(fr"({escape})(\d+)", r"\g<1>_\g<2>", text)

    pattern = r"([\S ])\1{3,}"
    matches = [e for e in re.finditer(pattern, text)]

    result = []
    slice_since = 0
    for match in matches:
        position = match.start(1)
        slice = text[slice_since:position]
        result.append(slice)
        symbol = match.group(1)
        length = match.end(0) - match.start(0)
        result.append(f"{escape}{length}{symbol}")
        slice_since = position + length
        pass

    return "".join(result) + text[slice_since:]


def rle_decompress(text: str):
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

# with open("task4.input", encoding="utf-8") as f:
#    text = f.readline()
#
# with open("task4.output", "w", encoding="utf-8") as f:
#    f.write(remove_abv_words(text))
