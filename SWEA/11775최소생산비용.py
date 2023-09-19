def solve(k, sum_cost):
    global ans

    if sum_cost > ans:
        return

    if k == N:
        ans = min(ans, sum_cost)
        return

    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                solve(k + 1, sum_cost + cost[k][i])
                visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    ans = 999999999

    solve(0, 0)
    print(f'#{tc} {ans}')
