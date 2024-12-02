nums = []

for i in range(1, 10):
    nums.append((int(input()), i))

nums.sort()

print(nums[-1][0])
print(nums[-1][1])