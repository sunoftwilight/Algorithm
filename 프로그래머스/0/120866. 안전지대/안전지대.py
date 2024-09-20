def solution(board):
    dir = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    
    n = len(board)
    answer = n * n
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                if visited[i][j] == False:
                    visited[i][j] = True
                    answer -= 1
                
                for di, dj in dir:
                    ni = i + di
                    nj = j + dj
                    
                    if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == False:
                        visited[ni][nj] = True
                        answer -= 1
    
    return answer