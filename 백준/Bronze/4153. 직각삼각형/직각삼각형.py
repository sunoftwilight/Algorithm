while True:
    ip = input()
    if ip == '0 0 0':
        break
        
    lengths = list(map(int, ip.split()))
    lengths.sort()

    answer = 'right' if lengths[0] ** 2 + lengths[1] ** 2 == lengths[2] ** 2 else 'wrong'
    print(answer)
