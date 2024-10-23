import heapq

def solution(progresses, speeds):
    answer = []
    done = []

    for i in range(len(progresses)):
        day = (100 - progresses[i]) // speeds[i]
        
        if (100 - progresses[i]) % speeds[i]:
            day += 1
        
        done.append((i+1, day))
    
    task = 0
    while task < len(speeds):
        tmp = 0
        while task + tmp < len(speeds):
            if done[task][1] == max(done[task:task+tmp+1], key=lambda x: x[1])[1]:
                tmp += 1
            else:
                break
                
        answer.append(tmp)
        task += tmp
        
    return answer