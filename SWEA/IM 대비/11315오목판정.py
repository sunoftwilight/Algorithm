T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    di = [0, 1, 1, 1]   # 우, 하, 우하, 좌하
    dj = [1, 0, 1, -1]

    ans = "NO"

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    cnt = m = 1
                    ni = nj = 0

                    while 0 <= ni < N and 0 <= nj < N:
                        ni = i + di[k] * m
                        nj = j + dj[k] * m

                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'o':
                                cnt += 1
                                m += 1
                            else:
                                break
                        else:
                            break

                    if cnt == 5:
                        ans = "YES"

    print(f'#{tc} {ans}')
