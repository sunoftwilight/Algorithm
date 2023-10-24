import heapq
direction = [[0, 1], [1, 0]]


def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, (0, (start, end)))
    D[start][end] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if D[now[0]][now[1]] < dist:
            continue

        for di, dj in direction:
            ni = now[0] + di
            nj = now[1] + dj

            if 0 <= ni < N and 0 <= nj < N:
                if arr[now[0]][now[1]] > arr[ni][nj]:
                    if D[ni][nj] > D[now[0]][now[1]]:
                        D[ni][nj] = D[now[0]][now[1]]
                        heapq.heappush(heap, (D[ni][nj], (ni, nj)))
                else:
                    cost = 1
                    while arr[now[0]][now[1]] + cost <= arr[ni][nj]:
                        cost += 1
                    if D[ni][nj] > D[now[0]][now[1]] + cost:
                        D[ni][nj] = D[now[0]][now[1]] + cost
                        heapq.heappush(heap, (D[ni][nj], (ni, nj)))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

INF = 999999999
D = [[INF] * N for _ in range(N)]

dijkstra(0, 0)
print(D[N-1][N-1])
