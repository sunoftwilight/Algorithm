def enQ(v):
    global last

    # 완전 이진 트리
    last += 1
    heap[last] = v

    # 부모 < 자식 (최소합)
    c = last
    p = c // 2

    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    last = 0
    heap = [0] * (N+1)

    tmp = list(map(int, input().split()))

    for i in range(N):
        enQ(tmp[i])

    print(f'#{tc} {find_a()}')