def comb(n, r):
    global ans

    if r == 0:
        nT = []
        for i in range(N):
            if i not in T:
                nT.append(i)

        start = 0
        link = 0

        for i in range(N//2):
            for j in range(N//2):
                if i != j:
                    start += team_scr[T[i]][T[j]]
                    link += team_scr[nT[i]][nT[j]]

        temp = abs(start - link)
        ans = min(ans, temp)

    elif n < r:
        return

    else:
        T[r-1] = P[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


N = int(input())
P = []
for i in range(N):
    P.append(i)

team_scr = [list(map(int, input().split())) for _ in range(N)]
R = N // 2
T = [0] * R

ans = 999999999
comb(N, R)

print(ans)
