from collections import deque

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    Q = deque([(1, 0, 0)])
    visited = [[0] * m for _ in range(n)]

    visited[0][0] = 1

    while Q:
        dist, ci, cj = Q.popleft()
        
        if ci == n - 1 and cj == m - 1:
            return dist

        for di, dj in direct:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                Q.append((dist + 1, ni, nj))
    
    return -1