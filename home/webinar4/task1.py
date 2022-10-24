# Вычислить число c заданной точностью d
# - при d = 0.001, π = 3.141.    10^(-1) ≤ d ≤10^(-10)

accuracy = float(input("Задайте точность для вычисления числа PI: "))

def pi_with_accuracy(accuracy):
    divisible_4 = 4
    current_divider = 1
    upper_difference = 0
    lower_difference = 0

    while True:
        upper_difference = lower_difference + (divisible_4 / current_divider)
        current_divider += 2
        lower_difference = upper_difference - (divisible_4 / current_divider)
        if upper_difference - lower_difference < accuracy:
            break
        current_divider += 2
    return (upper_difference + lower_difference) / 2

print(pi_with_accuracy(accuracy))