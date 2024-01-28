N = int(input())
B = list(map(int, input().split()))

total = 0

while True:
    for i in range(N):
        if B[i] % 2:
            B[i] -= 1
            total += 1

    if sum(B) == 0: break

    for i in range(N):
        B[i] //= 2
    total += 1

print(total)