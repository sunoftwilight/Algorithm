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


T = 10

for tc in range(1, T+1):
    no = int(input())
    arr = list(map(int, input().split()))
    size = len(arr)

    queue = [0] * size

    front = rear = 0

    for i in range(size):
        enq(arr[i])

    num = [1, 2, 3, 4, 5]
    i = 0
    while queue[rear] > 0:
        a = queue[front] - num[i]
        if a <= 0:
            a = 0
        deq()
        enq(a)
        i = (i + 1) % 5

    print(f'#{tc}', end=' ')
    for i in range(size):
        print(queue[(front + i) % size], end=' ')
    print()
