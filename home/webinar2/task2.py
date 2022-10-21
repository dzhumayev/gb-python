# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

try:
    inpt = input("Введите вещественное число: ")
    n = int(inpt)
    
    multi = 1
    listOfMulti = []
    for e in range(1, n + 1):
        multi *= e
        listOfMulti.append(multi)
    
    print(listOfMulti)

except ValueError:
    print("Введено не числовое значение")
