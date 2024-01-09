direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(i, j, new):
    if len(new) == 6:
        if new not in num:
            num.append(new)
        return

    else:
        for di, dj in direct:
            ni = i + di
            nj = j + dj

            if 0 <= ni < 5 and 0 <= nj < 5:
                dfs(ni, nj, new + num_board[ni][nj])


num_board = [list(map(str, input().split())) for _ in range(5)]

num = []

for i in range(5):
    for j in range(5):
        dfs(i, j, num_board[i][j])

print(len(num))