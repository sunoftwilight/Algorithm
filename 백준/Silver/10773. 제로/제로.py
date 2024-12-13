K = int(input())
nums = []

for _ in range(K):
    num = int(input())

    if not num:
        nums.pop()

    else:
        nums.append(num)

print(sum(nums))