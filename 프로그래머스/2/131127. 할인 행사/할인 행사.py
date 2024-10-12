def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9):
        tendays = discount[i : i + 10]
        
        flag = True
        for i in range(len(want)):
            if tendays.count(want[i]) < number[i]:
                flag = False
                break
        
        if not flag:
            continue
        
        answer += 1
        
    return answer