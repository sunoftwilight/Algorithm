from collections import deque

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs():
    global cnt

    Q = deque()
    cnt_no = 0

    for i in range(N):
        for j in range(M):
            if tmt[i][j] == 1:
                Q.append((i, j))
                visited[i][j] = 1
                cnt += 1

            elif tmt[i][j] == -1:
                cnt_no += 1

    if cnt == N * M - cnt_no:
        cnt = 0
        return

    while Q:
        ci, cj = Q.popleft()

        for di, dj in d:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < M:
                if tmt[ni][nj] == 0:
                    tmt[ni][nj] = 1
                    visited[ni][nj] = visited[ci][cj] + 1
                    Q.append((ni, nj))

    cnt = max(map(max, visited)) - 1
    return


M, N = map(int, input().split())
tmt = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
cnt = 0

bfs()

for i in range(N):
    for j in range(M):
        if tmt[i][j] == 0:
            cnt = -1

print(cnt)
