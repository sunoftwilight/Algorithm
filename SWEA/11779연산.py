from collections import deque

def solve(v):
    global ans

    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.popleft()

        if v == M:
            return visited[v]

        for i in range(4):
            if i == 0: w = v + 1
            elif i == 1: w = v * 2
            elif i == 2: w = v - 1
            else: w = v - 10

            if 0 < w <= 1000000 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    visited = [0] * 1000001
    Q = deque()

    ans = solve(N)

    print(f'#{tc} {ans-1}')
