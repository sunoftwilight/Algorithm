def postorder(v):
    if v <= N:
        postorder(v * 2)
        postorder(v * 2 + 1)

        # if랑 elif 순서 바뀌면 안됨!!!! 바뀌게 되면 오른쪽 자식 있는 애도 그냥 왼쪽 자식의 값만 더함!!
        if v * 2 + 1 <= N:
            tree[v] = tree[v * 2] + tree[v * 2 + 1]

        elif v * 2 <= N:
            tree[v] = tree[v * 2]


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)

    for _ in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num

    postorder(1)

    print(f'#{tc} {tree[L]}')
