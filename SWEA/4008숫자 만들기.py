def solve(k, result, add, sub, mul, div):    # 원소 개수 n, depth k
    global min_r, max_r

    if k == N:
        min_r = min(min_r, result)
        max_r = max(max_r, result)
        return

    else:
        if add:
            solve(k + 1, result + arr[k], add - 1, sub, mul, div)
        if sub:
            solve(k + 1, result - arr[k], add, sub - 1, mul, div)
        if mul:
            solve(k + 1, result * arr[k], add, sub, mul - 1, div)
        if div:
            solve(k + 1, int(result / arr[k]), add, sub, mul, div - 1)



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    add, sub, mul, div = map(int, input().split())
    arr = list(map(int, input().split()))

    min_r = 9999999999
    max_r = -9999999999

    solve(1, arr[0], add, sub, mul, div)

    print(f'#{tc} {max_r-min_r}')