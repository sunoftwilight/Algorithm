T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())))

    match = 0

    for a in A:
        for b in B:
            if a > b:
                match += 1
                print(a, b)
            else:
                break

    print(match)
