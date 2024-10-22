def solution(s):
    answer = ''
    s_list = s.split(' ')
    
    for item in s_list:
        tmp = ''
        for i in range(len(item)):
            if i % 2:
                tmp += item[i].lower()
            else:
                tmp += item[i].upper()
        
        answer += tmp + ' '
        
    return answer[:len(s)]