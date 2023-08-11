T = int(input())

for tc in range(1, T+1):
    brkt = input()

    cnt = 0
    stack = []
    i = 0

    while i < len(brkt):
        if brkt[i] == '(' and brkt[i+1] == ')' and i+1 < len(brkt):
            cnt += len(stack)
            i += 2

        elif brkt[i] == '(':
            stack.append(i)
            i += 1

        elif stack and brkt[i] == ')':
            stack.pop()
            cnt += 1
            i += 1

    print(f'#{tc} {cnt}')
