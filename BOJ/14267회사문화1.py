def dfs(num):
    for k in sangsa[num]:
        com[k] += com[num]
        dfs(k)


n, m = map(int, input().split())
parent = list(map(int, input().split()))
sangsa = [[] for _ in range(n+1)]
com = [0] * (n + 1)

for i in range(1, n+1):
    if parent[i-1] != -1:
        sangsa[parent[i-1]].append(i)

for _ in range(m):
    i, w = map(int, input().split())
    com[i] += w

dfs(1)

print(*com[1:])
