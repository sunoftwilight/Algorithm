def solution(babbling):
    answer = 0
    
    for word in babbling:
        remove_word = word.replace('aya', '---')
        remove_word = remove_word.replace('ye', '--')
        remove_word = remove_word.replace('woo', '---')
        remove_word = remove_word.replace('ma', '--')

        if remove_word.count('-') == len(word):
            answer += 1
    
    return answer