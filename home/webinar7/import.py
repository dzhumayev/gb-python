from parser import *


def import_data(filepath: str):
    return parse_data(filepath)

print(import_data("data/import/data.json"))

