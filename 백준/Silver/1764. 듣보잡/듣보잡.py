N, M = map(int, input().split())
peoples = dict()
cnt = 0

for _ in range(N + M):
    name = input()
    peoples[name] = peoples.get(name, 0) + 1

    if peoples[name] >= 2:
        cnt += 1

sorted_peoples = dict(sorted(peoples.items()))

print(cnt)
for name, k in sorted_peoples.items():
    if k >= 2:
        print(name)
