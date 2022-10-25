# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.
# - 7x^3 + y + z^2 + x^3 − z^2 = 8x^3 + y

import re
import string

coef_precondition = r"(?<!\^)"
number_pattern = r"([+-]?([0-9]*[.])?[0-9]+)"


def prepare_polynomial(polynomial: str):
    polynomial = re.sub(r"\s*", "", polynomial)
    polynomial = re.sub(r"-", "+-", polynomial)
    polynomial = re.sub(r"^[+]", "", polynomial)
    return polynomial


def prepare_monomial(monomial):
    re_var = r"([A-Za-z])(?!\^)"
    re_var_degree = fr"([A-Za-z]\^{number_pattern})"
    re_start_coef = r"^([-+])?(?=[A-Za-z])"

    pattern_repl = {re_start_coef: r"\g<1>1",
                    re_var: r" \1 ",
                    re_var_degree: r" \1 ",
                    f"{coef_precondition}{number_pattern}": r" \1 "}

    for key in pattern_repl:
        monomial = re.sub(key, pattern_repl.get(key), monomial)

    return re.sub(r"\s+", " ", monomial).strip()


def prepare_monomial_only_vars(monomial):
    return re.sub(coef_precondition + number_pattern, "", prepare_monomial(monomial)).strip()


def monomials_similar(monomial1: str, monomial2: str):
    monomials1 = prepare_monomial_only_vars(monomial1).split(" ")
    monomials2 = prepare_monomial_only_vars(monomial2).split(" ")

    if len(monomials1) != len(monomials2):
        return False
    for e in monomials1:
        if not (e in monomial2):
            return False
    return True

def extract_coef(monomial: str):
    return sum([float(tuple(e)[0]) for e in re.findall(fr"{coef_precondition}{number_pattern}", monomial)])


def polynomial_sum_line(polynomial1: str, polynomial2: str):
    monomials_sum = []

    monomials1 = prepare_polynomial(polynomial1).split("+")
    monomials2 = prepare_polynomial(polynomial2).split("+")
    added_flag = False

    for e1 in monomials1:
        for i, e2 in enumerate(monomials2):
            if monomials_similar(e1, e2):
                coef1 = extract_coef(e1)
                coef2 = extract_coef(e2)
                vars_line = prepare_monomial_only_vars(e1)
                monomials_sum.append(f"{sum([coef1, coef2])}{vars_line}")
                monomials2.pop(i)
                added_flag = True
                break
        if added_flag:
            added_flag = False
        else:
            monomials_sum.append(e1)

    monomials_sum = "+".join(monomials_sum + monomials2).strip()
    re_zerro = ("(?<=^|[+-])0.*?(?=$|[+-])", "")
    monomials_sum = re.sub(tuple(re_zerro)[0], tuple(re_zerro)[1], monomials_sum).strip()

    return monomials_sum


with open("task5.polynomial1", "r") as f:
    polynomial1 = f.read()
with open("task5.polynomial2", "r") as f:
    polynomial2 = f.read()


print(polynomial_sum_line(polynomial1, polynomial2))
print(polynomial_sum_line("7x^3 + y + z^2", "5x^3 - 3z^2 + 4z^3"))
