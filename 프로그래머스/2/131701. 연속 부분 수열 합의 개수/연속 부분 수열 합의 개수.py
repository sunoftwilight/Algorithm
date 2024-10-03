def solution(elements):
    answer = set()
    N = len(elements)
    
    for i in range(1, N + 1):
        circle = elements + elements[:i]
        
        for j in range(N):
            answer.add(sum(circle[j:j+i]))
    
    return len(answer)