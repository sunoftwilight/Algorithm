T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))

    for i in range(M):
        tmp = Q.pop(0)
        Q.append(tmp)

    print(f'#{tc} {Q[0]}')