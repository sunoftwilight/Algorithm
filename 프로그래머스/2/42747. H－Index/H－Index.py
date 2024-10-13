def solution(citations):
    answer = 0
    max_n = max(citations)
    
    citations.sort(reverse=True)
    
    for i in range(max_n, -1, -1):
        k = 0
        while k < len(citations) and citations[k] >= i:
            k += 1
        
        if k >= i:
            return i
        
    return answer