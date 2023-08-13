# def push(a):
#     global top
#
#     top += 1
#
#     if top == len(txt):
#         return "overflow"
#
#     else:
#         stack[top] = a
#
# def pop():
#     global top
#
#     if top == -1:
#         return "underflow"
#
#     else:
#         top -= 1
#         return stack[top+1]


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

#
# T = int(input())
#
# for tc in range(1, T+1):
#     top = -1
#
#     txt = input()
#
#     stack = [0] * len(txt)
#
#     for i in range(len(txt)):
#         if txt[i] == stack[top] and top > -1:
#             pop()
#         else:
#             push(txt[i])
#
#     print(f'#{tc} {top + 1}')


# 0813
# T = int(input())
#
# for tc in range(1, T+1):
#     txt = input()
#     N = len(txt)
#
#     stack = [''] * N
#
#     for i in range(N):
#         if stack and stack[-1] == txt[i]:
#             stack.pop()
#
#         else:
#             stack.append(txt[i])
#
#     ans = len(''.join(stack))
#
#     print(f'#{tc} {ans}')


def push(a):
    global top

    top += 1

    if top == len(txt):
        print("overflow")
        return 0

    else:
        stack[top] = a


def pop():
    global top

    # top -= 1      # 이게 여기 있으면 stack 비어있을 때 pop해도 top이 -2를 일단 가리키게 됨

    if top < -1:
        print("underflow")
        return 0

    else:
        top -= 1    # 그니까 stack이 안비었을 때만 -1 해주기
        return stack[top+1]


T = int(input())

for tc in range(1, T+1):
    txt = input()
    N = len(txt)

    top = -1

    stack = [''] * N

    for i in range(N):
        if stack and stack[top] == txt[i]:
            pop()

        else:
            push(txt[i])

    print(f'#{tc} {top+1}')