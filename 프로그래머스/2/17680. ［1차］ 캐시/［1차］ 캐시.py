from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
        
    cache_list = deque([])
    
    for city in cities:
        if city.upper() in cache_list:
            answer += 1
            cache_list.remove(city.upper())
            cache_list.append(city.upper())
            
        else:
            if len(cache_list) >= cacheSize:
                cache_list.popleft()
                
            cache_list.append(city.upper())
            answer += 5
    
    return answer