def paint(x1, y1, x2, y2):
    paint_lst = []

    for i in range(y2 - y1 + 1):
        for j in range(x2 - x1 + 1):
            paint_lst.append((y1 + i, x1 + j))

    return paint_lst


T = int(input())

for tc in range(1, T + 1):
    red = []
    blue = []

    area = int(input())

    for _ in range(area):
        a1, a2, b1, b2, c1 = map(int, input().split())

        if c1 == 1:
            red.extend(paint(a1, a2, b1, b2))

        if c1 == 2:
            blue.extend(paint(a1, a2, b1, b2))

    cnt = 0
    red = set(red)
    blue = set(blue)

    for search in red:                 # set은 &를 통해서 공통된 것 추출 가능
        if search in blue:
            cnt += 1

    print(f'#{tc} {cnt}')
