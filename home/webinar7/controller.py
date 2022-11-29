def choose_data_format():
    prompt = """Выберите формат документа
    1 - csv
    2 - json
    3 - xml
    => """

    fmt = input(prompt)
    if fmt == "1":
        return "csv"
    elif fmt == "2":
        return "json"
    elif fmt == "3":
        return "xml"
    else:
        return None

