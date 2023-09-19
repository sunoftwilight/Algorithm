def solve(v, cnt):
    global ans

    # 가지 치기
    if cnt >= ans:
        return

    # 기저 조건 (목적지에 도착하거나 더 넘어가면 종료)
    if v >= N:
        ans = min(ans, cnt)
        return

    else:
        i = 1
        # 충전지 값만큼만 더 갈수 있음
        while i <= arr[v]:
            solve(v + i, cnt + 1)
            i += 1


T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    N = arr[0]
    ans = 9999999

    solve(1, 0)

    print(f'#{tc} {ans-1}')
