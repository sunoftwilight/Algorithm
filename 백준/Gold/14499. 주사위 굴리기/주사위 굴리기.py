def turn(cmd_num):
    global dice

    if cmd_num == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]

    elif cmd_num == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]

    elif cmd_num == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

    elif cmd_num == 4:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]


N, M, x, y, K = map(int, input().split())
gido = [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))

direct = [(1, 0), (0, 1), (0, -1), (-1, 0)]
ci, cj = x, y

dice = [0, 0, 0, 0, 0, 0, 0]

for cmd in cmds:
    # 지도 칸 이동
    di, dj = direct[cmd % 4]
    ni, nj = ci + di, cj + dj

    # 지도 안쪽일 때만 명령 수행
    if 0 <= ni < N and 0 <= nj < M:
        # 주사위 이동
        turn(cmd)

        if gido[ni][nj]:
            # 칸의 수가 주사위 바닥에 복사, 칸은 0으로 변경
            dice[-1] = gido[ni][nj]
            gido[ni][nj] = 0

        else:
            # 주사위 바닥의 수를 칸에 복사
            gido[ni][nj] = dice[-1]

        print(dice[0])
        ci, cj = ni, nj
