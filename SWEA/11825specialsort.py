def selection_sort(arr, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    num = selection_sort(num, N)

    special = []

    for i in range(1, 11):
        if i % 2 == 1:
            special.append(num[(N-1) - i // 2])
        else:
            special.append(num[i // 2 - 1])

    print(f'#{tc}', *special)
