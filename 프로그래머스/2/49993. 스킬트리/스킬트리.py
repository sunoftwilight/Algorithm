from collections import deque


def solution(skill, skill_trees):
    answer = 0
    skill_idx = dict()
    
    for idx, ap in enumerate(skill):
        skill_idx[ap] = idx
    
    skills = deque([])
    for skill_tree in skill_trees:
        tmp = skill_tree
        
        for i in range(len(skill_tree)):
            if skill_tree[i] not in skill:
                tmp = tmp.replace(skill_tree[i], '')
        
        order = []
        for ap in tmp:
            order.append(skill_idx[ap])

        is_ok = True
        for i in range(len(order)):
            if order[i] != i:
                is_ok = False
                break
                
        if is_ok:
            answer += 1
    return answer