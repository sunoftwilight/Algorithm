T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    min_idx = 0
    max_idx = 0

    for i in range(N):                   # Live에서는 (1,N)으로 하고
        if nums[i] < nums[min_idx]:
            min_idx = i

        if nums[i] >= nums[max_idx]:     # >로 함 왜??
            max_idx = i

        # ans = abs(max_idx - min_idx)
        if max_idx > min_idx :
            ans = max_idx - min_idx
        else :
            ans = min_idx - max_idx

        # if ans < 0:
        #     ans *= (-1)

    print(f'#{test_case} {ans}')
