import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def eat_bambu(ci, cj):
    if dp[ci][cj]:
        return dp[ci][cj]

    point = 0
    for di, dj in direct:
        ni, nj = ci + di, cj + dj

        if 0 <= ni < N and 0 <= nj < N and info[ni][nj] > info[ci][cj]:
            dp[ci][cj] = max(dp[ci][cj], eat_bambu(ni, nj) + 1)

    return dp[ci][cj]


N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dp = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        count = eat_bambu(i, j)

print(max(map(max, dp)) + 1)
