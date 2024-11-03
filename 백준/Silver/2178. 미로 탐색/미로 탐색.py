from collections import deque

N, M = map(int, input().split())
maze = [input() for _ in range(N)]
answer = 0

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

Q = deque([(1, 0, 0)])
visited = [[False] * M for _ in range(N)]
visited[0][0] = True

while Q:
    pixel, ci, cj = Q.popleft()

    if ci == N-1 and cj == M-1:
        answer = pixel
        break

    for di, dj in direct:
        ni, nj = ci + di, cj + dj

        if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == '1' and not visited[ni][nj]:
            visited[ni][nj] = True
            Q.append((pixel+1, ni, nj))

print(answer)
