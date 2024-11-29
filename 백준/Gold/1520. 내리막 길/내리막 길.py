import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def go(ci, cj):
    if ci == N - 1 and cj == M - 1:
        return 1

    if dp[ci][cj] != -1:
        return dp[ci][cj]

    route = 0
    for di, dj in direct:
        ni, nj = ci + di, cj + dj

        if 0 <= ni < N and 0 <= nj < M and info[ni][nj] < info[ci][cj]:
            route += go(ni, nj)

    dp[ci][cj] = route

    return dp[ci][cj]


N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dp = [[-1] * M for _ in range(N)]

answer = go(0, 0)

print(answer)
