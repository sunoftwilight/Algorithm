N = int(input())
scores = list(map(int, input().split(' ')))

total = 0
M = max(scores)

for score in scores:
    total += (score / M) * 100

print(total / N)
