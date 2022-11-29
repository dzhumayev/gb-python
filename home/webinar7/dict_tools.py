def print_dictionary(dictionary: dict, number: int):
    print(f"Элемент {number}")
    for key in dictionary.keys():
        print(f"\t{key} : {dictionary.get(key)}")
    print("----------------------------------------")

def edit_dictionary(dictionary: dict):
    print("Введите новые значения для следующих значений или оставьте поле пустым чтобы не вносить изменение:")
    for key in dictionary.keys():
        new_value = input(f"{key}: ")
        if new_value != "":
            dictionary[key] = new_value
