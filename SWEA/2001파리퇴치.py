T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_pr = 0

    for i in range(N-(M-1)):
        for j in range(N-(M-1)):
            total = 0                # 구간 별 파리채에 죽은 파리 수
            for k in range(M):
                for m in range(M):
                    total += arr[i+k][j+m]
            if max_pr < total:
                max_pr = total
    print(f'#{tc} {max_pr}')
