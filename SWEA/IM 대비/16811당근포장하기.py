T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    # i = N - 1
    # new = []
    # while 0 <= i < N:
    #     tmp = []
    #     while arr[i] == arr[i-1]:
    #         tmp.append(arr[i])
    #         if i-1 == 0:
    #             tmp.append(arr[i-1])
    #         i -= 1
    #     if tmp:
    #         new.append(tmp)
    #     else:
    #         new.append(arr[i])
    #     i -= 1
    #
    # new.reverse()

    m = len(arr)
    while m % 3:
        m += 1
    m //= 3

    i = m
    j = 2 * m

    for k in range(N-1):
        if arr[k] == arr[i+1]:
            i += 1
            j += 1

    ans = -1

    small = arr[0:i]
    mid = arr[i:j]
    large = arr[j:N]
    print('s',small)
    print('m',mid)
    print('l',large)


