text = input()

cro_alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0
new_txt = []
length_not = len(text)

for i in range(8):
    if cro_alph[i] in text:
        cnt += 1
        length_not -= len(cro_alph[i])
        i = 0

ans = length_not + cnt
print(ans)