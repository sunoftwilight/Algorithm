def paper(N):
    n = N // 10
    f = [0] * (n + 1)
    f[0] = f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + 2 * f[i-2]

    return f[n]


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc} {paper(N)}')
