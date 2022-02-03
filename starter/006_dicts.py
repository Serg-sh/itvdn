d = {'a': 3, 'b': 0, 'c': 4, 'd': -3}
d1 = {'a': 3, 'b': "hello", 'c': 4, 'd': -3}
print(max(d.values()))

l = [val for val in d.values() if str(val).isdigit()]
print(max(l))

print(d.get('f', 'No'))