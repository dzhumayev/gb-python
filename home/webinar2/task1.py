#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#- 6782 -> 23
#- 0,56 -> 11

from ast import For


try:
    inpt = input("Введите вещественное число: ")
    float(inpt)
    listOfInpt = list(inpt)
    
    sum = 0
    for e in listOfInpt:
        if e.isdigit():
            sum += int(e)
    
    print(sum)

except ValueError:
    print("Введено не числовое значение")
