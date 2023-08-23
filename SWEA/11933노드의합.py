def parents(node):
    global sum_son

    if 2 * node <= N:
        sum_son += tree[2 * node]

    if 2 * node + 1 <= N:
        sum_son += tree[2 * node + 1]

    if sum_son:
        tree[node] = sum_son
    sum_son = 0


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    tree = [0] * (N+1)

    for _ in range(M):
        node, val = map(int, input().split())
        tree[node] = val

    sum_son = 0

    for i in range(N, 0, -1):
        parents(i)

    print(f'#{tc} {tree[L]}')
