N = int(input())
arr = list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(N):                      # 누적합
    prefix[i + 1] = max(prefix[i] + arr[i], arr[i])

print(max(prefix[1:]))