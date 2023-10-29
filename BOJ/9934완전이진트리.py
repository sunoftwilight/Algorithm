K = int(input())
bd = list(map(int, input().split()))

s = (2 ** K - 1) // 2
step = (2 ** K - 1) // 2 + 1

print(bd[s])
s //= 2

while True:
    for i in range(s, 2**K-1, step):
        print(bd[i], end=' ')
    print()

    if s == 0:
        break

    s //= 2
    step //= 2

