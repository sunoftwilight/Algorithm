def trans(N):
    global ans
    cnt = 0

    while N % 2 != 0.0:
        N *= 2
        ans.append(int(N // 1))
        cnt += 1
        N = N - (N // 1)

        if cnt >= 13:
            ans = 'overflow'
            break

    return ans


T = int(input())

for tc in range(1, T+1):
    N = float(input())
    ans = []

    trans(N)

    print(f'#{tc}', end=' ')
    for i in ans:
        print(i, end='')
    print()