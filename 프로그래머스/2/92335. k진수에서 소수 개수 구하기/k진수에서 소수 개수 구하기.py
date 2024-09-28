import math

def solution(n, k):
    answer = -1
    trans = ''
        
    while n > 0:
        n, remain = divmod(n, k)
        trans += str(remain)
    
    trans = trans[::-1]
    
    num_list = list(trans.split('0'))
    numbers = []
    
    for item in num_list:
        if item and int(item) > 1:
            numbers.append(int(item))
            
    for item in numbers:
        tmp_count = 0
        tmp_num = 2
        
        while tmp_num < math.sqrt(item):
            if item % tmp_num == 0:
                break
                    
            tmp_num += 1
            
        if tmp_num <= math.sqrt(item):
            numbers.remove(item)
        
    return len(numbers)