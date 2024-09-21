import copy

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(maps):
    global answer

    answer = []

    n = len(maps)
    m = len(maps[0])

    visited = copy.deepcopy(maps)

    def dfs(ci, cj, distance):
        global dir, answer

        if ci == n - 1 and cj == m - 1:
            answer.append(distance)

            return

        visited[ci][cj] = 0

        for di, dj in dir:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj]:
                dfs(ni, nj, distance + 1)
                visited[ni][nj] = 1

    dfs(0, 0, 1)

    if answer:
        return min(answer)

    else:
        return -1
