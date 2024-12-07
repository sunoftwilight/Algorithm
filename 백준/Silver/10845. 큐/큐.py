import sys
from collections import deque

N = int(sys.stdin.readline())
Q = deque()

for i in range(N):
    ip = list(sys.stdin.readline().split())

    if len(ip) == 1:
        cmd = ip[0]
    else:
        cmd, num = ip[0], ip[1]

    if cmd == 'push':
        Q.append(num)

    elif cmd == 'pop':
        if Q:
            n = Q.popleft()
            print(n)
        else:
            print(-1)

    elif cmd == 'size':
        print(len(Q))

    elif cmd == 'empty':
        if Q:
            print(0)
        else:
            print(1)

    elif cmd == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)

    elif cmd == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)
