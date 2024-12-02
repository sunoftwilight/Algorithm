T = int(input())

for _ in range(T):
    num, msg = input().split()
    num = int(num)

    pw = ''
    for ap in msg:
        pw += ap * num

    print(pw)