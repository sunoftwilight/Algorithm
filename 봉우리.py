T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    top = []

    for i in range(1, N-1):
        for j in range(1, N-1):
            max_nine = arr[i][j]
            flag = 1
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < N and 0 <= nj < N:
                    if max_nine <= arr[ni][nj]:
                        flag = 0

            if flag:
                top.append(arr[i][j])

    if len(top) <= 1:
        ans = -1

    else:
        most_h = most_l = top[0]

        for i in range(len(top)):
            if top[i] < most_l:
                most_l = top[i]

            if most_h < top[i]:
                most_h = top[i]

        ans = most_h - most_l

    print(f'#{tc} {ans}')