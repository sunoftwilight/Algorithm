def solution(topping):
    answer = 0
    n = len(topping)
    cheol = dict()
    bro = set()
    
    for topp in topping:
        if cheol.get(topp):
            cheol[topp] += 1
        else:
            cheol[topp] = 1
    
    for i in range(n-1, -1, -1):
        if cheol.get(topping[i]):
            cheol[topping[i]] -= 1
            
            if cheol[topping[i]] == 0:
                del cheol[topping[i]]
        
        bro.add(topping[i])
        
        if len(bro) == len(cheol.keys()):
            answer += 1
            
    return answer