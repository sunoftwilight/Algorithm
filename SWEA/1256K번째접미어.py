T = int(input())

for tc in range(1, T+1):
    K = int(input())
    txt = input()

    lst = []
    for i in range(len(txt)):
        lst.append(txt[i:])

    lst.sort()

    print(f'#{tc} {lst[K-1]}')
