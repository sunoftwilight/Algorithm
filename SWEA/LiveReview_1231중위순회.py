import sys; sys.stdin = open('1231_input.txt')


def inorder(node, N):                # N : 완전 이진 트리의 마지막 정점
    if node <= N:
        inorder(node*2, N)              # 왼쪽 자식으로 이동
        print(tree[node], end='')    # 중위 순회에서 할 일
        inorder(node*2+1, N)            # 오른쪽 자식으로 이동


T = 10

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)               # N번 노드까지 있는 완전 이진 트리

    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]

    # 중위 순회
    print(f'#{tc}', end=' ')
    inorder(1, N)    # root = 1
    print()
