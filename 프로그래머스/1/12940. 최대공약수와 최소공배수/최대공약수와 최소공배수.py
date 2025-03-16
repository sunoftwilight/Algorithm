def solution(n, m):
    answer = [0, 0]
    
    smaller = min(n, m)
    larger = max(n, m)
    
    for i in range(smaller, 0, -1):
        if n % i == 0 and m % i == 0:
            answer[0] = i
            break
    
    for j in range(larger, 1000001):
        if j % n == 0 and j % m == 0:
            answer[1] = j
            break
    
    return answer