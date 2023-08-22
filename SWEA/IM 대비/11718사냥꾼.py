T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                for k in range(8):
                    m = 1
                    ni = nj = 0
                    while 0 <= (i + di[k] * m) < N and 0 <= (j + dj[k] * m) < N:
                        ni = i + di[k] * m
                        nj = j + dj[k] * m

                        if arr[ni][nj] == 2:
                            cnt += 1
                            m += 1

                        elif arr[ni][nj] == 3:
                            break

                        else:
                            m += 1

    print(f'#{tc} {cnt}')
