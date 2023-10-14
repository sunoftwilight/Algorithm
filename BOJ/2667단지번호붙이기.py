d = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(a, b):
    cnt = 1

    Q = []
    Q.append((a, b))
    visited[a][b] = 1
    lst[a][b] = 0

    while Q:
        v = Q.pop(0)
        ci, cj = v[0], v[1]

        for di, dj in d:
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < N and 0 <= nj < N:
                if lst[ni][nj] and visited[ni][nj] == 0:
                    Q.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1
                    cnt += 1
                    lst[ni][nj] = 0

    return cnt


def dfs(i, j):
    global cnt

    visited[i][j] = 1

    lst[i][j] = 0
    cnt += 1

    for di, dj in d:
        ni = i + di
        nj = j + dj

        if 0 <= ni < N and 0 <= nj < N:
            if lst[ni][nj] and visited[ni][nj] == 0:
                dfs(ni, nj)

    return cnt


N = int(input())
lst = [list(map(int, list(input()))) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
total = 0
cnt_home = []
cnt = 0

for i in range(N):
    for j in range(N):
        if lst[i][j]:
            # cnt_home.append(bfs(i, j))
            cnt = 0
            cnt_home.append(dfs(i, j))
            total += 1

cnt_home.sort()

print(total)
for m in cnt_home:
    print(m)
