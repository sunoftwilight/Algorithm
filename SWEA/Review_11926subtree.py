def preorder(n):
    global cnt

    if n:
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])


# 완전 이진 트리 아님!
T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())        # 간선 개수, 시작 노드
    V = E + 1
    ch1 = [0] * (V + 1)                     # tree : (정점 개수 - 1) = 간선 개수
    ch2 = [0] * (V + 1)

    tmp = list(map(int, input().split()))

    # 주어진 트리에 맞게 숫자 채워넣기
    for i in range(E):
        p = tmp[i * 2]        # 입력에서 부모 노드 저장된 인덱스
        c = tmp[i * 2 + 1]    # 입력에서 자식 노드 저장된 인덱스

        if ch1[p] == 0:       # 부모노드의 왼쪽 자식 비었으면
            ch1[p] = c        # 채워넣고

        else:                 # 이미 차있으면
            ch2[p] = c        # 오른쪽 자식 자리에 채워넣어

    cnt = 0
    preorder(N)

    print(f'#{tc} {cnt}')
