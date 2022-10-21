# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

def seq(n):
    return [e for e in range(n * -1, n + 1)]
multi = 1
with open("task4.data", "r") as f:
    numbers = [int(e) for e in f.read().splitlines()]
    nseq = seq(int(input("Введите n: ")))
    for i in numbers:
        multi *= nseq[i]
print(multi)
    









