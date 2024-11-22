def perm(arr, k):
    if k >= M:
        print(*arr)
        return

    for j in range(1, N+1):
        if not visited[j]:
            visited[j] = True
            perm(arr+[j], k+1)
            visited[j] = False


N, M = map(int, input().split())
visited = [False] * (N + 1)

for i in range(1, N+1):
    visited[i] = True
    perm([i], 1)
    visited[i] = False
