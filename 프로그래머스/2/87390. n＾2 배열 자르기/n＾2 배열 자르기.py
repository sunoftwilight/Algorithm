def solution(n, left, right):
    answer = []
    
    for current in range(left, right+1):
        i = current // n
        j = current % n
        answer.append(max(i, j) + 1)
    
    return answer