def digit(a):
    global ans
    if a < 10:
        return
    s = a % 10
    d = a // 10

    if d > s:
        ans = -1
        return ans

    return digit(d)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    arr = []

    for i in range(N-1):
        for j in range(i+1, N):
            arr.append(num[i] * num[j])

    ans = 0

    for i in range(len(arr)):
        digit(arr[i])
        if ans == -1:
            arr[i] = -1
            ans = 0

    arr.sort()
    ans = arr[-1]

    print(f'#{tc} {ans}')
