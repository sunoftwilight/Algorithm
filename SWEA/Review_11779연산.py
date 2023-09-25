from collections import deque


def bfs(n, m):
    Q = deque([n])  # Q = deque(); Q.append(n)
    visited[n] = 1

    while Q:
        n = Q.popleft()

        if n == m:
            return visited[n] - 1

        for w in [n+1, n-1, n*2, n-10]:
            if 0 < w <= 1_000_000:
                if visited[w] == 0:
                    Q.append(w)
                    visited[w] = visited[n] + 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * (1_000_000 + 1)

    print(f'#{tc} {bfs(N, M)}')