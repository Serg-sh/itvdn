from math import gcd


def func_1(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return 0 if a + b >= 0 else -1
    else:
        return 1


print(func_1(4, 6))
print(func_1(4, -6))
print(func_1(4, 6.0))
print(func_1(4, 'r'))


def sum_func(a, b):
    return a + b


def func_2(func):
    print("Начало вызова")
    print(func)
    print("Конец вызова")


func_2(sum_func(5, 6))


def func_3(a, b):
    return gcd(a, b)


print(func_3(45, 33))
