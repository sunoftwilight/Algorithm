N, K = map(int, input().split())
medal = [[0, 0, 0, 0]]
medal += [list(map(int, input().split())) for _ in range(N)]
medal.sort()

rank = 1
for i in range(1, N+1):
    if i != K:
        if medal[i][1] > medal[K][1]:
            rank += 1

        elif medal[i][1] == medal[K][1] and medal[i][2] > medal[K][2]:
            rank += 1

        elif medal[i][1] == medal[K][1] and medal[i][2] == medal[K][2] and medal[i][3] > medal[K][3]:
            rank += 1

print(rank)