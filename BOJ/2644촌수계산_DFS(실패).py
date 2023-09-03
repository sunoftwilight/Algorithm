def dfs(a):
    global cnt
    global flag

    visited[a] = 1

    if a == B:
        flag = 1
        return

    for w in range(1, N+1):
        if adj[a][w] == 1 and visited[w] == 0:
            visited[w] = visited[a] + 1
            dfs(w)


N = int(input())
A, B = map(int, input().split())
M = int(input())

adj = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    adj[x][y] = adj[y][x] = 1

cnt = 0
flag = -1
dfs(A)

if flag != -1:
    flag = cnt

print(visited)
print(flag)