T = int(input())

for tc in range(1, T+1):
    txt = list(input().split())
    N = len(txt)

    stack = []
    flag = 0

    for i in range(N):
        if txt[i] not in ['+', '*', '-', '/', '.']:
            stack.append(int(txt[i]))

        else:
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()

                if txt[i] == '+':
                    stack.append(a + b)

                elif txt[i] == '-':
                    stack.append(a - b)

                elif txt[i] == '*':
                    stack.append(a * b)

                elif txt[i] == '/':
                    stack.append(a // b)

                elif txt[i] == '.':
                    flag = 'error'
                    break

            elif txt[i] == '.':
                flag = stack[-1]

            else:
                flag = 'error'
                break

    print(f'#{tc} {flag}')
