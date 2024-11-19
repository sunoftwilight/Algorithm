def solution(weights):
    answer = 0
    weights.sort()
    wd = dict()
    
    for w in weights:
        wd[w] = wd.get(w, 0) + 1
    
    for w in weights:        
        if wd.get(w * 2, False):
            answer += wd[w * 2]
        
        if wd.get(w * 3 / 2, False):
            answer += wd[w * 3 / 2]
        
        if wd.get(w * 4 / 3, False):
            answer += wd[w * 4 / 3]
    
    for value in wd.values():
        if value >= 2:
            answer += value * (value - 1) // 2
            
    return answer