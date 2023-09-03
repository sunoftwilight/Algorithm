def bfs(a):
    global cnt
    global flag

    Q = [a]
    visited[a] = 1

    while Q:
        a = Q.pop(0)

        if a == B:
            return visited[a] - 1

        for w in range(1, N+1):
            if adj[a][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[a] + 1

    return -1


N = int(input())
A, B = map(int, input().split())
M = int(input())

adj = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    adj[x][y] = adj[y][x] = 1

print(bfs(A))
