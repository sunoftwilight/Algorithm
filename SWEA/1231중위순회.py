<<<<<<< HEAD
import sys; sys.stdin = open('1231_input.txt')


def inorder(node):
    if node <= N:
        inorder(node*2)
        ans.append(tree[node])
        inorder(node*2+1)


=======
>>>>>>> d3f19017c430de60dc709f7ea94218cb2622b5c5
T = 10

for tc in range(1, T+1):
    N = int(input())
<<<<<<< HEAD
    tree = [0] * (N+1)

    for i in range(N):
        arr = list(input().split())
        tree[i + 1] = arr[1]

    ans = []
    inorder(1)

    print(f'#{tc} {"".join(ans)}')
=======
    # arr = [list(input().split()) for _ in range(N)]

    tree = [[0] * 3 for _ in range(N+1)]

    for i in range(N):
        tmp = list(input().split())
        tree[int(arr[i][0])][0] = int(arr[i][2])
        tree[int(arr[i][0])][1] = int(arr[i][3])
        tree[int(arr[i][0])]

>>>>>>> d3f19017c430de60dc709f7ea94218cb2622b5c5
