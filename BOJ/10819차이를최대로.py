def perm(n, k):    # 원소 개수 n, depth k
    global max_diff

    if n == k:
        curr_diff = 0

        for i in range(1, N):
            curr_diff += abs(p[i-1] - p[i])

        max_diff = max(curr_diff, max_diff)
        return

    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = arr[i]
                perm(n, k+1)
                visited[i] = 0


N = int(input())
arr = list(map(int, input().split()))

p = [0] * N
visited = [0] * N

max_diff = 0
perm(N, 0)

print(max_diff)
