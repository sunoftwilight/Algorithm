from collections import deque
from itertools import combinations
import copy

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def spread_virus(new_walls):
    global answer

    spread = copy.deepcopy(zido)
    spread_two = deque(copy.deepcopy(two))
    
    for i, j in new_walls:
        spread[i][j] = 1

    while spread_two:
        ci, cj = spread_two.popleft()

        for di, dj in direct:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < M and spread[ni][nj] == 0:
                spread[ni][nj] = 2
                spread_two.append((ni, nj))

    current_safe = 0

    for i in range(N):
        current_safe += spread[i].count(0)

    answer = max(answer, current_safe)


N, M = map(int, input().split())
zido = [list(map(int, input().split())) for _ in range(N)]

answer = 0

two = deque([])
zero = deque([])

for i in range(N):
    for j in range(M):
        if zido[i][j] == 2:
            two.append((i, j))
            
        elif zido[i][j] == 0:
            zero.append((i, j))

for new_walls in combinations(zero, 3):
    spread_virus(new_walls)

print(answer)
