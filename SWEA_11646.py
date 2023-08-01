T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    num = list(map(int, input().split()))

    sum_init = 0

    for n in range(M):
        sum_init += num[n]

    max_sum = min_sum = sum_init


    for i in range(N-(M-1)):
        sum = 0
        for k in range(M):
            sum += num[i+k]

        if max_sum < sum:
            max_sum = sum

        if min_sum > sum:
            min_sum = sum

    result = max_sum - min_sum

    print(f'#{test_case}', result)