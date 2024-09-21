import heapq


def solution(scoville, K):
    answer = 0
    
    heap = scoville
    heapq.heapify(heap)
    
    while True:
        first = heapq.heappop(heap)
        
        if first >= K:
            break
        
        if not heap:
            return -1
        
        second = heapq.heappop(heap)
        mixed = first + second * 2
        
        heapq.heappush(heap, mixed)
        
        answer += 1
        
    return answer