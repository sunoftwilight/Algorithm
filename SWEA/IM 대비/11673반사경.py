T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    i = j = 0
    cnt = 0

    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 우 하 좌 상
    di, dj = delta[0]

    while 0 <= i < N and 0 <= j < N:
        if arr[i][j] == 1:
            cnt += 1

            if di == 0 and dj == 1:
                di, dj = delta[3]

            elif di == 0 and dj == -1:
                di, dj = delta[1]

            elif di == 1 and dj == 0:
                di, dj = delta[2]

            elif di == -1 and dj == 0:
                di, dj = delta[0]

        elif arr[i][j] == 2:
            cnt += 1

            if di == 0 and dj == 1:
                di, dj = delta[1]

            elif di == 0 and dj == -1:
                di, dj = delta[3]

            elif di == 1 and dj == 0:
                di, dj = delta[0]

            elif di == -1 and dj == 0:
                di, dj = delta[2]

        i += di
        j += dj

    print(f'#{tc} {cnt}')
