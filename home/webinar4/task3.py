#Задайте последовательность чисел. Напишите программу, которая выведет список 
#неповторяющихся элементов исходной последовательности.
# - '1,1,2,3,4,5,3' -> [2, 4, 5]

list = [int(e) for e in input("Введите список чисел через запятую: ").split(",")]

uq_list = []
for e in list:
    first_index = list.index(e)
    last_index = list[::-1].index(e)

    if len(list) - 1 - first_index - last_index == 0:
        uq_list.append(e)
        
print(uq_list)



    



