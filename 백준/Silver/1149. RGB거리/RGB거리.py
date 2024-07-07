N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

# dp 배열 초기화
dp = [[0] * 3 for _ in range(N)]

# 첫 번째 집의 비용 설정
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

# dp 테이블 채우기
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

# 최종 결과는 마지막 집을 빨강, 초록, 파랑으로 칠할 때의 최소 비용 중 가장 작은 값
answer = min(dp[N-1][0], dp[N-1][1], dp[N-1][2])

print(answer)
