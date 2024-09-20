def solution(numbers, target):
    global answer
    
    answer = 0
    
    n = len(numbers)
    
    def dfs(numbers, result, depth):
        global answer
        
        num1 = result + numbers[depth]
        num2 = result - numbers[depth]

        if depth == n - 1:
            if num1 == target:
                answer += 1
                
            if num2 == target:
                answer += 1
            return 

        else:
            dfs(numbers, num1, depth + 1)
            dfs(numbers, num2, depth + 1)
    
    dfs(numbers, 0, 0)
    
    return answer