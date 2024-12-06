N = int(input())

answer = 0

for n in range(1, N+1):
    num = list(map(int, str(n)))
    div_sum = n + sum(num)

    if div_sum == N:
        answer = n
        break

print(answer)