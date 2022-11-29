from text_converter import *
import json



def export_data(list_of_dicts, filepath: str):
    if filepath.endswith(".csv"):
        export_csv(list_of_dicts, filepath)
    elif filepath.endswith(".json"):
        export_json(list_of_dicts, filepath)
    else:
        export_other(list_of_dicts, filepath)


def export_csv(list_of_dicts, filepath: str):
    list_of_dicts_to_csv(list_of_dicts, filepath)


def export_json(list_of_dicts, filepath: str):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(list_of_dicts, f)

def export_other(list_of_dicts, filepath: str):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(list_of_dicts))
