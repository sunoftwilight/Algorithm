T = int(input())

for tc in range(1, T+1):
    s_txt, f_txt = map(str, input().split())
    f = len(f_txt)
    s = len(s_txt)

    cnt = 0

    for i in range(s - f + 1):
        crrt = 0
        for j in range(f):
            if s_txt[i + j] == f_txt[j]:
                crrt += 1
            else:
                break

        if crrt == len(f_txt):
            cnt += 1

    typing = cnt + (s - f * cnt)

    print(f'#{tc} {typing}')
