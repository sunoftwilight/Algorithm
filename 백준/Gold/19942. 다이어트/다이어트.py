def choice(depth, p, f, s, v, cost, ing):
    global min_cost, min_ing

    if cost > min_cost:
        return

    if p >= pro and f >= fat and s >= carb and v >= vita:
        if cost == min_cost:
            ing.sort()
            min_ing.append(ing)

        elif cost < min_cost:
            min_cost = cost
            min_ing = [ing]

        else:
            return

    if depth == N:
        return

    choice(depth + 1, p + info[depth][0], f + info[depth][1], s + info[depth][2], v + info[depth][3], cost + info[depth][4], ing + [depth + 1])
    choice(depth + 1, p, f, s, v, cost, ing)


N = int(input())
pro, fat, carb, vita = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

min_cost = float('inf')
min_ing = []

choice(0, 0, 0, 0, 0, 0, [])

if min_ing:
    min_ing.sort()
    print(min_cost)
    print(*min_ing[0])

else:
    print(-1)
