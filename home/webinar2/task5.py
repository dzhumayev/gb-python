#Реализуйте алгоритм перемешивания списка.

import random

list = [1, 2, 3, 4, 5]
print(list)

def mixlist(list):
    for i in range(len(list)):
        ix_rand = random.randint(0, len(list) - 1)
        temp = list[i]
        list[i] = list[ix_rand]
        list[ix_rand] = temp
    return list

print(mixlist(list))










