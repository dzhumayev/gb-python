#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

import re

num = int(input("Введите десятичное число: "))
print(re.sub("0b", "", str(bin(num))))