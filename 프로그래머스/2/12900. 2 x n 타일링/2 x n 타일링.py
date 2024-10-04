import math


def solution(n):
    answer = [0, 1, 2] + [0] * (n - 2)
    
    if n <= 2:
        return answer[n]
        
    for i in range(3, n + 1):
        answer[i] = (answer[i-1] + answer[i-2]) % 1_000_000_007
    
    return answer[n]

