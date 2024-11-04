N = int(input())
buildings = list(map(int, input().split(' ')))

can_see = [0] * N

for i in range(N):
    cx, cy = i, buildings[i]

    for j in range(N):
        if i == j:
            continue

        bx, by = j, buildings[j]
        slope = (cy - by) / (cx - bx)
        intercept = cy - slope * cx

        s, e = j+1, i-1

        if i < j:
            s, e = i+1, j-1

        is_see = True

        while s <= e:
            mx, my = s, buildings[s]

            if my >= mx * slope + intercept:
                is_see = False
                break

            s += 1

        if is_see:
            can_see[i] += 1

print(max(can_see))
