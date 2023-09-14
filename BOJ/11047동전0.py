N, K = map(int, input().split())
coin = []

for _ in range(N):
    coin.append(int(input()))

i = N-1
cnt = 0
money = K
while K and i >= 0:
    while K // coin[i] == 0:
        i -= 1

    cnt += K // coin[i]
    K = K % coin[i]

print(cnt)