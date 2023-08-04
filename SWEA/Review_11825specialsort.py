def selection_sort(arr, n):
    for i in range(10):          # 10개만 정렬할거니까
        min_idx = i
        if i % 2:
            for j in range(i+1, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
        else:
            for j in range(i+1, n):
                if arr[min_idx] < arr[j]:
                    min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    selection_sort(num, N)

    print(f'#{tc}', end=' ')
    for i in range(10):
        print(num[i], end=' ')
    print()