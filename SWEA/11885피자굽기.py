def enq(item):
    global front, rear, size

    if (rear + 1) % size == front:
        front = (front + 1) % size
    rear = (rear + 1) % size
    queue[rear] = item


def deq():
    global front, rear, size

    front = (front + 1) % size
    return queue[front]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    size = N

    queue = [0] * N
    front = rear = 0

    for i in range(N):
        enq(cheese[i])

    cnt = 0
    i = N
    pizza = N
    while queue.count(0) < N-1:
        while i < M:
            if cnt % N == 0:
                queue = list(map(lambda x: x // 2, queue))

            if queue[front] == 0:
                deq()
                enq(cheese[i])
                pizza += 1
                i += 1

            a = queue[front]
            deq()
            enq(a)
            pizza += 1
            cnt += 1

        if cnt % N == 0:
            queue = list(map(lambda x: x // 2, queue))

        if queue[front] == 0:
            deq()

        a = queue[front]
        deq()
        enq(a)
        cnt += 1

    print(f'#{tc} {front}')
