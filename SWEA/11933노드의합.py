def postorder(node):
    global sum_son

    if node <= N:
        postorder(2*node)
        postorder(2*node + 1)
        sum_son += tree[node]
        tree[node] = sum_son


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    tree = [0] * (N+1)

    for _ in range(M):
        node, val = map(int, input().split())
        tree[node] = val

    sum_son = 0
    postorder(1)

    print(f'#{tc} {tree[L]}')
