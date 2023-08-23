T = int(input())

for tc in range(1, T+1):
    N, num = input().split()

    sixteen = {
        '0' : 0,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        'A' : 10,
        'B' : 11,
        'C' : 12,
        'D' : 13,
        'E' : 14,
        'F' : 15,
        'G' : 16

    }

    ten = 0

    for i in range(int(N)):
        k = sixteen[num[i]]
        ten += (16 ** (int(N)-1-i)) * k

    two = []

    while ten > 0:
        trans = ten % 2
        two.append(trans)
        ten //= 2

        if ten == 0 or ten == 1:
            two.append(ten)
            while len(two) % 4:
                two.append(0)
            break

    print(f'#{tc}', end=' ')
    for i in range(len(two)-1, -1, -1):
        print(two[i], end='')
    print()
