N = input()
F = int(input())

N_list = list(N)
N_list[-1] = N_list[-2] = '0'

new = int(''.join(N_list))

while True :
    if new % F == 0 :
        break
    new += 1

result = ''.join(list(str(new))[-2:])

print(result)
