from collections import deque

T = int(input())

for _ in range(T):
    msg = input()
    stack = deque([])

    idx = 0
    len_msg = len(msg)

    is_VPS = True

    while True:
        if idx < len_msg:
            if msg[idx] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()

                else:
                    is_VPS = False
                    break

            else:
                stack.append(msg[idx])

            idx += 1

        else:
            break

    if is_VPS:
        if stack:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')

