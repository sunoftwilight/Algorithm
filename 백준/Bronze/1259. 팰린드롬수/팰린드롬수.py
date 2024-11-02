while True:
    num = input()
    if num == '0':
        break

    N = len(num)
    quest = N // 2
    is_palin = True

    for i in range(quest):
        if num[i] != num[N - 1 - i]:
            is_palin = False
            break

    if is_palin:
        print('yes')
    else:
        print('no')
