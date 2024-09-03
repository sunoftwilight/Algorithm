def solution(n):    
    binary = format(n, 'b')
    no = str(binary).count('1')
    new = n
    
    while True:
        new += 1
        new_binary = format(new, 'b')
        new_no = str(new_binary).count('1')
        
        if new_no == no:
            break
        
    return new