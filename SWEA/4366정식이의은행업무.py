T = int(input())

for tc in range(1, T+1):
    Bin = input()
    Tri = input()

    sw_b = []
    sw_t = []

    for i in range(len(Bin)):
        if Bin[i] == '0':
            if i == len(Bin)-1:
                sw_b.append(Bin[:i] + '1')
            else:
                sw_b.append(Bin[:i] + '1' + Bin[i+1:])

        else:
            if i == len(Bin)-1:
                sw_b.append(Bin[:i] + '0')
            else:
                sw_b.append(Bin[:i] + '0' + Bin[i+1:])

    for i in range(len(Tri)):
        if Tri[i] == '0':
            if i == len(Tri) - 1:
                sw_t.append(Tri[:i] + '1')
                sw_t.append(Tri[:i] + '2')
            else:
                sw_t.append(Tri[:i] + '1' + Tri[i + 1:])
                sw_t.append(Tri[:i] + '2' + Tri[i + 1:])

        elif Tri[i] == '1':
            if i == len(Tri)-1:
                sw_t.append(Tri[:i] + '0')
                sw_t.append(Tri[:i] + '2')
            else:
                sw_t.append(Tri[:i] + '0' + Tri[i+1:])
                sw_t.append(Tri[:i] + '2' + Tri[i+1:])

        else:
            if i == len(Tri)-1:
                sw_t.append(Tri[:i] + '0')
                sw_t.append(Tri[:i] + '1')
            else:
                sw_t.append(Tri[:i] + '0' + Tri[i+1:])
                sw_t.append(Tri[:i] + '1' + Tri[i+1:])

    dec_b = []
    dec_t = []

    for i in sw_b:
        dec_b.append(int(i, 2))

    for i in sw_t:
        dec = int(i, 3)
        if dec in dec_b:
            print(f'#{tc} {dec}')
            break
    #
    # ans = 0
    #
    # for i in dec_b:
    #     if i in dec_t:
    #         ans = i
    #         break
    #
    # print(f'#{tc} {ans}')
