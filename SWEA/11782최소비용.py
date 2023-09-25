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
        # 가지치기
        if x == N-1 and y == N-1:
            return

        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for di, dj in direction:
            ni = min_i + di
            nj = min_j + dj

            if 0 <= ni < N and 0 <= nj < N:
                diff = 1    # 경사도

                if visited[ni][nj] == 0:

                    if arr[ni][nj] > arr[min_i][min_j]:
                        diff += arr[ni][nj] - arr[min_i][min_j]

                    # 업데이트
                    if D[ni][nj] > D[min_i][min_j] + diff:
                        D[ni][nj] = D[min_i][min_j] + diff


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    D = [[987654321] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dijkstra(0, 0)

    print(f'#{tc} {D[N-1][N-1]}')


# heap으로 풀기 =====================================================

# import heapq
#
# def dijkstra(x, y):
#     heap = []
#     D[x][y] = 0
#
#     heapq.heappush(heap, (D[x][y], x, y))
#
#     while heap:
#         d, min_i, min_j = heapq.heappop(heap)
#
#         visited[min_i][min_j] = 1
#
#         direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#
#         for di, dj in direction:
#             ni = min_i + di
#             nj = min_j + dj
#
#             if 0 <= ni < N and 0 <= nj < N:
#                 diff = 1
#                 if visited[ni][nj] == 0:
#                     if arr[ni][nj] > arr[min_i][min_j]:
#                         diff += arr[ni][nj] - arr[min_i][min_j]
#                     if D[ni][nj] > D[min_i][min_j] + diff:
#                         D[ni][nj] = D[min_i][min_j] + diff
#                         heapq.heappush(heap, (D[ni][nj], ni, nj))
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     D = [[987654321] * N for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#
#     dijkstra(0, 0)
#
#     print(f'#{tc} {D[N-1][N-1]}')
