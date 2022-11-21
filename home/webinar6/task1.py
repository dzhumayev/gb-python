# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from functools import reduce

source_list = 2, 3, 5, 9, 3  # [int(e) for e in input("Введите список чисел через запятую: ").split(",")]

# Получаем список кортежей, где [0] - индекс, [1] - значение
indexed_list = [(i, v) for i, v in enumerate(source_list)]
print(indexed_list)

# Получаем список значений из позиций с нечётными индексами
filterd_list = [tpl[1] for tpl in list(filter(lambda tpl: tpl[0] % 2 != 0, indexed_list))]
print(filterd_list)

# Получаем сумму
sum = reduce(lambda x, y: x + y, filterd_list)
print(sum)
