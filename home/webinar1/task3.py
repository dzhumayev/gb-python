# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

try:
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))

    if x == 0 or y == 0:
        print(f"Точка x = {x} , y = {y} не принадлежит какой-либо четверти ")
    elif x > 0 and y > 0:
        print(f"Точка x = {x} , y = {y} принадлежит четверти 1")
    elif x < 0 and y > 0:
        print(f"Точка x = {x} , y = {y} принадлежит четверти 2")
    elif x < 0 and y < 0:
        print(f"Точка x = {x} , y = {y} принадлежит четверти 3")
    else: # x > 0 and y < 0
        print(f"Точка x = {x} , y = {y} принадлежит четверти 4")

except ValueError:
    print("Введено не числовое значение")
