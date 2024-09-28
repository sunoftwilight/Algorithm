def solution(N, stages):
    answer = []
    
    failure = [0] + [1] * N
    stages.sort(reverse=True)
    
    i = 0
    
    while i < len(stages):
        if stages[i] == N + 1:
            failure[N] = stages.count(N+1) / (stages.count(N) + stages.count(N+1))
            
            i += stages.count(N) + stages.count(N+1)
            
        else:
            
            tmp = 0

            while i + tmp < len(stages) - 1:
                if stages[i + tmp + 1] != stages[i]:
                    break

                tmp += 1
            
            failure[stages[i]] = i / (i + tmp + 1)
            
            i += tmp + 1
    
    idx_fail = []
    for idx, fail in enumerate(failure):
        idx_fail.append((fail, idx))
    
    idx_fail.sort()
    
    for i in range(1, len(idx_fail)):
        answer.append(idx_fail[i][1])
    
    return answer