def solution(clothes):
    answer = 1
    
    org = dict()
    
    for item, key in clothes:
        if org.get(key):
            org[key] += 1
        else:
            org[key] = 2
    
    pieces = org.values()
    
    for piece in pieces:
        answer *= piece
    
    return answer - 1