import sys; sys.setrecursionlimit(10**6)

direction = [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]


def dfs(i, j):
    visited[i][j] = 1

    for di, dj in direction:
        ni = i + di
        nj = j + dj

        if 0 <= ni < h and 0 <= nj < w:
            if island[ni][nj] and visited[ni][nj] == 0:
                dfs(ni, nj)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    else:
        island = [list(map(int, input().split())) for _ in range(h)]

        visited = [[0] * w for _ in range(h)]
        cnt = 0

        for i in range(h):
            for j in range(w):
                if island[i][j] and visited[i][j] == 0:
                    dfs(i, j)
                    cnt += 1

        print(cnt)
