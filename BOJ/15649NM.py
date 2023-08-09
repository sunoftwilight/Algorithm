N, M = map(int, input().split())

lst = []

for i in range(1, N+1):
    lst.append(i)

for i in range(1 << N+1):
    cnt = []
    for j in range(N):
        if i & (1 << j):
            cnt.append(lst[j])

    if len(cnt) == M:
        print(*cnt)