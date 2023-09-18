def binary_search(target):
    low = 0
    high = len(N_arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if N_arr[mid] > target:
            high = mid - 1

        elif N_arr[mid] < target:
            low = mid + 1

        else:
            return mid


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_arr = list(map(int, input().split()))
    M_arr = list(map(int, input().split()))

    N_arr.sort()

    cnt = 0

    for i in range(M):
        binary_search(M_arr[i])
