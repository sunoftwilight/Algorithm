def mix(depth, sour, acerbity):
    global answer

    if depth == N:
        if acerbity:
            answer = min(answer, abs(sour - acerbity))
        return

    mix(depth + 1, sour * ing[depth][0], acerbity + ing[depth][1])
    mix(depth + 1, sour, acerbity)


N = int(input())
ing = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')

mix(0, 1, 0)
print(answer)
