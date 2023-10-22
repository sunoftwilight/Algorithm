import heapq


def dijkstra(s):
    heap = []
    heapq.heappush(heap, (0, s))
    D[s] = 0

    while heap:
        d, min_v = heapq.heappop(heap)

        if D[min_v] < d:
            pass

        for nxt_nd, nxt_cst in adj[min_v]:
            new_cst = d + nxt_cst

            if new_cst < D[nxt_nd]:
                D[nxt_nd] = new_cst
                heapq.heappush(heap, (new_cst, nxt_nd))


V, E = map(int, input().split())
SP = int(input())

adj = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append([e, w])

INF = 999999999
D = [INF] * (V+1)

dijkstra(SP)

for i in range(1, V+1):
    if D[i] == INF:
        print('INF')
    else:
        print(D[i])
