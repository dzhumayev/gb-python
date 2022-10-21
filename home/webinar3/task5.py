#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def list_fib_with_neg(num):
    lst = [0]
    a = 0
    b = 1
    for __ in range(num):
        a, b = b, a + b
        lst.insert(0, a * -1)
        lst.append(a)
    return lst

num = int(input("Введите десятичное число: "))
print(list_fib_with_neg(num))