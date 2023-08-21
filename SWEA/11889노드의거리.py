def bfs(v):
    visited[v] = 1

    Q = []
    Q.append(v)

    while Q:
        v = Q.pop(0)

        if v == G:
            return visited[v] - 1

        for w in range(1, V+1):
            if node[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1

    return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[0] * (V + 1) for _ in range(V+1)]

    visited = [0] * (V+1)

    for i in range(E):
        s, e = map(int, input().split())
        node[s][e] = node[e][s] = 1

    S, G = map(int, input().split())

    ans = bfs(S)

    print(f'#{tc} {ans}')