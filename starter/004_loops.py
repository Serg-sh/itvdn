counter = 5
while counter > 0:
    print(f"iteration: {counter=}")
    counter -= 1

for num in range(100)[::-1]:
    if num % 13 == 0:
        print(num)


