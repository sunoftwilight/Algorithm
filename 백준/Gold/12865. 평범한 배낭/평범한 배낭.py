def choice(depth, weight):

    if weight > K:                  # 수용 가능 무게를 초과한 경우
        return -9999999999999999    # 최소 가치가 되도록 매우 작은 수 넣기

    if depth == N:                  # depth = 0 ~ N-1까지
        return 0                    # N개의 물건을 모두 탐색한 경우 탐색 종료

    if dp[depth][weight]:           # 이미 해당 값에 대해 연산이 완료된 경우
        return dp[depth][weight]    # 여러번 연산할 필요가 없게 바로 값을 return

    # 물건을 넣는 경우와 안넣는 경우 중 더 이득인 경우를 선택
    dp[depth][weight] = max(choice(depth + 1, weight + things[depth][0]) + things[depth][1], choice(depth + 1, weight))

    return dp[depth][weight]        # 선택 완료 됐다면 해당 값 return


N, K = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(N)]
dp = [[False] * 100_001 for _ in range(N)]      # 행은 물건, 열은 무게

answer = choice(0, 0)

print(answer)
