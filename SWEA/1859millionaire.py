T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pri = list(map(int, input().split()))

    total = 0

    max_idx = N-1

    for i in range(N-1, -1, -1):
        if pri[max_idx] < pri[i]:
            max_idx = i

        else:
            total += pri[max_idx] - pri[i]

    print(f'#{tc} {total}')
