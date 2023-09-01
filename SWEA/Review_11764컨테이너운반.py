T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))    # 컨테이너
    t = list(map(int, input().split()))    # 트럭

    w.sort(reverse=True)
    t.sort(reverse=True)

    i = j = ans = 0

    while i < N and j < M:
        if w[i] <= t[i]:
            ans += w[i]
            i, j = i+1, j+1

        else:
            i += 1

    print(f'#{tc} {ans}')
