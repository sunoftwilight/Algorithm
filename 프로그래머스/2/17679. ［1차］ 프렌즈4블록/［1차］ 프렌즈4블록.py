direct = [(-1, 0), (-1, 1) ,(0, 1)]


def solution(m, n, board):
    answer = 0
    
    board = [list(board[i]) for i in range(m)]
    visited = [[False] * n for _ in range(m)]

    while True:
        thisTurn = set()
        
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == '':
                    continue
                if board[i][j] == board[i+1][j] == board[i+1][j+1] == board[i][j+1]:
                    thisTurn.add((i, j))
                    thisTurn.add((i+1, j))
                    thisTurn.add((i+1, j+1))
                    thisTurn.add((i, j+1))
        
        if len(thisTurn) == 0:
            break
        
        answer += len(thisTurn)
        
        removeList = list(thisTurn)
        
        for item in removeList:
            board[item[0]][item[1]] = ''
        
        while True:
            isMove = False
            
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == '':
                        board[i+1][j] = board[i][j]
                        board[i][j] = ''
                        isMove = True
                        
            if not isMove:
                break
        
    return answer