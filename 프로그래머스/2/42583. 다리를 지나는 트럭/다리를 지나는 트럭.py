from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([1] + [0] * (bridge_length - 1))
    sum_truck = sum(bridge)
    
    i = 0
    while sum_truck != 0:
        answer += 1
        sum_truck -= bridge.popleft()
        
        if i >= len(truck_weights):
            continue
        
        if sum_truck + truck_weights[i] > weight:
            bridge.append(0)
            
        else:
            bridge.append(truck_weights[i])
            sum_truck += truck_weights[i]
            i += 1
        
    return answer