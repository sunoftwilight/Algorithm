def dfs(x, y, cursum):
    global ans

    # 가지치기
    if ans <= cursum:
        return

    if x == N-1 and y == N-1:
        ans = min(ans, cursum)

    else:
        if x+1 < N:
            dfs(x+1, y, cursum + arr[x+1][y])

        if y+1 < N:
            dfs(x, y+1, cursum + arr[x][y+1])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 999999999
    dfs(0, 0, arr[0][0])

    print(f'#{tc} {ans}')
