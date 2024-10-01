def solution(files):
    answer = []
    numbers = list(map(str, range(0, 10)))
    
    forSort = []
    for i in range(len(files)):
        file = files[i]
        s, e = 1, 1
        
        while e < len(file): 
            if file[s] in numbers:
                if file[e] in numbers:
                    e += 1
                else:
                    break
            else:
                s += 1
                e += 1
        
        HEAD = file[ : s]
        NUM = file[s : e]
        TAIL = file[e : ]
        
        forSort.append([HEAD.upper(), int(NUM), i, file])
        
    forSort.sort()
    
    for item in forSort:
        answer.append(item[3])
        
    return answer