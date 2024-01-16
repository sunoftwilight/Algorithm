import copy

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
modi_arr = copy.deepcopy(arr)

cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            cnt += 1
            modi_arr[i][j] = 1
        for k in range(i, N):
            for m in range(j+1, M):
                if arr[k][m] == 0:
                    cnt += 1
                    modi_arr[k][m] = 1
                for n in range(k, N):
                    for l in range(m+1, M):
                        if arr[n][l] == 0:
                            cnt += 1
                            modi_arr[k][m] = 1
