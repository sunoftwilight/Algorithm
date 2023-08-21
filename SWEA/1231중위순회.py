import sys; sys.stdin = open('1231_input.txt')


def inorder(node):
    if node <= N:
        inorder(node*2)
        ans.append(tree[node])
        inorder(node*2+1)


T = 10

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)

    for i in range(N):
        arr = list(input().split())
        tree[i + 1] = arr[1]

    ans = []
    inorder(1)

    print(f'#{tc} {"".join(ans)}')
