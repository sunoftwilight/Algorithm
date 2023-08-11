# T = 10
#
# for tc in range(1, T+1):
#     N, num = map(str, input().split())
#
#     stack = []
#
#     for i in num:
#         if stack and stack[-1] == i:
#             stack.pop()
#
#         else:
#             stack.append(i)
#
#     print(f'#{tc} {"".join(stack)}')


# Live review
T = 10

for tc in range(1, T+1):
    str_N, str_num = input().split()

    N = int(str_N)
    stack = [0] * N
    top = -1

    for t in str_num:
        if top == -1 or stack[top] != t:      # 스택이 비어있거나, top 원소와 다르면 push(t)
            top += 1
            stack[top] = t

        else:                                 # 스택이 비어있지 않고, top과 같으면
            top = -1

    print(f'#{tc} {"".join(stack[:top+1])}')
