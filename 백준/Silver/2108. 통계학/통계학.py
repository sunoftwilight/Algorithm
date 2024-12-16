import sys

N = int(input())
nums = [int(sys.stdin.readline().strip()) for _ in range(N)]

nums.sort()
cnt = dict()

for num in nums:
    cnt[num] = cnt.get(num, 0) + 1

most = 0
mosts = []

for key, value in cnt.items():
    if most < value:
        most = value
        mosts = [key]

    elif most == value:
        mosts.append(key)

if len(mosts) > 1:
    mosts.sort()

avg = int(round(sum(nums) / N, 0))
mid = nums[N // 2]
mode = mosts[0] if len(mosts) == 1 else mosts[1]
scope = max(nums) - min(nums)

print(avg)
print(mid)
print(mode)
print(scope)
