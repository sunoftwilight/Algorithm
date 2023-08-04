T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]    # A = list(range(1, 13))

for tc in range(1, T+1):
    N, K = map(int, input().split())

    cnt = 0                                    # ans = 0

    for i in range(1 << 12):
        sub_set = []                           # cnt = 0
        total = 0
        for j in range(12):
            if i & (1 << j):   # i의 비트열 확인
                sub_set.append(A[j])           # cnt += 1 ; sum += arr[j]

        for k in range(len(sub_set)):          # 불필요
            total += sub_set[k]

        if total == K and len(sub_set) == N:   # if cnt == N and total == K
            cnt += 1                           # ans += 1

    print(f'#{tc} {cnt}')
