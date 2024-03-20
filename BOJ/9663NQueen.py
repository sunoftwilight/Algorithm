def n_queen(n):
    global ans
    if n == N:
        ans += 1                 # 모든 행 확인했으면 경우의 수 + 1
        return

    else:
        for i in range(N):
            board[n] = i         # 몇 열에 놓았는지 정보 입력

            for j in range(n):
                if board[n] == board[j] or abs(board[n] - board[j]) == n - j: # 이전 행들의 수직 방향이나 양 대각 방향에 퀸이 있으면 break
                    break
            else:
                n_queen(n+1)     # break 당하지 않았으면 퀸 배치 가능하므로 배치 후 다음 행으로 넘어가기


N = int(input())
ans = 0
board = [0 for _ in range(N)]    # 각 행의 몇열에 퀸이 배치되어 있느냐

n_queen(0)
print(ans)
