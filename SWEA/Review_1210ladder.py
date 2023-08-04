import sys; sys.stdin = open("input_ladder.txt")


def find_start(arr):
    for i in range(N):
        if arr[N-1][i] == 2:
            x = N - 1
            y = i
            return x, y


def ladder(arr, x, y):
    while True:
        if x == 0: return y
        # 3방향 탐색
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                x, y = nx, ny
                arr[x][y] = '@'   # 방문 표시
                break


dx = [0, 0, -1]
dy = [-1, 1, 0]

N = 100
T = 10

for tc in range(1, T+1):
    no = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    x, y = find_start(arr)

    print(f'#{tc} {ladder(arr, x, y)}')
