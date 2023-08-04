T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    N2 = N ** 2

    k = 0
    i = j = 0
    num = 1
    for _ in range(N * N):
        arr[i][j] = num

        ni = i + di[k]
        nj = j + dj[k]

        # 방향을 전환할 조건 :
        if 0 > ni or ni >= N or 0 > nj or nj >= N or arr[ni][nj] != 0:
            k = (k+1) % 4

            ni = i + di[k]
            nj = j + dj[k]

        i = ni
        j = nj
        num += 1
    print()