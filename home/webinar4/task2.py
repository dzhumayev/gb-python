#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Задайте натуральное число: "))

def factorize(number):
    factors = []
    i = 2
    while i * i <= number: 
        while number % i == 0: 
            number //= i 
            factors.append(i)
        i += 1
    if number > 1:
        factors.append(number)
    return factors

print(factorize(number))


