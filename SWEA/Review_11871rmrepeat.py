def is_empty(stack):
    if top == -1:
        return True
    else:
        return False


def push(stack, item):
    global top
    top += 1
    stack[top] = item


def peek(stack):
    return stack[top]      # return만 하고 top의 변화는 X = 그냥 보기만!


def pop(stack):
    global  top
    if top == -1:          # 비어있는지 확인
        return

    else:
        result = stack[top]
        top -= 1
        return result


T = int(input())

for tc in range(1, T+1):
    str = input()
    N = len(str)
    stack = [0] * 1000
    top = -1

    for i in range(N):
        if is_empty(stack):       # stack이 비어 있으면 -> push()
            push(stack, str[i])

        else:                               # stack이 비어있지 않으면
            if peek(stack) == str[i]:       # stack의 맨 위의 요소와 비교 (by peek)
                pop(stack)

            else:
                push(stack, str[i])

    print(f'#{tc} {top + 1}')

