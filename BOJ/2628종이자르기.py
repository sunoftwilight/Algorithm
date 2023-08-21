width, length = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

paper = [[0] * width for _ in range(length)]

a = 0
for i in range(N):
    a += 1
    if not arr[i][0]:
        for j in range(arr[i][1]):
            for k in range(width):
                paper[j][k] += 1
                a += 1
    else:
        for j in range(arr[i][1]):
            for k in range(length):
                paper[k][j] += 1
                a += 1

max_num = max(map(max, paper))
max_paper = 0

for m in range(max_num+1):
    cnt = 0
    for i in range(length):
        for j in range(width):
            if paper[i][j] == m:
                cnt += 1

    if max_paper < cnt:
        max_paper = cnt

print(max_paper)
