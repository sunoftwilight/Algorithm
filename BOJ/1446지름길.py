import heapq


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for next_node, cost in road[now]:
            next_cost = cost + dist

            if distance[next_node] > next_cost:
                distance[next_node] = next_cost
                heapq.heappush(heap, (distance[next_node], next_node))


N, D = map(int, input().split())
road = [[] for _ in range(D + 1)]

for i in range(D):
    road[i].append((i+1, 1))

for _ in range(N):
    s, e, w = map(int, input().split())
    if e <= D:
        road[s].append([e, w])

distance = [999999999] * (D + 1)
dijkstra(0)

print(distance[D])
