N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1], x[0]))

e = arr[0][1]
cnt = 1
for i in range(1, N):
    if arr[i][0] >= e:
        cnt += 1
        e = arr[i][1]

print(cnt)
