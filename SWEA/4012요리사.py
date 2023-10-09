def solve(k, v):
    global ans

    if k == N // 2:
        A = []
        B = []

        for i in range(N):
            if visited[i] == 1:
                A.append(i)
            else:
                B.append(i)
        print(A, B)
        A_sum = B_sum = 0

        for i in range(N // 2):
            for j in range(N // 2):
                A_sum += ingredient[A[i]][A[j]]
                B_sum += ingredient[B[i]][B[j]]

        sub = abs(A_sum - B_sum)
        ans = min(sub, ans)

        return

    else:
        for j in range(v, N):
            if visited[j] == 0:
                visited[j] = 1
                solve(k+1, j+1)
                visited[j] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ingredient = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N)

    ans = 99999999
    solve(0,0)

    print(f'#{tc} {ans}')
