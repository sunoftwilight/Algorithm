def solution(s):
    num_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    answer = ''
    
    idx = 0
    
    while idx < len(s):
        tmp = idx
        
        while s[tmp] not in num_list:
            tmp += 1
            
            if num_dict.get(s[idx : tmp]):
                # answer += num_dict[s[idx : tmp]]
                break
        
        if tmp - idx > 1:
            answer += num_dict[s[idx: tmp]]
            idx = tmp
            
        else:
            answer += s[idx]
            idx += 1    
    
    return int(answer)