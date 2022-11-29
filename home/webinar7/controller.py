from data_import import *
from dict_tools import *


def temp():
    filepath = "data/data.csv"  # input("Введите путь к файлу: ")
    data_list = import_data(filepath)
    for number, element in enumerate(data_list, 1):
        dictionary = dict(element)
        print_dict(dictionary, number)
        change_flag = True if input("Изменить данные: y - ДА, иначе НЕТ => ") == "y" else False
        if change_flag:
            edit_dict(dictionary)




temp()
