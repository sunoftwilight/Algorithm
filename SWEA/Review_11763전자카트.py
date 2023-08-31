def calc(cursum):
    global ans
    # 가지치기 없는 버전
    # total = 0
    # for i in range(N):
    #     total += dist[p[i]][p[i+1]]     # p = [0, 1, 2, 0] 이면, 0 -> 1로 갈때의 비용 : dist[0][1]이므로 !!
    #
    # ans = min(ans, total)

    # 가지치기를 위해 하나씩 더해가며 확인
    cursum += dist[p[N-1]][p[N]]          # 0 - 1 - 2 까지만 포함됨 => 2 - 0도 추가해주기
    ans = min(ans, cursum)


def perm(n, k, cursum):
    if ans < cursum: return               # 가지치기

    if n == k:
        calc(cursum)

    else:
        for i in range(n):
            if v[i] == 0:
                v[i] = 1
                p[k] = A[i]
                perm(n, k+1, cursum + dist[p[k-1]][p[k]])
                v[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    dist = [list(map(int, input().split())) for _ in range(N)]

    A = list(range(N))
    p = [0] * N + [0]                          # 0 1 2 0 으로 저장 (출발, 도착 = 1번 지점(=인덱스 0)으로 고정)
    v = [0] * N
    v[0] = 1                                   # 0번은 제외

    ans = 999999999
    perm(N, 1, 0)

    print(f'#{tc} {ans}')
