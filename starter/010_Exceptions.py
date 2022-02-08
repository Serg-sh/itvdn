def divide(a, b):
    try:
        c = a / b
        print(c)
    except ZeroDivisionError as err:
        print(0, err)


divide(2, 0)


def list_index(lst, index):
    try:
        print(lst[index])
    except IndexError as err:
        print(-1, "\n", err)


list_index(lst=[1, 2, 3, 4], index=4)