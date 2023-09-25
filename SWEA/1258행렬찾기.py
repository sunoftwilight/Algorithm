T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mtr = [list(map(int, input().split())) for _ in range(N)]

    area = []
    cnt = 0

    for i in range(N):
        for j in range(N):
            if mtr[i][j]:
                st_i = end_i = i
                st_j = end_j = j

                while end_i <= N-1 and end_j <= N-2 and mtr[end_i][end_j+1]:
                    end_j += 1

                while end_i <= N-2 and end_j <= N-1 and mtr[end_i+1][end_j]:
                    end_i += 1

                for m in range(st_i, end_i+1):
                    for n in range(st_j, end_j+1):
                        mtr[m][n] = 0

                area.append([(end_i-st_i+1)*(end_j-st_j+1), end_i-st_i+1, end_j-st_j+1])
                cnt += 1

    area.sort()

    print(f'#{tc} {cnt}', end=" ")
    for k in range(len(area)):
        area[k].pop(0)
        print(*area[k], end=" ")
    print()