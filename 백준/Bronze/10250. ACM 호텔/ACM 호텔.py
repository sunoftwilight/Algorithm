for _ in range(int(input())):
    H, W, N = map(int, input().split())

    num = N // H + 1
    floor = N % H

    if not floor:
        num -= 1
        floor = H

    print(str(floor) + str(num).zfill(2))