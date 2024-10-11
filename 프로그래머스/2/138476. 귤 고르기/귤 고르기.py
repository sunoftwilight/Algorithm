from collections import Counter, deque

def solution(k, tangerine):
    answer = 0
    n_size = deque(Counter(tangerine).most_common())
    
    while k > 0:
        n, idx = n_size.popleft()
        k -= idx
        answer += 1
    
    return answer