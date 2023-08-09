T = int(input())

for tc in range(1, T+1):
    f_str = input()
    s_str = input()

    f_dic = {}

    for i in f_str:
        f_dic.setdefault(i, 0)

    for j in range(len(s_str)):
        if f_dic.get(s_str[j]) != None:
            f_dic[s_str[j]] += 1

    lst = list(f_dic.values())

    many = lst[0]
    for k in range(len(lst)):
        if many < lst[k]:
            many = lst[k]

    print(f'#{tc} {many}')