def bfs(v):
    Q = [v]
    visited[v] = 1

    while Q:
        v = Q.pop(0)

        for w in range(1, N+1):
            if adj[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = 1 + visited[v]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)

    for i in range(M):
        s, e = map(int, input().split())
        adj[s][e] = adj[e][s] = 1

    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            cnt += 1
            bfs(i)

    print(f'#{tc} {cnt}')
