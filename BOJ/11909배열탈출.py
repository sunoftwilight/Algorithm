import heapq
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, (0, (start, end)))
    D[start][end] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if D[now[0]][now[1]] > dist:
            continue

        if 1 <= now[0] and now[1] <= N:
            for di, dj in direction[:2]:
                ni = now[0] + di
                nj = now[1] + dj

        elif

            if 0 <= ni < N and 0 <= nj < N:


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

INF = 999999999
D = [[INF] * N for _ in range(N)]

dijkstra(0, 0)
print(D[N-1][N-1])
