def calc(op, left, right):
    if op == '+':
        result = left + right
        return result

    elif op == '-':
        result = left - right
        return result

    elif op == '*':
        result = left * right
        return result

    elif op == '/':
        result = left / right
        return result


def postorder(v):
    if ch1[v] == 0 and ch2[v] == 0:
        return num[v]
    else:
        left = postorder(ch1[v])
        right = postorder(ch2[v])
        num[v] = calc(op[v], left, right)
        return num[v]


T = 10

for tc in range(1, T+1):
    N = int(input())

    op = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    num = [0] * (N + 1)

    for i in range(N):
        tmp = list(input().split())
        idx = int(tmp[0])

        if tmp[1] == '+' or tmp[1] == '-' or tmp[1] == '*' or tmp[1] == '/':
            op[idx] = tmp[1]
            ch1[idx] = int(tmp[2])
            ch2[idx] = int(tmp[3])

        else:
            num[idx] = int(tmp[1])

    ans = postorder(1)

    print(f'#{tc} {int(ans)}')