#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

try:
    n = int(input("Введите вещественное число: "))
    
    multi = 1
    listOfMulti = []
    for e in range(1, n + 1):
        multi *= e
        listOfMulti.append(multi)

    print(listOfMulti)

except ValueError:
    print("Введено не числовое значение")
