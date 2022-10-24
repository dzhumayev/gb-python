# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input("Введите натуральную степень k: "))

def random_polynomial(k):
    coefficients = [random.randint(0, 101) for i in range(k + 1)]
    monomials = []

    for e in range(k + 1):
        if coefficients[e] == 0:
            if len(monomials) == 0:
                return "0"
            else:
                continue
        current_k = k - e
        x_note = f"x^{current_k}" if current_k >= 2 else "x" if current_k == 1 else ""
        monomials.append(f"{coefficients[e]}{x_note}")

    return f"{'+'.join(monomials)}=0"



with open("task4.data", "w") as f:
    f.write(random_polynomial(k))
