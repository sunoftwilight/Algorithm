T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    board = [[0] * (N+1) for _ in range(N+1)]

    board[N//2][N//2] = board[N//2+1][N//2+1] = 2
    board[N//2][N//2+1] = board[N//2+1][N//2] = 1

    arr = [list(map(int, input().split())) for _ in range(M)]

    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    for i in range(M):
        board[arr[i][1]][arr[i][0]] = arr[i][2]
        for j in range(8):
            ni = arr[i][1] + di[j]
            nj = arr[i][0] + dj[j]

            if 0 < ni < N+1 and 0 < nj < N+1:
                if board[ni][nj] and board[ni][nj] != arr[i][2]:
                    m = 1
                    while 0 < ni < N+1 and 0 < nj < N+1:
                        ni = arr[i][1] + di[j] * m
                        nj = arr[i][0] + dj[j] * m

                        if 0 < ni < N+1 and 0 < nj < N+1:
                            if board[ni][nj] == arr[i][2]:
                                m = 0
                                while 0 < ni < N+1 and 0 < nj < N+1 and not(ni == arr[i][1] and nj == arr[i][0]):
                                    m += 1
                                    ni -= di[j] * m
                                    nj -= dj[j] * m

                                    if ni == arr[i][1] and nj == arr[i][0]:
                                        break
                                    if 0 < ni < N+1 and 0 < nj < N+1:
                                        board[ni][nj] = arr[i][2]
                                break
                            else:
                                m += 1

    cnt_b = 0
    cnt_w = 0

    for i in range(N+1):
        for j in range(N+1):
            if board[i][j] == 1:
                cnt_b += 1
            elif board[i][j] == 2:
                cnt_w += 1

    print(f'#{tc} {cnt_b} {cnt_w}')
