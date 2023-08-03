T = 10

for tc in range(1, T+1):
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    of_sum = []

    # 각 행의 합
    for i in range(N):
        sum_row = 0
        for j in range(N):
            sum_row += arr[i][j]
        of_sum.append(sum_row)
        print(sum_row)

    # 각 열의 합
    for i in range(N):
        sum_col = 0
        for j in range(N):
            sum_col += arr[j][i]
        of_sum.append(sum_col)
        print(sum_col)

    # 왼쪽 출발 대각선
    sum_left = 0
    for k in range(N):
        sum_left += arr[k][k]
    of_sum.append(sum_left)

    # 오른쪽 출발 대각선
    sum_right = 0
    for k in range(N):
        sum_right += arr[k][(N-1)-k]
    of_sum.append(sum_right)

    # sum_sort = sorted(of_sum)

    max_sum = 0
    for ms in of_sum:
        if max_sum < ms:
            max_sum = ms

    print(f'#{tc} {max_sum}')