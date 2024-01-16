direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(row, col, cur):
    for dr, dc in direct:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 0:
                arr[nr][nc] = cur + 1
                virus[cur].append((nr, nc))


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

virus = [[] for _ in range(K)]

for k in range(K):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == k+1:
                virus[k].append((i, j))

while S != 0:
    for k in range(K):
        for _ in range(len(virus[k])):
            r, c = virus[k].pop(0)
            bfs(r, c, k)
    S -= 1

print(arr[X-1][Y-1])
