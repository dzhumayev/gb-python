# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def remove_abv_words(text: str):
    text = list(filter(lambda s: "абв" not in s, text.split(" ")))
    return " ".join(text)


with open("task1.input", encoding="utf-8") as f:
    text = f.readline()

with open("task1.output", "w", encoding="utf-8") as f:
    f.write(remove_abv_words(text))
