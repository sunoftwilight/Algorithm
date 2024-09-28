def solution(n, t, m, p):
    answer = ''
    trans_num = ''
    
    need_len = p + m * (t - 1)
    
    
    def trans_n(n, num):
        result = ''
        
        if num == 0:
            return '0'
        
        remain_dict = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F',
        }

        while num > 0:
            num, remain = divmod(num, n)
            
            if remain < 10:
                result += str(remain)
            else:
                result += remain_dict[remain]
        
        return result[::-1]

    
    current_num = 0
    while len(trans_num) < need_len:
        if n == 2:
            trans_num += format(current_num, 'b')
            
        elif n == 8:
            trans_num += format(current_num, 'o')

        elif n == 10:
            trans_num += format(current_num, 'd')
            
        elif n == 16:
            trans_num += format(current_num, 'x')
        
        else:
            trans_num += trans_n(n, current_num)
                    
        current_num += 1
    
    trans_num = trans_num.upper()
    
    for i in range(p - 1, need_len, m):
        answer += trans_num[i]
    
    return answer