T = 10

for tc in range(1, T+1):
    N, num = map(str, input().split())

    stack = []

    for i in num:
        if stack and stack[-1] == i:
            stack.pop()

        else:
            stack.append(i)

    print(f'#{tc} {"".join(stack)}')