import sys
sys.setrecursionlimit(10 ** 6)

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def dfs(i, j):
    visited[i][j] = 1

    for di, dj in direction:
        ni = i + di
        nj = j + dj

        if 0 <= ni < N and 0 <= nj < N and safe[ni][nj] >= k and visited[ni][nj] == 0:
            dfs(ni, nj)


N = int(input())
safe = [list(map(int, input().split())) for _ in range(N)]

rain_max = max(map(max, safe))
max_cnt = 0

for k in range(rain_max+1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if safe[i][j] >= k and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1
    max_cnt = max(cnt, max_cnt)

print(max_cnt)
