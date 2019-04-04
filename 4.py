"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""


def is_palindrome(numb):
    numb = str(numb)
    return numb == "".join(reversed(numb))


c = 0
i1 = i2 = 0
numb1 = numb2 = 999
for i in range(1, 1000):
    if (i % 10 == 1 and i > 1):
        i2 += 1
        i1 = c * 10
        if (numb2 - i2) % 100 == 0:
            c += 1
    elif i > 1:
        i1 += 1

    result = (numb1 - i1) * (numb2 - i2)
    if is_palindrome(result):
        print(result, numb1 - i1, numb2 - i2, i)
        break
