T = int(input())

for tc in range(1, T+1):
    N = int(input())

    a = b = c = d = e = 0

    dic = {'2': a, '3': b, '5': c, '7': d, '11': e}

    for i in list(dic.keys()):
        while N % int(i) == 0:
            N = N / int(i)
            dic[i] += 1

    print(f'#{tc} {dic["2"]} {dic["3"]} {dic["5"]} {dic["7"]} {dic["11"]}')
