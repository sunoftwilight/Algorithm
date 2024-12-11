N = int(input())
peoples = []

for i in range(N):
    ip = input().split()
    age, name = int(ip[0]), ip[1]

    peoples.append((age, i, name))

peoples.sort()

for age, num, name in peoples:
    print(age, name)