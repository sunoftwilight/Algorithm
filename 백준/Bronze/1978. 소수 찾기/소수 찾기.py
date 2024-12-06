N = int(input())
nums = list(map(int, input().split()))
answer = 0

for num in nums:
    if num == 1:
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        answer += 1

print(answer)