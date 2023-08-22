def inorder(node):
    global n

    if node <= N:
        inorder(2 * node)
        tree[node] = n
        n += 1
        inorder(2 * node + 1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    n = 1
    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')
