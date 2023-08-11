def paper(N):
    n = N // 10
    f = [0] * (n + 1)
    f[0] = f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + 2 * f[i-2]
        # 홀수*10만큼 커지면 앞의 형태에다가 | 형태만 덧붙이기 가능
        # 짝수*10 만큼 커지면 앞의 형태에다가 ㅁ or = 형태로 덧붙이기 가능
        # (||는 중복되므로 불가)

    return f[n]


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc} {paper(N)}')
