direct = [[1, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]


def dfs(n, ci, cj, v):
    global ans

    # 가지치기 : 절반 돌았는데 *2 해도 정답 갱신이 불가능 => 가망X
    if n == 2 and ans >= len(v) * 2:
        return

    # 종료 조건 (3번까지만 꺾어야함!!!)
    if n > 3:
        return

    # 정답 처리 조건 (3번 꺾고 시작점으로 돌아옴)
    if n == 3 and (si, sj) == (ci, cj):
        ans = max(ans, len(v))

    # n방향, n+1방향 총 2가지 방향으로 뻗어나가기
    for k in range(n, n+2):
        ni = ci + direct[k][0]
        nj = cj + direct[k][1]

        # 범위 내이고, 먹어본 적 없는 디저트라면
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            # 먹어본 디저트 목록에 추가하고
            v.append(arr[ni][nj])
            # 순회 이어나감
            dfs(k, ni, nj, v)
            # 순회 종료하면 다른 방향으로 확인해봐야하니깐 pop
            v.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = -1

    for si in range(N-2):
        for sj in range(1, N-1):
            dfs(0, si, sj, [])

    print(f'#{tc} {ans}')
