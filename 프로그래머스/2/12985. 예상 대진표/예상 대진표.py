def solution(n,a,b):
    answer = 1
    n1 = a + 1 if a % 2 else a
    n2 = b + 1 if b % 2 else b
    
    while True:
        if abs(n1 - n2) == 1 or abs(n1 - n2) == 0:
            return answer
        
        n1 //= 2
        n2 //= 2
        
        n1 = n1 + 1 if n1 % 2 else n1
        n2 = n2 + 1 if n2 % 2 else n2
        
        answer += 1
        
    
    return answer