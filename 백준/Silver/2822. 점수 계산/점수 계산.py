arr = [(int(input()), i) for i in range(1, 9)]
arr.sort(reverse=True)

score = 0
nums = []

for i in range(5):
    score += arr[i][0]
    nums.append(arr[i][1])

nums.sort()
nums = list(map(str, nums))

print(score)
print(' '.join(nums))
