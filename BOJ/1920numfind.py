# N = int(input())
# N_lst = list(map(int, input().split()))
#
# M = int(input())
# M_lst = list(map(int, input().split()))
#
# for m in M_lst:
#     if m in N_lst:
#         print(1)
#     else:
#         print(0)


N = int(input())
N_lst = list(map(int, input().split()))

M = int(input())
M_lst = list(map(int, input().split()))

inter = set(N_lst).intersection(set(M_lst))

for m in M_lst:
    if m in inter:
        print(1)
    else:
        print(0)
