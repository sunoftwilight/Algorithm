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

<<<<<<< HEAD
    for k in range(len(arr)):
        for i in range(1, len(arr[k])):
            flag = 0
            for j in range(i):
                if int(arr[k][i]) < int(arr[k][j]):
                    arr[k] = '-1'
                    flag = 1
                    break
            if flag:
                break

    arr = list(map(int, arr))
=======
    ans = 0

    for i in range(len(arr)):
        digit(arr[i])
        if ans == -1:
            arr[i] = -1
            ans = 0
>>>>>>> e6d7fdef79a5731897df98a02c4d1bc4dc214a78

    arr.sort()
    ans = arr[-1]

    print(f'#{tc} {ans}')
