def solution(s):
    if s.startswith(')') or s.endswith('('):
        return False
    
    stacks = list(s)
    tmp = 0
    is_need = False
    before = ''
    
    while stacks:
        current = stacks.pop()
        
        if current == ')':
            tmp += 1
            is_need = True
        
        if current == '(':
            if not is_need:
                return False
            tmp -= 1
        
        if tmp < 0:
            return False
        
        
        
    return True