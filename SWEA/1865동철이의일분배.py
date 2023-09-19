def solve(k, sum_pro):
    global ans

    if sum_pro <= ans:
        return

    if k == N:
        ans = max(ans, sum_pro)
        return

    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                solve(k + 1, sum_pro * pro[k][i] * 0.01)
                visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pro = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    visited = [0] * N

    solve(0, 1)

    print(f'#{tc} {ans*100:.6f}')
