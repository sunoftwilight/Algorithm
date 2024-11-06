from itertools import combinations
import copy


def surveillance(blocks):
    case = copy.deepcopy(info)

    for bi, bj in blocks:
        case[bi][bj] = 'O'

    for ti, tj in teachers:
        for di, dj in direct:
            m = 0

            while True:
                ni, nj = ti + di * m, tj + dj * m

                if 0 <= ni < N and 0 <= nj < N:
                    if case[ni][nj] == 'S':
                        return True
                    elif case[ni][nj] == 'O':
                        break
                    else:
                        m += 1
                else:
                    break

    return False


N = int(input())
info = [input().split(' ') for _ in range(N)]
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

empty = []
teachers = []

for i in range(N):
    for j in range(N):
        if info[i][j] == 'X':
            empty.append((i, j))

        elif info[i][j] == 'T':
            teachers.append((i, j))

answer = 'NO'

for three_blocks in combinations(empty, 3):
    is_find = surveillance(three_blocks)

    if not is_find:
        answer = 'YES'
        break

print(answer)
