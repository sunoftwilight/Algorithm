N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

ans = 0

if N < 3 or M < 3:
    if A != B:
        ans = -1
else:
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                ans += 1
                for k in range(i, i+3):
                    for m in range(j, j+3):
                        if A[k][m]:
                            A[k][m] = 0
                        else:
                            A[k][m] = 1
            if i == N-3 and j == M-3 and A != B:
                ans = -1

print(ans)
