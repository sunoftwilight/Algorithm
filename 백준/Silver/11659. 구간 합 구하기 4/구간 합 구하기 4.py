import sys

N, M = map(int, input().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
scopes = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

sums = [0] * N
sums[0] = nums[0]

for i in range(1, N):
    sums[i] = sums[i - 1] + nums[i]

for s, e in scopes:
    ans = sums[e-1]

    if s != 1:
        ans -= sums[s-2]

    print(ans)