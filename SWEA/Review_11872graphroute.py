def dfs(v):
    visited[v] = 1  # 방문 체크

    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[w] == 0:  # 인접 & 미방문 정점 있으면
            dfs(w)  # 재귀 호출


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        s, e = map(int, input().split())  # 간선
        adj[s][e] = 1  # 유향 그래프

    S, G = map(int, input().split())

    dfs(S)

    print(f'#{tc} {visited[G]}')  # S -> G 이동 경로가 있었다면 G에 방문 했겠지~
