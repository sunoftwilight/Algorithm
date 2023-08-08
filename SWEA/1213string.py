T = 10

for tc in range(1, T+1):
    case = int(input())
    f_txt = input()
    f = len(f_txt)
    s_txt = input()
    s = len(s_txt)

    cnt = 0

    for i in range(s-f+1):
        for j in range(f):
            if s_txt[i + j] != f_txt[j]:
                break

        else:
            cnt += 1

    print(f'#{tc} {cnt}')
