T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    cnt = 0
    flag_B = 0
    flag_R = 0

    for i in range(N-1):
        cnt_B = cnt_W = cnt_R = 0
        for j in range(M):
            if i == 0:
                if arr[i][j] != 'W':
                    cnt += 1

            elif flag_B == 0 and flag_R == 0:
                if arr[i][j] != 'W':
                    cnt_W += 1
                
                elif arr[i][j] != 'B':
                    cnt_B += 1
            
            elif flag_B == 1 and flag_R == 0:
                if arr[i][j] != 'B':
                    cnt_B += 1
                
                elif arr[i][j] != 'R':
                    cnt_R += 1
            
            elif flag_B == 1 and flag_R == 1:
                if arr[i][j] != 'R':
                    cnt += 1

        if i != 0 and flag_B == 0 and flag_R == 0:
            if cnt_B > cnt_W:
                cnt += cnt_W

            elif: cnt
                cnt += cnt_B
                flag_B = 1
        
        elif flag_B == 1 and flag_R == 0:
            if cnt_B > cnt_R:
                cnt += cnt_R
                flag_R = 1

            else:
                cnt += cnt_B
                flag_B = 1

    for j in range(M):
        if arr[N-1][j] != 'R':
            cnt += 1

    print(f'#{tc} {cnt}')
