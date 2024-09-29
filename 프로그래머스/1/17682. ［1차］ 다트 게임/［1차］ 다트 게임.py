def solution(dartResult):
    answer = []
    bonus_dict = {'S': 1, 'D': 2, 'T': 3}
    
    s = 0
    while s < len(dartResult)-1:
        if dartResult[s: s+2] == '10':
            score = 10
            s += 1
            
        else:
            score = int(dartResult[s])
            
        bonus = dartResult[s + 1]
        
        if s + 2 < len(dartResult) and dartResult[s + 2] in ['*', '#']:
            option = dartResult[s + 2]
            s += 3
        
        else: 
            option = '-'
            s += 2
        
        no_effect = score ** bonus_dict[bonus]
        
        if option == '*':
            if len(answer) > 0:
                answer[-1] = answer[-1] * 2
            answer.append(no_effect * 2)

        elif option == '#':
            answer.append(no_effect * (-1))
            
        else:
            answer.append(no_effect)
        
    return sum(answer)