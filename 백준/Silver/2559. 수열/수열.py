A, B = map(int, input().split())
nums = list(map(int, input().split()))

answer = float("-inf")
tmp = sum(nums[: B])

for i in range(0, A - B):
    answer = max(answer, tmp)
    tmp = tmp - nums[i] + nums[i + B]

print(max(tmp, answer))
