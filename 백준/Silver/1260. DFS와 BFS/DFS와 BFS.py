from collections import deque


def dfs(w):
    disited[w] = True
    danswer.append(str(w))

    if disited.count(True) == N:
        return

    for node in adj[w]:
        if not disited[node]:
            dfs(node)


def bfs(w):
    Q = deque([w])
    bisited[w] = True
    banswer.append(str(w))

    while Q:
        cw = Q.popleft()

        for node in adj[cw]:
            if not bisited[node]:
                bisited[node] = True
                banswer.append(str(node))
                Q.append(node)


N, M, V = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(N+1):
    adj[i].sort()

danswer = []
disited = [False] * (N + 1)
dfs(V)

banswer = []
bisited = [False] * (N + 1)
bfs(V)

print(' '.join(danswer))
print(' '.join(banswer))
