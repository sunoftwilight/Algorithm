direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(i, j, c):
    global cnt

    cnt += 1
    color[i][j] = 'V'

    for di, dj in direct:
        ni = i + di
        nj = j + dj

        if 0 <= ni < M and 0 <= nj < N:
            if c == 'W' and color[ni][nj] == 'W':
                dfs(ni, nj, 'W')

            elif c == 'B' and color[ni][nj] == 'B':
                dfs(ni, nj, 'B')


N, M = map(int, input().split())

color = [list(input()) for _ in range(M)]

white = 0
blue = 0

for i in range(M):
    for j in range(N):
        if color[i][j] == 'W':
            cnt = 0
            dfs(i, j, 'W')
            white += cnt ** 2

        elif color[i][j] == 'B':
            cnt = 0
            dfs(i, j, 'B')
            blue += cnt ** 2

print(white, blue)
