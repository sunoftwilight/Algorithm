N = int(input())
find_num = int(input())

snail = [[0] * N for _ in range(N)]
direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]

i, j = N // 2, N // 2
cnt = 1
snail[i][j] = cnt

M = 1
k = 0

while cnt < N ** 2:

    di, dj = direct[k % 4]

    for m in range(1, M+1):
        ni = i + di
        nj = j + dj

        if (0 <= ni < N and 0 <= nj < N) and snail[ni][nj] == 0:
            cnt += 1
            snail[ni][nj] = cnt
            if cnt == N ** 2: break

            i, j = ni, nj

    k += 1

    if (di == 0 and dj == 1) or (di == 0 and dj == -1):
        M += 1

find_i, find_j = 0, 0

for i in range(N):
    for j in range(N):
        if j == N-1:
            print(snail[i][j], end="\n")
        else:
            print(snail[i][j], end=" ")

        if snail[i][j] == find_num:
            find_i, find_j = i, j

print(find_i+1, find_j+1)
