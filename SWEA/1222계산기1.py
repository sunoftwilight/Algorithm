T = 10

for tc in range(1, T+1):
    N = int(input())
    txt = list(input().split())

    op = []
    postfix = []

    cnt = 0

    for i in range(N):
        if txt[i] != '+':
            postfix.append(int(txt[i]))
            cnt += 1

        else:
            op.append(txt[i])
