H, W = map(int, input().split())
block = list(map(int, input().split()))

arr = [[0] * W for _ in range(H)]

for i in range(H-1, -1, -1):
    for j in range(W-1, -1, -1):
        if block[j] != 0:
            block[j] -= 1
            arr[i][j] = 1


rain, tmp = 0, 0
i, j = 0, 0
wall_s = False

while True:

    if i == H - 1 and j == W -1:
        break

    if arr[i][j] == 1:
        wall_s = True

    if wall_s and arr[i][j] == 0:
        tmp += 1

    if arr[i][j] and tmp:
        rain += tmp
        tmp = 0

    if j == W-1:
        if wall_s:
            tmp = 0
            wall_s = False
        i += 1
        j = 0

    else:
        j += 1

print(rain)