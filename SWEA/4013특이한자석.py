def dfs(n, d):
    global chk

    # 방문 체크
    chk[n] = 1

    # 오른쪽 자석과의 관계 확인
    if n < 3:
        # 두 자성이 다르고, 확인한 적 없으면 dfs
        if info[n][2] != info[n+1][6] and not chk[n+1]:
            # n번과는 반대 방향으로 회전하므로 -1 * d
            dfs(n+1, -1 * d)

    # 왼쪽 자석과의 관계 확인
    if n > 0:
        # 두 자성이 다르고, 확인한 적 없으면 dfs
        if info[n][6] != info[n-1][2] and not chk[n-1]:
            # n번과는 반대 방향으로 회전하므로 -1 * d
            dfs(n-1, -1 * d)

    # 시계 방향으로 돌면 맨 뒤의 원소가 맨 앞으로
    if d == 1:
        info[n] = [info[n].pop()] + info[n]

    # 반시계 방향으로 돌면 맨 앞의 원소가 맨 뒤로
    else:
        info[n] = info[n][1:] + [info[n][0]]


T = int(input())

for tc in range(1, T+1):
    K = int(input())
    info = [list(map(int, input().split())) for _ in range(4)]

    # 회전에 대한 확인
    for _ in range(K):
        num, dir = map(int, input().split())
        chk = [0] * 4
        dfs(num-1, dir) # idx이므로 0~3번 자석까지 존재

    ans = 0
    for i in range(4):
        ans += info[i][0] * 2 ** i

    print(f'#{tc} {ans}')
