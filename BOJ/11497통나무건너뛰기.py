T = int(input())

for tc in range(T):
    N = int(input())
    loges = sorted(list(map(int, input().split())))

    new = [0] * N

    for i in range(N):
        if i % 2 == 0:
            new[i//2] = loges[i]

        else:
            new[N-1-(i//2)] = loges[i]

    max_diff = 0

    for j in range(1, N):
        max_diff = max(abs(new[j-1] - new[j]), max_diff)

    print(max_diff)
