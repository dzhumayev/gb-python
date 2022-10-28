# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import re


def rle_compress(text: str):
    anchor = '#'
    escape = '_'

    text = re.sub(fr"({anchor})({escape})*(\d+)", fr"\g<1>\g<2>{escape}\g<3>", text)

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
        result.append(f"{anchor}{length}{symbol}")
        slice_since = position + length
        pass

    return "".join(result) + text[slice_since:]


def rle_decompress(text: str):
    anchor = '#'
    escape = '_'

    pattern = fr"({anchor})(\d+)([\S ])"
    matches = [e for e in re.finditer(pattern, text)]

    result = []
    slice_since = 0
    for match in matches:
        position = match.start(1)
        slice = text[slice_since:position]
        result.append(slice)
        symbol = match[3]
        length = int(match[2])
        repl = symbol * length
        result.append(repl)
        slice_since = match.end(3)
        pass

    result = "".join(result) + text[slice_since:]
    return re.sub(fr"({anchor})({escape})", anchor, result)

# with open("task4.input", encoding="utf-8") as f:
#    text = f.readline()
#
# with open("task4.output", "w", encoding="utf-8") as f:
#    f.write(remove_abv_words(text))
