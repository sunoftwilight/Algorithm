N = int(input())
answer = 0

for a in range(1, N + 1):
    for b in range(1, N + 1 - a):
        for c in range(1, N + 1 - a - b):
            if a + b + c == N and not a % 2 and c >= b + 2:
                answer += 1

print(answer)