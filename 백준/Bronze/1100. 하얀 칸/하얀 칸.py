arr = [input() for _ in range(8)]

answer = 0
start = False

for i in range(8):
    for j in range(start, 8, 2):
        if arr[i][j] == 'F':
            answer += 1

    start = not start

print(answer)