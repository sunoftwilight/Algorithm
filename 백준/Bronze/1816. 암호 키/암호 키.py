N = int(input())

for _ in range(N):
    key = int(input())
    num = 2

    answer = 'YES'

    while num < 10 ** 6:
        if key % num == 0:
            answer = 'NO'
            break

        num += 1

    print(answer)
