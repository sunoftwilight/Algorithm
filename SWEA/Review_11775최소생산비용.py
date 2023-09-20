def perm(n, k, cursum):
    global ans

    if ans <= cursum:
        return

    if n == k:
        if ans > cursum:
            ans = cursum
        return

    else:
        for i in range(n):
            if visited[i]:
                continue

            visited[i] = 1
            p[k] = i
            perm(n, k + 1, cursum + arr[k][p[k]])
            visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    p = [0] * N
    ans = 987654321
    perm(N, 0, 0)
    print(f'#{tc} {ans}')
