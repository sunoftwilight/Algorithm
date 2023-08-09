T = 10

for tc in range(1, T+1):
    case = int(input())

    f_txt = input()
    f = len(f_txt)

    s_txt = input()
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

    print(f'#{tc} {cnt}')

# # while 대신 사용 가능
# for i in range(s-f+1):
#     for j in range(f):
#         if s_txt[i + j] != f_txt[j]:
#             break
#
#     else:
#         cnt += 1
