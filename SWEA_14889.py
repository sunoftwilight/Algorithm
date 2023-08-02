T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    sum_all = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    #sum_all += abs(arr[i][j] - arr[ni][nj])
                    if arr[i][j] - arr[ni][nj] > 0:
                        sum_all += arr[i][j] - arr[ni][nj]
                    else:
                        sum_all += arr[ni][nj] - arr[i][j]

    print(f'#{tc} {sum_all}')