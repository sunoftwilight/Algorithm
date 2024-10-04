def solution(arr):
    answer = [0, 0]
    n = len(arr)
    
    if arr.count(arr[0][0]) == n ** 2:
        if arr[0][0]:
            return [0, 1]
        return [1, 0]
    
    
    def compression(r, c, l):
        for i in range(r, r + l):
            for j in range(c, c + l):
                if arr[r][c] != arr[i][j]:
                    l //= 2
                    
                    compression(r, c, l)
                    compression(r + l, c, l)
                    compression(r, c + l, l)
                    compression(r + l, c + l, l)
                    return
                
        answer[arr[r][c]] += 1
        
    
    compression(0, 0, n)
    return answer