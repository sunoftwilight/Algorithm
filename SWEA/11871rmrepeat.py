def push(a):
    global top

    top += 1

    if top == len(txt):
        return "overflow"

    else:
        stack[top] = a

# def push(a):
#     stack.append(a)


def pop():
    global top

    if top == -1:
        return "underflow"

    else:
        top -= 1
        return stack[top+1]


# T = int(input())
#
# for tc in range(1, T+1):
#     top = -1
#
#     txt = list(input())
#
#     stack = [0] * len(txt)
#
#     while len(txt) > 0:
#         last = txt.pop()
#
#         if len(txt) > 0 and last == txt[-1]:
#             txt.pop()
#
#         elif last == stack[-1]:
#             stack.pop()
#
#         else:
#             push(last)
#
#     ans = 0
#
#     while stack[-1] != 0:
#         ans += 1
#         stack.pop()
#
#     print(f'#{tc} {ans}')


T = int(input())

for tc in range(1, T+1):
    top = -1

    txt = input()

    stack = [0] * len(txt)

    for i in range(len(txt)):
        if txt[i] == stack[top] and top > -1:
            pop()
        else:
            push(txt[i])

    print(f'#{tc} {top + 1}')




