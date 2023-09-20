N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

all = []
for rows in arr:
    rows.sort()
    all += rows[N-5:N:-1]

print(all)
