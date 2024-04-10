import heapq

def solution(operations):
    answer = []
    heap = []

    for cmd in operations:
        if cmd.startswith('I'):
            num = int(cmd.split('I ')[1])
            heapq.heappush(heap, num)

        elif heap:
            if cmd == "D 1":
                heap.pop()

            elif cmd == "D -1":
                heapq.heappop(heap)

    if not heap:
        answer = [0, 0]

    else:
        answer = [max(heap), min(heap)]

    return answer