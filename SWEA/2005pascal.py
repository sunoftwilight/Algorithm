# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#
#     psc = [[''] * i for i in range(1, N+1)]
#
#     for i in range(N):
#         psc[i][0] = 1
#
#     i = 1
#     while 0 < i < N:
#         for j in range(1, len(psc[i])):
#             if j == len(psc[i])-1:
#                 psc[i][j] = 1
#
#             else:
#                 psc[i][j] = psc[i-1][j-1] + psc[i-1][j]
#
#         i += 1
#
#     print(f'#{tc}')
#     for i in range(N):
#         print(*psc[i])


def pascal(N):
    memo = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if j == 0 or j == i:
                memo[i][j] = 1

            else:
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

    return memo


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = pascal(N)

    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()

