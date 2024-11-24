N = int(input())
counsel = [list(map(int, input().split())) for _ in range(N)]

dp = [False] * N
dp[-1] = counsel[-1][1] if counsel[-1][0] == 1 else 0

for i in range(N-2, -1, -1):
    if counsel[i][0] + i > N:
        dp[i] = dp[i+1]

    elif counsel[i][0] + i >= N:
        dp[i] = max(dp[i+1], counsel[i][1])

    else:
        dp[i] = max(counsel[i][1] + dp[i + counsel[i][0]], dp[i+1])

print(max(dp))
