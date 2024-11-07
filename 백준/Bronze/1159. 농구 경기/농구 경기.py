N = int(input())
players = [input() for _ in range(N)]

first_names = {}
answer = []

for player in players:
    first_names[player[0]] = first_names.get(player[0], 0) + 1

for key, value in first_names.items():
    if value >= 5:
        answer.append(key)

if answer:
    answer.sort()
    print(''.join(answer))
else:
    print('PREDAJA')
