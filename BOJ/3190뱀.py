from collections import deque

# 입력 =======================================
N = int(input())
arr = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

L = int(input())
rot = []
for _ in range(L):
    s, d = map(str, input().split())
    rot.append((int(s), d))

# ============================================
# direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]

snake = deque()
snake.append((0, 0))

di, dj = 0, 1
sec, drc = rot.pop(0)

total = 0

while True:
    # 방향 전환 ------------------------------
    if total == sec:

        if di == -1 and dj == 0:
            if drc == 'L': di, dj = 0, -1
            if drc == 'D': di, dj = 0, 1

        elif di == 1 and dj == 0:
            if drc == 'L': di, dj = 0, 1
            if drc == 'D': di, dj = 0, -1

        elif di == 0 and dj == -1:
            if drc == 'L': di, dj = 1, 0
            if drc == 'D': di, dj = -1, 0

        elif di == 0 and dj == 1:
            if drc == 'L': di, dj = -1, 0
            if drc == 'D': di, dj = 1, 0

        if rot:
            sec, drc = rot.pop(0)

    # 1초간 ------------------------------
    i, j = snake[-1]

    total += 1
    ni, nj = i + di, j + dj   # 머리 옮기기

    if 0 <= ni < N and 0 <= nj < N:
        if (ni, nj) in snake:
            break

        snake.append((ni, nj))

        if arr[ni][nj] == 1:
            arr[ni][nj] = 0

        else:
            snake.popleft()

    else:
        break

print(total)
