T = int(input())

for tc in range(1, T+1):
    N = int(input())
    p = [0] * (N + 1)

    for _ in range(N-1):
        A, B = map(int, input().split())
        p[B] = A

    nd1, nd2 = map(int, input().split())

    anc1 = [nd1]
    anc2 = [nd2]

    while p[nd1] != 0:
        anc1.append(p[nd1])
        nd1 = p[nd1]

    while p[nd2] != 0:
        anc2.append(p[nd2])
        nd2 = p[nd2]

    inter = [x for x in anc1 if x in anc2]
    print(inter[0])
    # for x in anc1:
    #     if x in anc2:
    #         print(x)
    #         break
