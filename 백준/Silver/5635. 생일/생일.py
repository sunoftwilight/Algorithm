N = int(input())
students = [input().split(' ') for _ in range(N)]

sorting = []

for name, d, m, y in students:
    sorting.append((int(y), int(m), int(d), name))

sorting.sort()

print(sorting[-1][3])
print(sorting[0][3])
