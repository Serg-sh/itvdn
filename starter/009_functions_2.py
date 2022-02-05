a = lambda x: x**2
print(a(2))


y = 10


def func_1():
    global y
    x = 20


func_1()
print(y)


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n


print(factorial(4))
