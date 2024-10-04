from collections import deque


def solution(x, y, n):
    global answer
    
    answer = 987654321
    
    def bfs(num, depth):
        Q = deque([(num, depth)])
        
        while Q:
            cnum, k = Q.popleft()
            
            if cnum == x:
                return k
            
            if cnum % 2 == 0:
                Q.append((cnum / 2, k + 1))
            
            if cnum % 3 == 0:
                Q.append((cnum / 3, k + 1))
            
            if cnum - n >= x:
                Q.append((cnum - n, k + 1))
        
        return -1
        
    answer = bfs(y, 0)
    
    return answer