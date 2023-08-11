T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행
    max_row = 0

    for k in range(N):
        cnt = 0
        j = 0
        while j < M:
            if arr[k][j] == 1:
                cnt += 1

                if (j+1 < M and arr[k][j+1] == 0) or j == M-1:
                    if max_row < cnt:
                        max_row = cnt
                    cnt = 0

            j += 1

    # 열
    max_col = 0

    for k in range(M):
        cnt = 0
        j = 0
        while j < N:
            if arr[j][k] == 1:
                cnt += 1

                if (j+1 < N and arr[j+1][k] == 0) or j == N-1:
                    if max_col < cnt:
                        max_col = cnt
                    cnt = 0

            j += 1

    ans = max_row

    if ans < max_col:
        ans = max_col

    print(f'#{tc} {ans}')
    # print(max_row, max_col)
