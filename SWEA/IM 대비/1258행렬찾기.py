T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    row = 1
    col = 0
    i = j = 0

    ans = []

    while 0 <= i < N and 0 <= j < N:
        if arr[i][j] != 0:
            col += 1
            arr[i][j] = 0
            j += 1

            if (0 <= j < N and arr[i][j] == 0) or j >= N:
                j -= 1
                i += 1
                while arr[i][j] != 0:
                    row += 1
                    for k in range(col):
                        arr[i][j-k] = 0
                    i += 1
                ans.append([row, col])

                i -= row
                j += 1
                row = 1
                col = 0

        elif arr[i][j] == 0:
            j += 1

        if j >= N:

            j = 0
            i += 1

    area = []
    for i, j in ans:
        area.append([i * j, i, j])

    area.sort()

    for i in range(1, len(area)):
        if area[i-1][0] == area[i][0]:
            if area[i-1][1] > area[i][1]:
                area[i-1], area[i] = area[i], area[i-1]

    print(f'#{tc} {len(ans)}', end=' ')
    for k, i, j in area:
        print(i, j, end=' ')
    print()
