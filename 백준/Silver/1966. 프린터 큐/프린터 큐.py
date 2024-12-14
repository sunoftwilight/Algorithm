from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))

    printer = deque([])

    for i in range(N):
        printer.append((priority[i], i))

    sorted_priority = deque(sorted(priority, reverse=True))

    cnt = 0
    while True:
            pri, idx = printer.popleft()

            if pri == sorted_priority[0]:
                cnt += 1
                sorted_priority.popleft()

                if idx == M:
                    break

            else:
                printer.append((pri, idx))

    print(cnt)