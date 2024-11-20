N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = [float("inf")] * N

x = set()
y = set()

for i, j in arr:
    x.add(i)
    y.add(j)

for i in list(x):
    for j in list(y):
        dis = []

        for ci, cj in arr:
            dis.append(abs(i - ci) + abs(j - cj))

        dis.sort()

        for k in range(N):
            answer[k] = min(answer[k], sum(dis[: k+1]))

print(*answer)
