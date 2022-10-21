#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
#между максимальным и минимальным значением дробной части элементов.
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import re

lst = input("Введите список чисел через запятую: ").split(",")
lst = list(filter(lambda e: re.match(r"\d*\.\d+", e.strip()) != None, lst))
lst = [float(e) for e in [re.sub(r"(\d+)\.(\d+)", r"0.\2", e) for e in lst]]
print(max(lst) - min(lst))


