def f(i, j, bw, N):
    board[i][j] = bw         # 주어진 돌 놓기

    for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i + di, j + dj
        tmp = []

        # (1) 보드 내부고, (2) 반대 색이면, 계속 이동
        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]:
            tmp.append((ni, nj))
            ni, nj = ni + di, nj + dj

        # (1) 보드 내부이고, (2) 같은 색이면,
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw:
            for p, q in tmp:
                board[p][q] = bw


B = 1             # 흑돌
W = 2             # 백돌
op = [0, 2, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())      # 보드 크기 N, 돌 놓는 횟수 M
    play = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]

    # 중심부 4개의 돌 배치
    board[N//2 - 1][N//2 - 1] = board[N//2][N//2] = W
    board[N//2 - 1][N//2] = board[N//2][N//2 - 1] = B

    for col, row, bw in play:    # 입력이 col, row, color // col, row는 인덱스 1 기준
        f(row-1, col-1, bw, N)   # 돌 놓기

    # 각 테스트 케이스마다 게임이 끝난 후, 보드 위의 흑돌과 백돌의 개수를 출력
    b_cnt = w_cnt = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                b_cnt += 1

            elif board[i][j] == W:
                w_cnt += 1

    print(f'#{tc} {b_cnt} {w_cnt}')
