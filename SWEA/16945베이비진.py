def perm(n, k, r):
    global flag

    if r == k:
        np = []
        for i in range(n):
            if visited[i] == 0:
                np.append(card[i])

        flag_a = chk(p)
        flag_b = chk(np)

        if flag_a and flag_b:
            flag = 1

        return flag

    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = card[i]
                perm(n, k+1, r)
                visited[i] = 0


def chk(lst):
    check = 0
    if lst[0] == lst[1] == lst[2]:
        check = 1

    if int(lst[1]) == int(lst[0])+1 and int(lst[2]) == int(lst[0])+2:
        check = 1

    return check


T = int(input())

for tc in range(1, T+1):
    card = list(input())

    N = 6
    R = 3

    p = [0] * R
    visited = [0] * N

    flag = 0
    perm(N, 0, R)

    print(f'#{tc} {flag}')
