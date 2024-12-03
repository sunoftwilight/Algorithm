T = int(input())

for _ in range(T):
    result = input()

    total = 0
    tmp = 0

    for res in result:
        if res == 'O':
            tmp += 1
            total += tmp

        else:
            tmp = 0

    print(total)