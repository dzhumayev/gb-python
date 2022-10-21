#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

import math

lst = [int(e) for e in input("Введите список чисел через запятую: ").split(",")]
multiPairList = []

for i, e in enumerate(lst):
    if i > (len(lst) - 1) / 2:
        break
    multiPairList.append(lst[i] * lst[len(lst) - 1 - i])

print(multiPairList)

