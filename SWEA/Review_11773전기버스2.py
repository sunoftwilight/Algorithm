def dfs(n, k, e, c):
    global ans

    if ans <= c:
        return

    if n == k:
        if ans < c:
            ans = c
            return

    else:
        # 충전 O
        dfs(n, k + 1, arr[k] - 1, c + 1)

        # 충전 X, e가 0보다는 커야한다.
        if e > 0:
            dfs(n, k + 1, e - 1, c)


T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    ans = 9999999
    dfs(arr[0], 2, arr[1]-1, 0)

    print(f'#{tc} {ans}')
