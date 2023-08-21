T = 10

for tc in range(1, T+1):
    N = int(input())
    # arr = [list(input().split()) for _ in range(N)]

    tree = [[0] * 3 for _ in range(N+1)]

    for i in range(N):
        tmp = list(input().split())
        tree[int(arr[i][0])][0] = int(arr[i][2])
        tree[int(arr[i][0])][1] = int(arr[i][3])
        tree[int(arr[i][0])]

