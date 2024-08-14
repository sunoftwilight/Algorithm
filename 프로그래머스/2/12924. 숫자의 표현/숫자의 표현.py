def solution(n):
    answer = 1
    
    for i in range(1, n // 2 + 1):
        tmp = 0
        
        while tmp < n:
            tmp += i
            
            if tmp == n:
                answer += 1
                
            i += 1
    
    return answer