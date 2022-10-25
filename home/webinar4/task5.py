# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.
# - 7x^3 + y + z^2, x^3 − z^2

import re
import functools

re_letter = r"[A-Za-z]"

re_coef_lookbehind_neg = r"(?<![\^\.\d])"
re_coef = fr"{re_coef_lookbehind_neg}([+-]?([0-9]*[.])?[0-9]+)"

re_degree_lookahead_neg = r"(?!\^)"
re_var_simple = fr"({re_letter}){re_degree_lookahead_neg}"
re_var_in_degree = fr"({re_letter}\^d+)"


def split_polynomial(polynomial: str):
    result = polynomial.replace(" ", "")
    result = re.sub(r"([+-])", r" \1", result)
    result = re.sub(r"([+])", r"", result)
    return result.strip().split(" ")


def minimize_spaces(s: str):
    return re.sub(r"\s+", fr" ", s).strip()

def set_default_coef(monomial: str):
    repl = r"\g<1>"
    result = re.sub(fr"^([+-])?(?={re_letter})", fr"{repl}1 ", monomial)
    result = re.sub(fr"{re_coef}", fr" {repl} ", result)
    result = re.sub(fr"{re_var_simple}", fr" {repl} ", result)
    result = re.sub(fr"{re_var_in_degree}", fr" {repl} ", result)
    return minimize_spaces(result).strip()


def remove_coefs(monomial: str):
    result = re.sub(re_coef_lookbehind_neg + re_coef, "", set_default_coef(monomial))
    return result.strip()


def extract_coef(monomial: str):
    result = functools.reduce(lambda a, b: a * b, [float(tuple(e)[0]) for e in re.findall(fr"{re_coef}", monomial)])
    return result


def monomials_similar(monomial1: str, monomial2: str):
    monomials1 = remove_coefs(monomial1).split(" ")
    monomials2 = remove_coefs(monomial2).split(" ")

    if len(monomials1) != len(monomials2):
        return False
    for e in monomials1:
        if not (e in monomial2):
            return False
    return True


def polynomial_sum_line(polynomial1: str, polynomial2: str):
    result = []

    monomials1 = split_polynomial(polynomial1)
    monomials2 = split_polynomial(polynomial2)
    added_flag = False

    for e1 in monomials1:
        for i, e2 in enumerate(monomials2):
            if monomials_similar(e1, e2):
                coefs_sum = extract_coef(set_default_coef(e1)) + extract_coef(set_default_coef(e2))
                if coefs_sum == 0:
                    added_flag = True
                    monomials2.pop(i)
                    break
                result.append("+" if coefs_sum > 0 else "")
                result.append(f"{coefs_sum}{remove_coefs(e1)}".replace(" ", ""))
                monomials2.pop(i)
                added_flag = True
                break
        if added_flag:
            added_flag = False
        else:
            result.append("+" if extract_coef(set_default_coef(e1)) > 0 else "")
            result.append(e1)

    result = re.sub(r"^[+]", "", re.sub(r"\.0", "", "".join(result + monomials2)))
    return result.strip()


with open("task5.polynomial1", "r") as f:
    polynomial1 = f.readline()

with open("task5.polynomial2", "r") as f:
    polynomial2 = f.readline()

print(polynomial_sum_line(polynomial1, polynomial2))
