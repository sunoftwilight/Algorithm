from collections import deque

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(maps):
    maps = [list(maps[i]) for i in range(len(maps))]
    n, m = len(maps), len(maps[0])
    s, l, e = (), (), ()
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                s = (i, j)
                
            elif maps[i][j] == 'L':
                l = (i, j)
                
            elif maps[i][j] == 'E':
                e = (i, j)
    
    
    def bfs(start, arrive):        
        Q = deque([(start[0], start[1], 0)])
        
        visited = [[False] * m for _ in range(n)]
        visited[start[0]][start[1]] = True
        
        while Q:
            ci, cj, distance  = Q.popleft()
            
            if maps[ci][cj] == arrive:
                return distance
            
            for di, dj in direct:
                ni, nj = ci + di, cj + dj
                
                if 0 <= ni < n and 0 <= nj < m:
                    if maps[ni][nj] != 'X' and not visited[ni][nj]:
                        visited[ni][nj] = True
                        Q.append((ni, nj, distance + 1))
                        
        return -1
        
    
    toLever = bfs(s, 'L')
    if toLever == -1:
        return -1
        
    toExit = bfs(l, 'E')
    if toExit == -1:
        return -1
    
    return (toLever + toExit)