T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: (x[1], x[0]))

    '''
    x[1] 정렬 후, x[1] 값이 같은 요소들은 x[0]에 대해 재정렬하는 방법
    
    1.
    arr.sort(key=lambda x: (x[1], x[0]))
    
    2. 
    def cmp(x):
        :return x[1], x[0]
            
    arr.sort(key = cmp)
        
    '''

    finish = ans = 0
    for i in range(N):
        if finish <= arr[i][0]:
            ans += 1
            finish = arr[i][1]

    print(f'#{tc} {ans}')
