def solution(dirs):
    answer = 0
    direct = { "U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    
    ci, cj = 5, 5
    
    visited = []
    
    for item in dirs:
        di, dj = direct[item]
        ni, nj = ci + di, cj + dj
        
        if  0 <= ni <= 10 and 0 <= nj <= 10:
            if ((ci, cj), (ni, nj)) not in visited and ((ni, nj), (ci, cj)) not in visited:
                answer += 1
                visited.append(((ci, cj), (ni, nj)))
                
            ci, cj = ni, nj
            
    return answer