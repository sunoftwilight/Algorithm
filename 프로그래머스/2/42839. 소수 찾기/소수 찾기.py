import math
import copy

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    N = len(numbers)
    
    
    def isPrime(num):
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        
        return True
        
        
    def dfs(numComb, maxLen, visited, numbers):
        if len(numComb) == maxLen:
            combNums.add(int(numComb))
            return
        
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                dfs(numComb + numbers[i], maxLen, visited, numbers)
                visited[i] = False
                
        return

    
    combNums = set()
    for i in range(1, N + 1):
        for j in range(N):
            visited = [False] * N
            visited[j] = True
            dfs(numbers[j], i, visited, numbers)
    
    combNums = list(combNums)
    answer = copy.deepcopy(combNums)
    
    for num in combNums:
        if num <= 1 or not isPrime(num):
            answer.remove(num)
            
    return len(answer)