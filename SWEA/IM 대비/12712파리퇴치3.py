T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    max_sum = 0

    for i in range(N):
        for j in range(N):
            sum_one = arr[i][j]

            for k in range(0, 8, 2):
                for p in range(1, M):
                    ni = i + di[k] * p
                    nj = j + dj[k] * p

                    if 0 <= ni < N and 0 <= nj < N:
                        sum_one += arr[ni][nj]

            if max_sum < sum_one:
                max_sum = sum_one

            sum_two = arr[i][j]

            for k in range(1, 8, 2):
                for p in range(1, M):
                    ni = i + di[k] * p
                    nj = j + dj[k] * p

                    if 0 <= ni < N and 0 <= nj < N:
                        sum_two += arr[ni][nj]

            if max_sum < sum_two:
                max_sum = sum_two

    print(f'#{tc} {max_sum}')
