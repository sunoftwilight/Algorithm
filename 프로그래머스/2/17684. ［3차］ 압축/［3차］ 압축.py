def solution(msg):
    answer = []
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idx = list(range(1, 27))
    idx_dict = {key: value for key, value in zip(alpha, idx)}
    
    new_idx = 27
    s, e = 0, 0
    
    while e <= len(msg):
        if idx_dict.get(msg[s : e + 1]):
            if e == len(msg) - 1:
                answer.append(idx_dict[msg[s : e + 1]])
                break
                
            e += 1
            
        else:
            answer.append(idx_dict[msg[s:e]])
            idx_dict[msg[s:e+1]] = new_idx
            
            new_idx += 1
            s = e
        
    return answer
