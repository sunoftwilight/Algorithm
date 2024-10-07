import math


def solution(arr):
    answer = 1
    how_many = [False] * 101
    
    arr.sort()
    
    
    def prime_factorization(num):
        primes = []
        i, limit = 2, math.sqrt(num) + 1
        
        while i < limit:
            if num % i == 0:
                primes.append(i)
                num //= i
            
            else:
                i += 1
        
        if num >= 2:
            primes.append(num)
        
        return primes
    
    
    for item in arr:
        result = prime_factorization(item)
        current = 0
        
        for prime in result:
            if current == prime:
                continue
                
            if not how_many[prime]:
                how_many[prime] = result.count(prime)
                
            else:
                how_many[prime] = max(how_many[prime], result.count(prime))
                
    
    for i in range(101):
        if how_many[i]:
            answer *= i ** how_many[i]
    
    return answer