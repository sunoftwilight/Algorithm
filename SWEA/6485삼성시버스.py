T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 정류장별 노선 세기
    cnt = [0] * 5001

    for num in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            cnt[i] += 1

    P = int(input())

    # P개의 입력 받기 (정류장 넘버)
    chk_bus_stop = []

    for n in range(P):
        chk_bus_stop.append(int(input()))

    # 정류장 넘버(chk_bus_stop)에 대한 노선 개수 출력
    ans = []

    for stop_num in chk_bus_stop:
        ans.append(cnt[stop_num])

    print(f'#{tc}', *chk_bus_stop)
