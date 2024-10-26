from itertools import product


def solution(word):
    words = []
    
    for i in range(1, 6):
        tmp = list(product(['A', 'E', 'I', 'O', 'U'], repeat=i))
        for item in tmp:
            words.append(''.join(list(item)))
    
    words.sort()
    answer = words.index(word) + 1
    
    return answer