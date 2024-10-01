from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    allNums = queue1 + queue2
    target = (sum1 + sum2) // 2
    
    if max(allNums) > target or (sum1 + sum2) % 2:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    maxLen = len(queue1) * 3
    
    answer = 0
    
    while True: 
        if answer >= maxLen:
            return -1
        
        if sum1 > sum2:
            item = queue1.popleft()
            queue2.append(item)
            sum1 -= item
            sum2 += item
        
        elif sum1 < sum2:
            item = queue2.popleft()
            queue1.append(item)
            sum2 -= item
            sum1 += item
        
        else:
            break
            
        answer += 1
    
    return answer