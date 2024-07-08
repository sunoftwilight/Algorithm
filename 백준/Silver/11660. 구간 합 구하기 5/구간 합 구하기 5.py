import sys
input = sys.stdin.readline

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

cumulative_sum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        # (0, 0) ~ (i, j) 직사각형 누적합 = 상 + 좌 + me - 좌상
        cumulative_sum[i][j] = (cumulative_sum[i-1][j] + cumulative_sum[i][j-1]
                                + table[i-1][j-1] - cumulative_sum[i-1][j-1])

for tc in range(M):
    r1, c1, r2, c2 = map(int, input().split())

    # (r1, c1) ~ (r2, c2) 직사각형 누적합 = r2, c2까지 누적합 - r1, c2 이전까지 행의 누적합
    #                                     - r2, c1 이전까지 열의 누적합 + r1, c1까지의 누적합
    result = (cumulative_sum[r2][c2] - cumulative_sum[r1-1][c2]
              - cumulative_sum[r2][c1-1] + cumulative_sum[r1-1][c1-1])

    print(result)
