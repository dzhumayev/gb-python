# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#Здесь непонятное условие, сделал по выражению из семинара

try:
    n = int(input("Введите вещественное число: "))

    def seqdict(n):
        return {key: round((1+1/val)**val, 2) for key, val in enumerate(range(1, n+1), 1)}

    dict = seqdict(n)
    print(dict)
    print(sum(dict.values()))


except ValueError:
    print("Введено не числовое значение")
