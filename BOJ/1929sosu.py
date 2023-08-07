# 시간 초과
# M, N = map(int, input().split())
#
# for num in range(M, N+1):
#     cnt = 0
#
#     for i in range(1, num+1):
#         if num % i == 0:
#             cnt += 1
#         if cnt > 2:
#             break
#
#     if cnt == 2:
#         print(num)


# 시간 초과2

# import math

# M, N = map(int, input().split())
#
# for num in range(M, N+1):
#     cnt = 0
#
#     for i in range(1, int(math.sqrt(num))+1):
#         if num % i == 0:
#             cnt += 1
#         if cnt > 2:
#             break
#
#     if cnt == 1 and num != 1:
#         print(num)


# 에라토스테네스의 체

M, N = map(int, input().split())
a = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N+1):
    if a[i]:
        for j in range(2 * i, N + 1, i):
            a[j] = False
        if i >= M:
            primes.append(i)

for k in range(len(primes)):
    print(primes[k])
