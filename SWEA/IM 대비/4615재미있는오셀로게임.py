T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    board = [[0] * N for _ in range(N)]

    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 1

    print(board)
    # arr = [list(map(int, input().split())) for _ in range(M)]

