T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    arr = []

    for i in range(N-1):
        for j in range(i+1, N):
            arr.append(str(num[i] * num[j]))

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

    arr.sort()
    ans = arr[-1]

    print(f'#{tc} {ans}')
