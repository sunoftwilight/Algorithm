N, K = map(int, input().split())
ans = 1

for i in range(K+1, N+1):
    ans *= i

for j in range(1, N-K+1):
    ans //= j
    
print(ans)
