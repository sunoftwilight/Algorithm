def choice(k, jack, visit):
    global answer

    if k == 3:
        score = sum(jack)

        if score <= M:
            answer = max(answer, score)
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = True
            choice(k+1, jack + [cards[i]], visit)
            visit[i] = False


N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort()

answer = 0
visited = [False] * N
choice(0, [], visited)

print(answer)