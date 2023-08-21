T = 10

for tc in range(1, T + 1):
    no = int(input())
    Q = list(map(int, input().split()))

    cnt = 0

    while True:
        tmp = Q.pop(0)          # 디큐
        tmp -= cnt % 5 + 1      # 감소

        if tmp < 0:             # 검사
            tmp = 0

        Q.append(tmp)           # 엔큐
        cnt += 1

        if tmp == 0:
            break

    print(f'#{tc}', *Q)
