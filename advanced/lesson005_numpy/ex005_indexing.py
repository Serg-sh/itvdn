import numpy

a = numpy.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
])

print(a[0, 0])
print(a[0, -1])
print(a[0, -2])
print(a[:2, 4])
print(a[1:, 4])
print(a[:, 4])
print(a[:2])
print(a[:, 0:4])
print(a[1:3, 1:3])

b = numpy.array([
    [
        [1, 2],
        [3, 4],
        [5, 6],
    ],
    [
        [6, 7],
        [8, 9],
        [10, 11]
    ],
    [
        [12, 13],
        [14, 15],
        [16, 17]
    ],
    [
        [18, 19],
        [20, 21],
        [22, 23],
    ]
])

print('B', b[1:3, 1:2, 1])
print('B', b[:, :, 0])
print('B', b[:, :, 1])
print('B', b[:, :, -1])
print('B', b[:, ::-1, ::-1])
print('B', b[::-1, ::-1, ::-1])

