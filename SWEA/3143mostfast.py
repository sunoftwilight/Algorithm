T = int(input())

for tc in range(1, T+1):
    s_txt, f_txt = map(str, input().split())
    f = len(f_txt)
    s = len(s_txt)

    cnt = 0
    i = j = 0

    while i < s and j < f:
        if s_txt[i] != f_txt[j]:
            i = i - j
            j = -1

        i += 1
        j += 1

        if j == f:
            cnt += 1
            j = 0

    typing = cnt + (s - f * cnt)
    print(f'#{tc} {typing}')
