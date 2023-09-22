import heapq

def dijkstra(x, y):
    D[x][y] = 0

    for _ in range(N**2):
        min_v = 987654321
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0 and D[i][j] < min_v:
                    min_v = D[i][j]
                    min_i = i
                    min_j = j

        visited[min_i][min_j] = 1

        if x == N-1 and y == N-1:
            return

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = min_i + di
            nj = min_j + dj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if D[ni][nj] > D[min_i][min_j] + arr[min_i][min_j]:
                    D[ni][nj] = D[min_i][min_j] + arr[min_i][min_j]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]

    D = [[987654321] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dijkstra(0, 0)

    print(f'#{tc} {D[N-1][N-1]}')
