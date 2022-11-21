# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import re
from itertools import repeat


def compress_sequence(sequence: str):
    count = len(sequence)
    if count == 1:
        return sequence
    return f"{count}{sequence[0]}"


def decompress_sequence(sequence: str):
    if len(sequence) == 1:
        return sequence
    symbol = re.search(r"([a-z])", sequence).group(0)
    count = int(re.search(r"[0-9]+", sequence).group(0))
    return "".join([e for e in repeat(symbol, count)])


def compress_text(text: str):
    pattern = r"([\S ])\1*"
    return "".join(list(map(compress_sequence, [match.group(0) for match in re.finditer(pattern, text)])))


def decompress_text(text: str):
    pattern = r"(\d+)*\w"
    return "".join(list(map(decompress_sequence, [match.group(0) for match in re.finditer(pattern, text)])))


with open("task2.input", encoding="utf-8") as f:
    source_sequence = f.readline()

compressed_sequence = compress_text(source_sequence)
decompressed_sequence = decompress_text(compressed_sequence)

print(compressed_sequence)
print(decompressed_sequence)
print(source_sequence)
