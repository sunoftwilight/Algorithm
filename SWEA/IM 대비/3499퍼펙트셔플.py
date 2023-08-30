T = int(input())

for tc in range(1, T+1):
    N = int(input())

    deck = list(input().split())

    if N % 2:
        front = deck[: N // 2 + 1]
        back = deck[N // 2 + 1 :]
    else:
        front = deck[: N // 2]
        back = deck[N // 2 :]

    shuffle = []

    for i in range(N):
        if i % 2:
            shuffle.append(back.pop(0))
        else:
            shuffle.append(front.pop(0))

    print(f'#{tc}', *shuffle)
