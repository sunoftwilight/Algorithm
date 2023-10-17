def solve():
    ct_dis = 0
    for i, j in hus:
        min_dis = 987654321
        for m, n in new:
            dis = abs(i-m) + abs(j-n)
            min_dis = min(min_dis, dis)
        ct_dis += min_dis
    return ct_dis


def perm(k, s):
    global ans

    if k == M:
        tmp = solve()
        ans = min(ans, tmp)
        return

    else:
        for i in range(s, CHK):
            if visited[i] == 0:
                visited[i] = 1
                new[k] = chk[i]
                perm(k+1, i+1)
                visited[i] = 0


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chk = []
hus = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chk.append((i, j))
        elif city[i][j] == 1:
            hus.append((i, j))

CHK = len(chk)
visited = [0] * CHK
new = [0] * M

ans = 987654321
perm(0, 0)

print(ans)
