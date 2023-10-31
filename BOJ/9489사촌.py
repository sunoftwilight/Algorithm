while True:
    N, K = map(int, input().split())
    if (N, K) == (0, 0):
        break

    arr = list(map(int, input().split()))
    parent = [0] * N
    parent[0] = -1

    idx = -1
    for i in range(1, N):
        if arr[i] == K:
            target = i

        if arr[i] != arr[i-1] + 1:
            idx += 1

        parent[i] = idx

    ans = 0
    for j in range(1, N):
        if parent[j] != parent[target] and parent[parent[j]] == parent[parent[target]]:
            ans += 1

    print(ans)
