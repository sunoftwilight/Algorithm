T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    cnt = 0
    max_cnt = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            cnt += 1
        if nums [i] == 0:
            max_cnt = cnt
            cnt = 0
