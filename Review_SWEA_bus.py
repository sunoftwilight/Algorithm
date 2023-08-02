T = int(input())

for tc in range(1, T+1):
    N = int(input())

    cnt = [0] * 5001

    # 정류장별 노선 세기
    for num in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            cnt[i] += 1

    P = int(input())

    # P개의 입력 받기 (정류장 넘버)
    chk_bus_stop = []

    for _ in range(P):
        p = int(input())
        chk_bus_stop.append(cnt[p])

    print(f'#{tc}', *chk_bus_stop)
