T = int(input())

for test_case in range(1, T + 1):
    
    list_n = list(map(int, input().split()))
    sum = 0
    
    for i in range(1,11):
        if list_n[i] % 2 ==0 :
            continue
        else:
            sum += list_n[i]
    print('#' + str(test_case) + ' ' + str(sum))    