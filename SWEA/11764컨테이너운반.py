T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    W = list(map(int, input().split()))
    W.sort(reverse=True)

    T = list(map(int, input().split()))
    T.sort(reverse=True)

    i = j = ans = 0

    while 0 <= j < M and 0 <= i < N:

        if W[i] <= T[j]:
            ans += W[i]
            i += 1
            j += 1

        else:
            i += 1

    print(f'#{tc} {ans}')
