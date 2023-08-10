T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pri = list(map(int, input().split()))

    total = 0
    cnt = 0

    for i in range(N):
        if i <= N-2 and pri[i] < pri[i+1]:
            total -= pri[i]
            cnt += 1

        elif pri[i] > pri[i+1] and min(pri) == :
            total += pri[i] * cnt
            cnt = 0

    print(f'#{tc} {total}')
