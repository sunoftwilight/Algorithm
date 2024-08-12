def solution(s):
    
    s = s.lower()
    words_list = s.split(" ")

    for i in range(len(words_list)):
        if words_list[i] == "":
            continue
        else:
            words_list[i] = words_list[i][0].upper() + words_list[i][1:]

    answer = ' '.join(words_list)
        
    return answer