N, r, c = map(int, input().split())
direct = [(0, 1), (1, -1), (0, 1)]

answer = 0

while N > 0:
    mid = 2 ** (N-1)
    N -= 1
    loc = 0

    if r < mid and c < mid:
        loc = 1

    elif r < mid and c >= mid:
        loc = 2
        c -= mid

    elif r >= mid and c < mid:
        loc = 3
        r -= mid

    elif r >= mid and c >= mid:
        loc = 4
        r -= mid
        c -= mid

    answer += (mid ** 2) * (loc - 1)

print(answer)
