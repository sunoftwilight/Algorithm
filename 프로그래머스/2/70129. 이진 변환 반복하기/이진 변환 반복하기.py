def solution(s):
    answer = [0, 0]
    
    while s != '1':
        answer[0] += 1
        answer[1] += s.count('0')
        
        c = len(s) - s.count('0')
        
        s = str(format(c, 'b'))
        
    return answer