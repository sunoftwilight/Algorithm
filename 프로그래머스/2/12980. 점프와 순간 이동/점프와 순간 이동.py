def solution(n):
    ans = 0
    
    while True:
        if n % 2 == 1:
            ans += 1
            n -= 1
        
        n //= 2
        
        if not n:
            break
        
    return ans