# 집합 사용 풀이

def find_set(x):
    if x == parent[x]:
        return x

    else:
        return find_set(parent[x])


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())           # 정점, 간선
    tmp = list(map(int, input().split()))
    parent = list(range(N+1))                  # make-set

    for i in range(M):
        s, e = tmp[2 * i], tmp[2 * i + 1]

        # union
        parent[find_set(e)] = find_set(s)

    cnt = 0
    for i in range(1, N+1):
        if parent[i] == i:
            cnt += 1

    print(f'#{tc} {cnt}')


# ---------------------------------------------------
# BFS 사용 풀이 -> 내가 쓴 답이랑 동일
# ---------------------------------------------------
# DFS 사용 풀이
def dfs(v):
    visited[v] = 1

    for w in adj[v]:
        if visited[w] == 0:
            dfs(w)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 정점, 간선
    tmp = list(map(int, input().split()))
    adj = [[] for _ in range(V + 1)]  # 인접리스트
    visited = [0] * (V + 1)

    # 인접리스트 채우기
    for i in range(E):
        s, e = tmp[2 * i], tmp[2 * i + 1]
        adj[s].append(e)
        adj[e].append(s)

    cnt = 0

    for i in range(1, V + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(f'#{tc} {cnt}')