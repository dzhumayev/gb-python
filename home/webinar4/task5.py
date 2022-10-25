# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.
# - 7x^3 + y + z^2 + x^3 − z^2 = 8x^3 + y

import re
import string

re_letter = r"[A-Za-z]"
re_coef_lookbehind_neg = r"(?<![\^\.\d])"
re_coef = fr"{re_coef_lookbehind_neg}([+-]?([0-9]*[.])?[0-9]+)"

re_degree_lookahead_neg = r"(?!\^)"
re_var_simple = fr"({re_letter}){re_degree_lookahead_neg}"

#re_degree_lookahead_pos = r"(?=\^\d+)"
re_var_in_degree = fr"({re_letter}\^d+)"



def prepare_polynomial(polynomial: str):
    result = polynomial.replace(" ", "")
    result = re.sub(r"([+-])", r" \1", result).strip()
    print(f"prepare_polynomial(polynomial: str): {result}")
    return result
prepare_polynomial("7x^3 + y - z  ^ 2")

def prepare_monomial(monomial):
    repl = r"\g<1>"
    result = re.sub(fr"^([+-])?(?={re_letter})", fr"{repl}1 ", monomial)
    result = re.sub(fr"{re_coef}", fr" {repl} ", result)
    result = re.sub(fr"{re_var_simple}", fr" {repl} ", result)
    result = re.sub(fr"{re_var_in_degree}", fr" {repl} ", result)
    print(f"prepare_monomial(monomial): {result}")
    return result
prepare_monomial("+z^223q")


def prepare_monomial_only_vars(monomial):
    return re.sub(re_coef_lookbehind_neg + re_coef, "", prepare_monomial(monomial)).strip()


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
    return sum([float(tuple(e)[0]) for e in re.findall(fr"{re_coef_lookbehind_neg}{re_coef}", monomial)])


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


#with open("task5.polynomial1", "r") as f:
#    polynomial1 = f.read()
#with open("task5.polynomial2", "r") as f:
#    polynomial2 = f.read()
#
#
#print(polynomial_sum_line(polynomial1, polynomial2))
#print(polynomial_sum_line("7x^3 + y + z^2", "5x^3 - 3z^2 + 4z^3"))
