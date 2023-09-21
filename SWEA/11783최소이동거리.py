def dijkstra(s):
    D[s] = 0

    for i in range(N+1):

        min_v = 987654321
        for j in range(N+1):
            if visited[j] == 0 and D[j] < min_v:
                min_v = D[j]
                v = j

        visited[v] = 1

        for k in range(N+1):
            if visited[k] == 0 and adj[v][k]:
                if D[k] > D[v] + adj[v][k]:
                    D[k] = D[v] + adj[v][k]


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)

    D = [987654321] * (N+1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w

    dijkstra(0)
    print(f'#{tc} {D[N]}')