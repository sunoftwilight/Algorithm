def enq(a):
    global size, rear, front

    if (rear + 1) % size == front:
        front = (front + 1) % size
    rear = (rear + 1) % size
    queue[rear] = a


def deq():
    global size, front

    front = (front + 1) % size
    return queue[front]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    size = len(arr)

    queue = [0] * size
    front = rear = 0

    for i in range(size):
        enq(arr[i])

    for _ in range(M):
        a = queue[front]
        deq()
        enq(a)

    print(f'#{tc} {queue[front]}')
