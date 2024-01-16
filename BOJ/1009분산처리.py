rot = {
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1],
    0: [0],
}

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    a %= 10

    if a == 0:
        num = 10

    elif a == 1 or 5 or 6:
        num = a

    else:
        this_rot = rot[a]
        num = this_rot[b % len(this_rot) - 1]

    print(num)
