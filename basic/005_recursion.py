def gen_list(num: int, lst: list = None):
    global val
    if lst is None:
        lst = []
        val = 1

    if num < val:
        lst.append(1)
        print(lst)
        return
    else:
        lst.append(val)
        val += 1
        if val > num:
            print(lst)
            return
        gen_list(num, lst)


gen_list(6)
gen_list(10)


def is_contains(value: int, obj):
    if len(obj) >= 1:
        if isinstance(obj[0], list):
            is_contains(value, obj[0])
        else:
            if obj[0] == value:
                print(f"{value} in list {obj=}")
                return
            else:
                is_contains(value, obj[1:])
    else:
        print(f"{value} not in list {obj=}")
        return


list_1 = [1, 2, [3, 4, [5, [6, []]]]]
list_2 = []

is_contains(2, list_1)
is_contains(6, list_1)
is_contains(7, list_1)
is_contains(2, list_2)
