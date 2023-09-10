import heapq, sys

N = int(input())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if num:
        heapq.heappush(heap, (abs(num),num))

    else:
        if heap:
            print(heapq.heappop(heap)[1])

        else:
            print(0)
