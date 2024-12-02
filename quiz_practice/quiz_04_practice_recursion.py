def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def sum_of_natural_numbers(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)


def sum_of_digits(n: int) -> int:
    nStr: str = str(n)
    if len(nStr) == 1:
        return n
    else:
        return int(nStr[0]) + int(sum_of_digits(int(nStr[1:])))


def power(num: int, exponent: int):
    if exponent == 0:
        return 1
    else:
        return num * power(num, exponent - 1)
