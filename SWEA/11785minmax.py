# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     ans = max(arr) - min(arr)
#
#     print(f'#{tc} {ans}')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_val = max_val = arr[0]

    for i in range(1, N):
        if min_val > arr[i] :
            min_val = arr[i]
        if max_val < arr[i] :
            max_val = arr[i]

    ans = max_val - min_val

    print(f'#{tc} {ans}')
