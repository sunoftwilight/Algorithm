T = int(input())

for tc in range(1, T+1):
    N = int(input())
    time = []

    for _ in range(N):
        time.append(list(map(int, input().split())))

    time.sort(key=lambda x: x[1])
    time = [[0, 0]] + time

    ans = 0
    j = 0

    for i in range(1, N+1):
        if time[i][0] >= time[j][1]:
            ans += 1
            j = i

    print(f'#{tc} {ans}')
