T = int(input())

for tc in range(1, T+1):
    txt = input()

<<<<<<< HEAD
    stack = [''] * len(txt)
=======
    stack = []
>>>>>>> 96daf56d281bc2410319eaeca716e58e4b7067ce

    flag = 1

    for i in range(len(txt)):
        if txt[i] == '(' or txt[i] == '{':
            stack.append(txt[i])

        elif txt[i] == ')':
            if stack and stack[-1] == '(':
                # if stack[-1] == '(' and stack: 으로 조건을 주면,
                # stack이 빈 경우에 -1을 탐색하라고 하니까 인덱스 out이 발생함 = RuntimeError
                # 그니까 stack을 먼저 조건으로 줘서 만약에 빈거면 뒤에 조건은 검사 안하게 만들기 (단축검사)
                stack.pop()
            else:
                flag = 0

        elif txt[i] == '}':
<<<<<<< HEAD
            if stack[-1] == '{' and len(stack) > 0:
=======
            if stack and stack[-1] == '{':
>>>>>>> 96daf56d281bc2410319eaeca716e58e4b7067ce
                stack.pop()
            else:
                flag = 0

    if stack:
        flag = 0

    print(f'#{tc} {flag}')
