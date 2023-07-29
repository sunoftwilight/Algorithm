# T = int(input())

# num_lst = list(map(int, input().split()))
# num_lst = sorted(num_lst)

# leng = len(num_lst)

# origin = num_lst[0] * num_lst[leng-1]

# print(origin)

T = int(input())

num_lst = list(map(int, input().split()))

origin = max(num_lst) * min(num_lst)

print(origin)