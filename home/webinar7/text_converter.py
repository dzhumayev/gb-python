import csv

def list_of_dicts_to_csv(list_of_dicts, filepath: str):
    keys = list_of_dicts[0].keys()

    with open(filepath, 'w', newline='', encoding="utf-8") as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list_of_dicts)