def solution(n, words):
    answer = [0, 0]
    
    speak = dict()
    
    for i in range(len(words)):
        if speak.get(words[i]) or (i != 0 and words[i-1][-1] != words[i][0]):
            return [i % n + 1, i // n + 1]
        
        speak[words[i]] = True

    return answer