import sys

N = int(input())
stack = []

for _ in range(N):
    cmd = sys.stdin.readline().strip()

    if cmd.startswith('push'):
        msg, num = cmd.split()

        stack.append(num)

    elif cmd == 'pop':
        if stack:
            n = stack.pop()
            print(n)
        else:
            print(-1)

    elif cmd == 'size':
        print(len(stack))

    elif cmd == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)