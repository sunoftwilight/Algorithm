def move(x, y, cnt):
    global where, many

    if cnt < many:
        return

    if x+1 < N and room[x][y] + 1 == room[x+1][y]:
        move(x+1, y, cnt+1)

    if y+1 < N and room[x][y] + 1 == room[x][y+1]:
        move(x, y+1, cnt+1)

    if 0 <= x-1 < N and room[x][y] + 1 == room[x-1][y]:
        move(x-1, y, cnt+1)

    if 0 <= y-1 < N and room[x][y] + 1 == room[x][y-1]:
        move(x, y-1, cnt+1)

    else:
        many = max(many, cnt)
        return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    where = 999999999
    max_cnt = 1

    for i in range(N):
        for j in range(N):
            many = 0
            move(i, j, 1)

            if max_cnt < many:
                max_cnt = many
                where = room[i][j]

            if max_cnt == many:
                where = min(where, room[i][j])

    print(f'#{tc} {where} {max_cnt}')
