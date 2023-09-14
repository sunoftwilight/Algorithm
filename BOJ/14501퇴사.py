def comb(n, r):

    if r == 0:


    elif r > n:
        return

    else:
        T[r-1] = coun[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


N = int(input())
coun = []

for _ in range(N):
    coun.append(list(map(int, input().split())))

max_money = 0
for i in range(N):
    T = [0] * i
    comb(N, i)