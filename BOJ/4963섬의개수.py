direction = [0, 1], [1, 0], [0, -1], [-1, 0]


def dfs(i, j):
    visited[i][j] = 1

    for di, dj in direction:
        ni = i + di
        nj = j + dj

        if 0 <= ni < w and 0 <= nj < h and visited[ni][nj] != 0:
            dfs(ni, nj)


# while list(map(int, input().split())) != [0, 0]:
while True:
    w, h = map(int, input().split())
    island = [list(map(int, input().split())) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]
    cnt = 0

    for i in range(w):
        for j in range(h):
            if island[i][j] and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1

    print(cnt)
