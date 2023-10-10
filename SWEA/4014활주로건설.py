def solve(arr):
    global ans

    cnt = 1
    for i in range(1, N):
        if arr[i-1] == arr[i]:
            cnt += 1
        elif arr[i-1] + 1 == arr[i] and cnt >= X:
            cnt = 1
        elif arr[i-1] - 1 == arr[i] and cnt >= 0:
            cnt = - X + 1
        else:
            return

    if cnt >= 0:
        ans += 1
    return


T = int(input())

for tc in range(1, T+1):
    N, X = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]

    rvs_info = [[0] * N for _ in range(N)]
    for m in range(N):
        for n in range(N):
            rvs_info[n][m] = info[m][n]

    ans = 0
    for i in range(N):
        solve(info[i])
        solve(rvs_info[i])

    print(f'#{tc} {ans}')
