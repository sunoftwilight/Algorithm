T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(input()) for _ in range(N)]
    cnted = [[1] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    all_h = 0
    cover = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                pass

            elif arr[i][j] == 'H':
                all_h += 1

            else:
                for k in range(4):
                    if arr[i][j] == 'A':
                        ni = i + di[k]
                        nj = j + dj[k]

                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'H' and cnted[ni][nj]:
                            cover += 1
                            cnted[ni][nj] = 0

                    elif arr[i][j] == 'B':
                        for m in range(1, 3):
                            ni = i + di[k] * m
                            nj = j + dj[k] * m

                            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'H' and cnted[ni][nj]:
                                cover += 1
                                cnted[ni][nj] = 0

                    elif arr[i][j] == 'C':
                        for m in range(1, 4):
                            ni = i + di[k] * m
                            nj = j + dj[k] * m

                            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'H' and cnted[ni][nj]:
                                cover += 1
                                cnted[ni][nj] = 0

    print(f'#{tc} {all_h - cover}')
