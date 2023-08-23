T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    arr = []

    for i in range(N-1):
        for j in range(i+1, N):
            arr.append(str(num[i] * num[j]))

    for k in range(len(arr)):
        for i in range(len(arr[k])):
            for j in range(i):
                if int(arr[k][i]) < int(arr[k][j]):
                    arr[k] = 0
                    break

    for m in range(len(arr)):
        arr[m] = int(arr[m])
    arr.sort()
    ans = arr[-1]

    print(f'#{tc} {ans}')
