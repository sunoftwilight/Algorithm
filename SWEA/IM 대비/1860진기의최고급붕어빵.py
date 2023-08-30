T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())      # N 손님 수, M초 마다 K개 생산
    when = list(map(int, input().split()))

    when.sort()

    time = [0] * (max(when) + 1)

    for i in range(len(time)):
        if i and i % M == 0:
            time[i] += K

    ans = "Possible"

    for i in when:
        sum_bung = 0

        for k in range(i+1):
            sum_bung += time[k]

        if sum_bung > 0:
            time[i] -= 1

        else:
            ans = "Impossible"
            break

    print(f'#{tc} {ans}')
