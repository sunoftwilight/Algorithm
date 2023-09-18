def perm(n, k):    # 원소 개수 n, depth k
    global min_r, max_r
    if n == k:
        result = arr[0]

        for i in range(n):
            if op[i] == '+':
                result += arr[i+1]

            elif op[i] == '-':
                result -= arr[i+1]

            elif op[i] == '*':
                result *= arr[i+1]

            else:
                if result >= 0:
                    result //= arr[i+1]
                else:
                    result = -((-result) // arr[i+1])

        min_r = min(min_r, result)
        max_r = max(max_r, result)
        return

    else:
        for i in range(k, n):
            op[k], op[i] = op[i], op[k]
            perm(n, k+1)
            op[k], op[i] = op[i], op[k]


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


min_r = 9999999999
max_r = -9999999999
perm(N-1, 0)

print(max_r)
print(min_r)
