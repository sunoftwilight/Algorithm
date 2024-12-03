A = int(input())
B = int(input())
C = int(input())

num = str(A * B * C)
cnt = dict()

for n in range(10):
    cnt[n] = num.count(str(n))

for value in cnt.values():
    print(value)