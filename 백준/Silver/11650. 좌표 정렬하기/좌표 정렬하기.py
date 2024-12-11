N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

arr.sort()

for i, j in arr:
    print(i, j)