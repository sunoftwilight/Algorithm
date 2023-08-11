# 파스칼 삼각형 점화식
# m[i][j] = m[i-1][j-1] + m[i-1][j]

size = 100
memo = [[0] * size for _ in range(size)]

for i in range(size):
    for j in range(i+1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')

    for i in range(N):
        for j in range(i+1):
            print(f'{memo[i][j]}', end=' ')
        print()
