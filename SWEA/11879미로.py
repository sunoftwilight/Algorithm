'''
def dfs(i, j):
    visited[i][j] = 1

    if arr[i][j] == 3:
        flag = 1
        return

    for k in (4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N and (arr[ni][nj] == 3 or arr[ni][nj] == 0):
            dfs(ni, nj)
'''


def dfs(i, j):
    global flag

    visited[i][j] = 1

    if arr[i][j] == 3:
        flag = 1
        return flag

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and (arr[ni][nj] == 0 or arr[ni][nj] == 3):
            # 방문 안한 점만 dfs로 탐색해야댐 ==> visited[ni][nj] == 0 확인 필요!!!
            dfs(ni, nj)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    a = b = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                a = i
                b = j

    flag = 0
    dfs(a, b)

    print(f'#{tc} {flag}')
