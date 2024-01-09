import sys; sys.setrecursionlimit(10**6)

direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(a, b):
    global thisfood

    for di, dj in direct:
        ni = a + di
        nj = b + dj

        if 0 <= ni < N and 0 <= nj < M and road[ni][nj] == 1:
            road[ni][nj] = 0
            thisfood += 1
            dfs(ni, nj)


N, M, K = map(int, input().split())

road = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    road[r-1][c-1] = 1

maxfood = 0

for i in range(N):
    for j in range(M):
        if road[i][j] == 1:
            thisfood = 0
            dfs(i, j)
            maxfood = max(maxfood, thisfood)

print(maxfood)
