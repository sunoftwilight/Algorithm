N = int(input())
num = list(map(int, input().split()))

ans = []

for i in range(1, N+1):
    ans.insert(len(ans)-num[i-1], i)

print(*ans)
