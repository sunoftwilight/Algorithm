def solution(n, arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        one = bin(arr1[i])[2:].zfill(n)
        two = bin(arr2[i])[2:].zfill(n)
        
        line = ''
        for j in range(n):
            if one[j] == '1' or two[j] == '1':
                line += '#'
            else:
                line += ' '
        
        answer.append(line)
        
    return answer