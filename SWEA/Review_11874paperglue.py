# 재귀
def f(n):
    if n <= 1:
        return 1

    else:
        return f(n - 1) + 2 * f(n - 2)


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc} {f(N // 10)}')


# DP
memo = [1, 1]

for i in range(2, 31):
    memo.append(memo[i-1] + 2 * memo[i-2])


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc} {memo[N // 10]}')

