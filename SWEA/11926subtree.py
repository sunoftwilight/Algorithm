def inorder(node):
    global cnt

    if node:
        inorder(tree[node][0])
        cnt += 1
        inorder(tree[node][1])


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    tree = [[0] * 3 for _ in range(E+2)]

    # 주어진 트리에 맞게 숫자 채워넣기
    for i in range(E):
        p = arr[i * 2]        # 입력에서 부모 노드 저장된 인덱스
        c = arr[i * 2 + 1]    # 입력에서 자식 노드 저장된 인덱스

        if tree[p][0] == 0:   # 부모노드의 왼쪽 자식 비었으면
            tree[p][0] = c    # 채워넣고

        else:                 # 이미 차있으면
            tree[p][1] = c    # 오른쪽 자식 자리에 채워넣어

        # [c][2]는 c의 부모노드 자리 -> p 삽입
        tree[c][2] = p

    cnt = 0

    inorder(N)

    print(f'#{tc} {cnt}')
