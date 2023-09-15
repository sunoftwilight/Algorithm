def perm(n, k):    # 원소 개수 n, depth k
    global min_r, max_r
    if n == k:
        final = []
        for i in range(2*N-1):
            if i % 2 == 0:
                final.append(str(arr[i//2]))
            else:
                final.append(str(p[i]))
        result = eval(''.join(final))
        min_r = min(min_r, result)
        max_r = max(max_r, result)
        return

    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = op[i]
                perm(n, k+1)
                visited[i] = 0


N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
op = []


for _ in range(add):
    op.append('+')

for _ in range(sub):
    op.append('-')

for _ in range(mul):
    op.append('*')

for _ in range(div):
    op.append('/')

p = [0] * (N-1)
visited = [0] * (N-1)
min_r = 9999999999
max_r = 0
perm(N-1, 0)

print(min_r)
print(max_r)
