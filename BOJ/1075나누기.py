N = int(input())
F = int(input())

remain = N % F 

lastN = int(''.join(list(str(N))[-2:]))

new = N - remain
num = int(''.join(list(str(new))[-2:]))

if F != 100:
    if lastN < F :
        if num + (F - remain) < 100 :
            N = N + (F - remain)
            num = int(''.join(list(str(N))[-2:]))

    while (num - F) >= 0 :
        num -= F

print(str(num).zfill(2))