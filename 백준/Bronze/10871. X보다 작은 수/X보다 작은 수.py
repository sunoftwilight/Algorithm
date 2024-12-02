N, X = map(int, input().split())
nums = list(map(int, input().split()))

lows = []
for num in nums:
    if num < X:
        lows.append(num)

print(*lows)