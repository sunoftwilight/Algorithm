N = int(input())
arr = [0] + list(map(int, input().split()))
result = [0] * (N + 1)

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if result[j] == 0 and cnt == arr[i]:
            result[j] = i
            break

        elif result[j] == 0:
            cnt += 1

print(*result[1:])
