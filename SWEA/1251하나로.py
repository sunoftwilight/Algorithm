def solve(s):
    D[s] = 0
    total = 0

    for i in range(N):
        min_v = 9999999999999
        for j in range(N):
            if visited[j] == 0 and D[j] < min_v:
                min_v = D[j]
                v = j

        visited[v] = 1
        total += adj[PI[v]][v]

        for w in range(N):
            if adj[v][w] and not visited[w]:
                if D[w] > adj[v][w]:
                    D[w] = adj[v][w]
                    PI[w] = v

    return total


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    D = [9999999999999] * N
    PI = list(range(N))
    visited = [0] * N

    adj = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                w = ((X[i]-X[j])**2 + (Y[i]-Y[j])**2) * E
                adj[i][j] = adj[j][i] = w

    print(f'#{tc} {round(solve(0))}')
