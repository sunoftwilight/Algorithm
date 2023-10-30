import sys; sys.setrecursionlimit(10**9)


def postorder(s, e):
    if s > e:
        return

    # 만약 root보다 큰 값 없는 경우 전부 왼쪽 서브트리로 취급
    rt_s = e + 1

    for i in range(s+1, e+1):
        if tree[s] < tree[i]:
            rt_s = i
            break

    # root 다음부터 왼쪽 서브트리 탐색
    postorder(s+1, rt_s-1)
    # 왼쪽 서브트리 탐색 끝나면 오른쪽 서브트리 탐색
    postorder(rt_s, e)
    # 왼쪽, 오른쪽 서브트리 탐색 끝나면 root 출력
    print(tree[s])


tree = []

while True:
    try:
        tree.append(int(input()))
    except:
        break

postorder(0, len(tree)-1)