def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    multi = len(arr1[0])
    
    answer = [[0] * col for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            i_row = arr1[i]
            j_col = []
            
            k = 0
            while k < multi:
                j_col.append(arr2[k][j])
                k += 1
                
            for m in range(multi):
                answer[i][j] += i_row[m] * j_col[m]
                
    return answer