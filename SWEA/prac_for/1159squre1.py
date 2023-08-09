T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())

    arr = [[0]*W for _ in range(H)]

    cnt = 0

    for i in range(H):
        for j in range(W):
            cnt += 1
            arr[i][j] = cnt

    print(f'#{tc}')
    for i in range(H):
        print(*arr[i])

