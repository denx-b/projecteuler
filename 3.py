"""
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""


def is_prime(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False

    return True


def large_div(numb):
    import math

    exp = 0
    compare = 0
    while (compare < numb):
        exp += 1
        compare = math.factorial(exp)

    div = 2 ** exp
    if div >= numb:
        div = math.ceil(numb / 2)

    while (div > 1):
        if (numb % div == 0 and is_prime(div)):
            return div
        div -= 1

    return div


print(large_div(600851475143))
