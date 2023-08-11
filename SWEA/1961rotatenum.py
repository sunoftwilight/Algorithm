T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rt_one = [[] for _ in range(N)]
    rt_two = [[] for _ in range(N)]
    rt_three = [[] for _ in range(N)]

    # 90도
    for j in range(N):
        for i in range(N-1, -1, -1):
            rt_one[j].append(str(arr[i][j]))

    # 180도
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            rt_two[(N-1)-i].append(str(arr[i][j]))

    # 270도
    for j in range(N-1, -1, -1):
        for i in range(N):
            rt_three[(N-1)-j].append(str(arr[i][j]))

    # 출력 형태
    print(f'#{tc}')
    for p in range(N):
        print(''.join(rt_one[p]), ''.join(rt_two[p]), ''.join(rt_three[p]))
