di = [0, 1]
dj = [1, 0]


def dfs(i, j, sum_v):
    global min_v

    if sum_v > min_v:
        return

    if i == N-1 and j == N-1:
        min_v = min(min_v, sum_v)

    for m in range(2):
        ni = i + di[m]
        nj = j + dj[m]

        if 0 <= ni < N and 0 <= nj < N:
            sum_t = sum_v + arr[ni][nj]
            dfs(ni, nj, sum_t)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_v = 999999999

    dfs(0, 0, arr[0][0])

    print(f'#{tc} {min_v}')
