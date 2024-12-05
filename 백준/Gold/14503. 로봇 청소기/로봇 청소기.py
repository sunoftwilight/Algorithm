N, M = map(int, input().split())
r, c, d = map(int, input().split())
place = [list(map(int, input().split())) for _ in range(N)]

direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]

answer = 0
ci, cj = r, c
curr_d = d

while True:
    if place[ci][cj] == 0:
        place[ci][cj] = 2
        answer += 1

    is_dirty = False
    tmp_d = curr_d

    for i in range(4):
        tmp_d = (tmp_d + 4 - 1) % 4
        ni, nj = ci + direct[tmp_d][0], cj + direct[tmp_d][1]

        if 0 <= ni < N and 0 <= nj < M and not place[ni][nj]:
            ci, cj = ni, nj
            curr_d = tmp_d
            is_dirty = True
            break

    if not is_dirty:
        ni, nj = ci - direct[curr_d][0], cj - direct[curr_d][1]

        if 0 <= ni < N and 0 <= nj < M and place[ni][nj] != 1:
            ci, cj = ni, nj

        else:
            break

print(answer)