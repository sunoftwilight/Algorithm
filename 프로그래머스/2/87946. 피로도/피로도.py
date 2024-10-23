from itertools import permutations

def solution(k, dungeons):
    answer = -1
    perm = list(permutations(dungeons))
    
    for comb in perm:
        piro = k
        can_go = 0
        
        for dun in comb:
            if piro >= dun[0]:
                piro -= dun[1]
                can_go += 1
            else:
                break
        
        answer = max(can_go, answer)
        
        if answer == len(dungeons):
            break
    
    return answer