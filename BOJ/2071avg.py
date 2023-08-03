T = int(input())

for test_case in range(1, T + 1):
    list1 = list(map(int, input().split()))
    
    sum = 0
    
    for i in range(10):
        sum += list1[i]
        
    avg = round(sum/10)
    
    # avg = round(sum(list1)/10)  
    # => sum을 이용해 list를 한번에 합할 수 있음.
    
    print(f"#{test_case} {avg}")