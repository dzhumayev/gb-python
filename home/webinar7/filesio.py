def read_file(filepath: str):
    with open(filepath, encoding="utf-8") as f:
        return f.read()
