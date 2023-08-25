T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    sum_get = 0

    for i in range(N//2 + 1):
        sum_get += sum(farm[i][(N // 2) - i: (N // 2) + i + 1])

        if i != N // 2 :
            sum_get += sum(farm[N-1-i][(N//2)-i : (N//2)+i+1])

    print(f'#{tc} {sum_get}')
