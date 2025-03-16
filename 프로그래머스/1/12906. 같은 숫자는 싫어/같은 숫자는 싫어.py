from collections import deque

def solution(arr):
    answer = []
    nums = deque(arr)
    
    while True:
        if nums:
            if answer and answer[-1] == nums[0]:
                nums.popleft()

            else:
                put_num = nums.popleft()
                answer.append(put_num)
        else:
            break    
    
    return answer