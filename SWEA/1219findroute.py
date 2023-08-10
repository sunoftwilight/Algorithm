import sys; sys.stdin = open('11874_input.txt', 'r')

def dfs(v):
    visited[v] = 1

    for w in range(1, 100):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)


T = 10

for tc in range(1, T+1):
    no, total = map(int, input().split())
    temp = list(map(int, input().split()))

    adj = [[0] * 100 for _ in range(100)]

    visited = [0] * 100

    for i in range(total):
        s, e = temp[2*i], temp[2*i+1]
        adj[s][e] = 1

    dfs(0)

    print(f'#{tc} {visited[99]}')