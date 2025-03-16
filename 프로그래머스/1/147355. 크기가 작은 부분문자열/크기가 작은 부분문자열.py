def solution(t, p):
    answer = 0
    
    len_t = len(t)
    len_p = len(p)
    
    for i in range(0, len_t - len_p + 1):
        sub = t[i : i + len_p]
        
        if int(sub) <= int(p):
            answer += 1
    
    return answer