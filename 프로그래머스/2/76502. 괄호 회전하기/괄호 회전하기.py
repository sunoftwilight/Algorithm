def solution(s):
    answer = 0
    
    def correct(string):
        stacks = []
        
        for paren in string:
            if not stacks:
                if paren in {'}', ']', ')'}:
                    return False
                else:
                    stacks.append(paren)
            
            else:
                if paren in {'{', '[', '('}:
                    stacks.append(paren)
                    
                elif paren == '}' and stacks[-1] == '{':
                        stacks.pop()
                        
                elif paren == ']' and stacks[-1] == '[':
                    stacks.pop()
                    
                elif paren == ')' and stacks[-1] == '(':
                    stacks.pop()
                    
                else:
                    return False
        
        if stacks:
            return False
        
        return True
    
    
    for i in range(len(s)):
        new = s[i:] + s[:i]
        is_correct = correct(new)
        
        if is_correct:
            answer += 1
        
    return answer