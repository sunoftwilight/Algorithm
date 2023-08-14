txt = input()
N = len(txt)

stack = []
flag = 0

for i in range(N):
    if txt[i] == '-':
        stack.append(txt[i])
        stack.append('(')
        flag = 1

    elif flag == 1 and ((i+1 < N and txt[i+1] == '-') or i == N-1):
        stack.append(txt[i])
        stack.append(')')
        flag = 0

    else:
        stack.append(txt[i])

a = []
ans = []
not_num = ['(', ')', '-', '+']

for i in range(len(stack)):
    if stack[i] not in not_num:   # 네개 다 아니어야하므로 and로 묶기!! (아무 생각없이 이거나 이거나 이거가 아니어야댐~ 했다가 or로 적으면 안댄다..)
        a.append(stack[i])
        if i == len(stack) - 1:
            ans.append(str(int(''.join(a))))

    else:
        if a:
            ans.append(str(int(''.join(a))))
        ans.append(stack[i])
        a.clear()

print(eval(''.join(ans)))
