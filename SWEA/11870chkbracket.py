T = int(input())

for tc in range(1, T+1):
    txt = input()

    stack = [''] * len(txt)

    flag = 1

    for i in range(len(txt)):
        if txt[i] == '(' or txt[i] == '{':
            stack.append(txt[i])

        elif txt[i] == ')':
            if stack[-1] == '(' and len(stack) > 0:
                stack.pop()
            else:
                flag = 0

        elif txt[i] == '}':
            if stack[-1] == '{' and len(stack) > 0:
                stack.pop()
            else:
                flag = 0

    print(f'#{tc} {flag}')
