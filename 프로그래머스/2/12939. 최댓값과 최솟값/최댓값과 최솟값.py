def solution(s):    
    nums = list(map(int, s.split()))
    nums.sort()
    
    answer = f'{nums[0]} {nums[-1]}'
    
    return answer