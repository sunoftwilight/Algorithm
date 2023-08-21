nanjaeng = []

for k in range(9):
    nanjaeng.append(int(input()))

nine = sum(nanjaeng)
i = seven = 0
j = 1

while i < 8 and j < 9:
    seven = nine - nanjaeng[i] - nanjaeng[j]

    if seven == 100:
        nanjaeng.pop(j)
        nanjaeng.pop(i)
        break

    else:
        if j == 8:
            i += 1
            j = i + 1

        else:
            j += 1

nanjaeng.sort()

for i in range(len(nanjaeng)):
    print(nanjaeng[i])
