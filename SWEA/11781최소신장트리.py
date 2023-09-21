def prim(s):
    D[s] = 0
    total = 0

    for i in range(V+1):

        min_v = 987654321
        for j in range(V+1):
            if visited[j] == 0 and D[j] < min_v:
                min_v = D[j]
                v = j

        visited[v] = 1
        total += adj[PI[v]][v]

        for w in range(V+1):
            if adj[v][w] and visited[w] == 0:
                if D[w] > adj[v][w]:
                    D[w] = adj[v][w]
                    PI[w] = v

    return total


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    D = [987654321] * (V+1)
    PI = list(range(V+1))

    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = adj[e][s] = w

    print(f'#{tc} {prim(0)}')
