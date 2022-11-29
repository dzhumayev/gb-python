from data_import import *
from data_export import *
from dict_tools import *


def choose_save_mode():
    prompt = """Выберите действие
    1 - Сохранить
    2 - Сохранить как"""

    while True:
        save_mode = input(prompt)
        if save_mode == "1":
            return "save"
        elif save_mode == "2":
            return "save_as"
        else:
            print("Ошибка выбора режима. Попробуйте ещё раз")
            continue


def temp():
    filepath = "data/data.csv"  # input("Введите путь к файлу: ")

    try:
        dictionary_list = [dict(e) for e in import_data(filepath)]

        change_flag = False
        change_prompt = "Изменить данные: y - ДА, иначе НЕТ => "

        for number, dictionary in enumerate(dictionary_list, 1):
            print_dictionary(dictionary, number)
            change_flag = True if change_flag or input(change_prompt) == "y" else False
            if change_flag:
                edit_dictionary(dictionary)

        if change_flag:
            if choose_save_mode() == "save":
                filepath = "data/tempf"
                export_data(dictionary_list, filepath)
            else:
                filepath = "data/tempf.csv"
                export_data(dictionary_list, filepath)
    except ValueError:
        print("Ошибка. Невозможно импортировать файл")


temp()
