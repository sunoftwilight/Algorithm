def comb(n, r):
    if r == 0:
        cnt_mo = 0
        for i in range(L):
            if T[i] in ['a', 'e', 'i', 'o', 'u']:
                cnt_mo += 1
        cnt_ja = L - cnt_mo

        if cnt_ja >= 2 and cnt_mo >= 1:
            a = sorted(T)
            psw.append(''.join(a))

    elif n < r:
        return

    else:
        T[r-1] = alph[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


L, C = map(int, input().split())
alph = list(input().split())

T = [0] * L
psw = []
comb(C, L)

psw.sort()

for i in range(len(psw)):
    print(psw[i])
