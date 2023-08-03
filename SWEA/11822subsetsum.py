T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, T+1):
    N, K = map(int, input().split())

    cnt = 0

    for i in range(1 << 12):
        sub_set = []
        total = 0
        for j in range(12):
            if i & (1 << j):
                sub_set.append(A[j])

        for k in range(len(sub_set)):
            total += sub_set[k]

        if total == K and len(sub_set) == N:
            cnt += 1

    print(f'#{tc} {cnt}')
