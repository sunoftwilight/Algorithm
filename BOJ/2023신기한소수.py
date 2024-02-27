import sys; sys.setrecursionlimit(10 ** 6)

def prime(num):
    if num == 1:
        return False

    for k in range(2, num):      # 2부터 (x - 1)까지의 모든 수를 확인하며
        if num % k == 0:         # x가 해당 수로 나누어 떨어진다면
            return False         # 소수가 아님
    return num


def dfs(num, depth):
    if depth > N: return

    if depth == N:
        is_prime = [False] * N + [True]
        # for m in range(1, N+1):
        #     part = int(num[ :m])
        for m in range(N):
            part = num // 10 ** m
            check = prime(part)

            if not check: return

            is_prime[m] = True

        if is_prime.count(True) == N+1:
            print(num)

        else: return

    else:
        for j in num_list:
            dfs(num + j * (10 ** (N-depth-1)), depth + 1)


N = int(input())
# num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num_list:
    dfs(i * (10 ** (N-1)), 1)
