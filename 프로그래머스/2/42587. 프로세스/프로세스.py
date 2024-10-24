from collections import deque

def solution(priorities, location):
    answer = 0
    n = len(priorities) - 1
    
    for i in range(len(priorities)):
        priorities[i] = (priorities[i], True) if i == location else (priorities[i], False)
    
    priorities = deque(priorities)
    print(priorities)
    while priorities:
        pri, loc = priorities.popleft()
        
        if priorities and pri < max(priorities)[0]:
            priorities.append((pri, loc))
            
        else:
            answer += 1
            if loc:
                break
                
    return answer