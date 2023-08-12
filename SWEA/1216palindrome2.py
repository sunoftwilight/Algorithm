import sys; sys.stdin = open('1216_input.txt')

def row(arr):
    M = N

    while M > 0:
        for i in range(N):
            for j in range(N - M + 1):
                flag = 1
                for k in range(M // 2):
                    if arr[i][j + k] != arr[i][j + (M - 1) - k]:
                        flag = 0
                        break

                if flag:
                    return M
        M -= 1


def col(arr):
    M = N

    while M > 0:
        for i in range(N):
            for j in range(N - M + 1):
                flag = 1
                for k in range(M // 2):
                    if arr[j + k][i] != arr[j + (M - 1) - k][i]:
                        flag = 0
                        break

                if flag:
                    return M
        M -= 1


T = 10

for tc in range(1, T+1):
    no = int(input())
    N = 100
    arr = [input() for _ in range(N)]

    max_row = row(arr)
    max_col = col(arr)

    max_len = max_row

    if max_len < max_col:
        max_len = max_col

    print(f'#{tc} {max_len}')
