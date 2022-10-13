# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

try:
    dayNumber = int(input("Введите день недели: "))

    if dayNumber >= 1 and dayNumber <= 7:
        if dayNumber <= 5:
            print(f"День недели с номером {dayNumber} будний")
        else:
            print(f"День недели с номером {dayNumber} выходной")
    else:
        print(f"День недели с номером {dayNumber} не существует")
except ValueError:
    print("Введено не числовое значение")
