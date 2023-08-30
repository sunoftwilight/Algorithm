def perm(n, k, r, arr):
    global flag

    if r == k:
        ans = chk(p)
        if ans:
            flag = 1
            return flag

    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = arr[i]
                perm(n, k+1, r, arr)
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
    card = list(input().split())

    ply1 = []
    ply2 = []
    flag = 0

    for i in range(12):
        if i % 2 == 0:
            ply1.append(card[i])
        else:
            ply2.append(card[i])

        if len(ply1) >= 3:
            p = [0] * 3
            visited = [0] * len(ply1)
            perm(len(ply1), 0, 3, ply1)

            if flag:
                print(f'#{tc} {1}')
                break

        if flag == 0 and len(ply2) >= 3:
            p = [0] * 3
            visited = [0] * len(ply2)
            perm(len(ply2), 0, 3, ply2)

            if flag:
                print(f'#{tc} {2}')
                break

    if not flag:
        print(f'#{tc} {flag}')
