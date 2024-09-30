def solution(record):
    answer = []
    uidDict = {}
    
    for item1 in record:
        if item1.startswith('L'):
            continue
        
        io, uid, name = item1.split(' ')
        uidDict[uid] = name
    
    for item2 in record:
        if item2. startswith('L'):
            io, uid = item2.split(' ')
            answer.append(f'{uidDict[uid]}님이 나갔습니다.')
        
        elif item2. startswith('E'):
            io, uid, name = item2.split(' ')
            answer.append(f'{uidDict[uid]}님이 들어왔습니다.')
            
    return answer