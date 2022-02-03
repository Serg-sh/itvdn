str1 = " helo"
print(set(str1))
set1 = {1, 3, 2, 0.5}
set2 = {3, 0.5, 4}
print(set1)
print(set1.intersection(set2))
print(set1.difference(set2))

a = {3, 5, 11, 7, 4 - 3}
b = {11, 5, 8, 1, 10, 7}
print(a.intersection(b))
print(a.union(b))

bul = True
for ch in str1:
    if str1.count(ch) > 1:
        bul = False
        break
print(bul)


def check_unique(string):
    for ch in string:
        if str1.count(ch) > 1:
            return False
    return True


print(check_unique(str1))
