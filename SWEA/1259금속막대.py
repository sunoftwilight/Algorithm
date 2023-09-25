T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    nasa = []
    for k in range(N):
        nasa.append(arr[2 * k: 2 * k + 2])

    ml = []
    ml.append(nasa.pop(0))

    i = j = 0
    while nasa:
        if ml[0][0] == nasa[j][1]:
            inst = nasa.pop(j)
            ml.insert(0, inst)
            i += 1
            j = 0

        elif ml[i][1] == nasa[j][0]:
            inst = nasa.pop(j)
            ml.append(inst)
            i += 1
            j = 0

        else:
            j += 1

    print(f'#{tc}', end=' ')
    for m in range(N):
        print(*ml[m], end=' ')
    print()
