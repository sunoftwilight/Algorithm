arr = [list(map(int, input().split())) for _ in range(4)]

dohwaji = [[0] * 101 for _ in range(101)]

for i in range(4):
    for j in range(arr[i][0], arr[i][2]):
        for k in range(arr[i][1], arr[i][3]):
            dohwaji[j][k] = 1

cnt = 0

for i in range(1, 101):
    for j in range(1, 101):
        if dohwaji[i][j] == 1:
            cnt += 1

print(cnt)
