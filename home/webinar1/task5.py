# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве

import math

try:
    x1 = float(input("Введите x1: "))
    y1 = float(input("Введите y1: "))
    x2 = float(input("Введите x2: "))
    y2 = float(input("Введите y2: "))

    result = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    print(f"Расстояние между точками в 2D пространстве: {result}")
except ValueError:
    print("Введено не числовое значение")
