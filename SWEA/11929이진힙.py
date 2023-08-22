def enq(node):
    global last

    last += 1
    heap[last] = node

    c = last
    p = c // 2

    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


def sum(n):
    global sum_p
    if n > 0:
        n //= 2
        sum_p += heap[n]
        sum(n)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = [0] * (N+1)
    last = 0

    for i in range(N):
        enq(arr[i])

    sum_p = 0
    sum(N)

    print(f'#{tc} {sum_p}')
