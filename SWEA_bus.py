T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    P = int(input())

    # P개의 입력 받기 (정류장 넘버)
    chk_bus_stop = []

    for n in range(P):
        chk_bus_stop.append(int(input()))


    # 정류장별 노선 세기
    cnt = [0] * 5001

    for i in range(a1, b1+1):
        cnt[i] += 1
    print(cnt[0:6])
    for j in range(a2, b2+1):
        cnt[i] += 1
    print(cnt[0:6])
    # 정류장 넘버(chk_bus_stop)에 대한 노선 개수 출력
    ans = []

    for k in chk_bus_stop:
        ans.append(cnt[k])

    print(f'#{tc} ',*ans)
    print(a1, b1, a2, b2)
    print(cnt[0:6])
