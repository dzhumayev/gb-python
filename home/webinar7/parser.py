from filesio import read_file
import csv
import json


def parse_data(filepath: str):
    if filepath.endswith(".csv"):
        return parse_csv(filepath)
    elif filepath.endswith(".json"):
        return parse_json(filepath)
    else:
        return read_file(filepath)


def parse_csv(filepath: str):
    lst = []
    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            lst.append(row)
    return lst


def parse_json(filepath: str):
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)
